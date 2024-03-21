import psycopg2
import vanna as vn
import logging
from cryptography.fernet import Fernet
import json
from vanna.local import LocalContext_OpenAI
import requests

logging.basicConfig(level=logging.CRITICAL)


def get_connection(api_key):
    _endpoint = "https://ask.vanna.ai/rpc"
    headers = {
        "Content-Type": "application/json",
        "Vanna-Key": api_key,
        "Vanna-Org": "demo-tpc-h",
    }
    data = {"method": 'list_orgs', "params": []}
    response = requests.post(_endpoint, headers=headers,
                             data=json.dumps(data))
    return response.json()


def decrypt_data(encrypted_data, key):
    """
    Decrypt the given encrypted data using the provided key.

    Args:
        encrypted_data (bytes): Encrypted data to be decrypted.
        key (bytes): Decryption key.

    Returns:
        str: Decrypted data as a string.

    Notes:
        This function uses Fernet symmetric encryption to decrypt the provided
        data.
    """
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_data).decode()


def get_model(api_key):
    """
    Retrieve an instance of the OpenAI model using the provided API key.

    Args:
        api_key (str): API key for accessing the OpenAI service.

    Returns:
        LocalContext_OpenAI: Instance of the OpenAI model.

    Notes:
        This function creates and returns an instance of the OpenAI model
        initialized with the provided API key.
    """
    return LocalContext_OpenAI({"api_key": api_key})


def train_model(*args):
    """
     Train the specified model using the provided arguments.

     Args:
         *args: Variable number of arguments, with the first argument being a
         dictionary containing the training parameters and the second argument
        being the secret key for decryption.

     Returns:
         None

     Notes:
         This function trains the specified model using the provided parameters.
         It interacts with a PostgreSQL database to retrieve model information
          and update training status. Additionally, it utilizes Vanna or
          OpenAI models based on the AI type specified in the parameters.
     """
    kwargs, secert_key = args
    kwargs = json.loads(decrypt_data(kwargs, secert_key))
    ai_type = kwargs.get("ai_type")
    vn_model_name = kwargs.get("vn_model_name")
    api_key = kwargs.get("api_key")
    model_name = kwargs.get("model_name")
    connection = kwargs.get("connection", False)
    dbname = kwargs.get("dbname", False)
    user = kwargs.get("user", False)
    pwd = kwargs.get("pwd", False)
    host = kwargs.get("host", False)
    port = kwargs.get("port", False)
    print(f"Training Started for {model_name}")
    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=pwd,
            host=host,
            port=port
        )

        def get_table_ddl(table_name, cur):
            cur.execute(f"""
                    SELECT column_name, data_type, is_nullable
                    FROM information_schema.columns
                    WHERE table_name = '{table_name}'
                    """)
            columns = cur.fetchall()

            cur.execute(f"""
                    SELECT
                        tc.table_name, kcu.column_name, ccu.table_name AS 
                        foreign_table_name, ccu.column_name
                        AS foreign_column_name
                    FROM
                        information_schema.table_constraints AS tc
                        JOIN information_schema.key_column_usage AS kcu
                            ON tc.constraint_name = kcu.constraint_name
                        JOIN information_schema.constraint_column_usage AS ccu
                            ON ccu.constraint_name = tc.constraint_name
                    WHERE
                        constraint_type = 'FOREIGN KEY' 
                        AND tc.table_name='{table_name}';
                    """)
            foreign_keys = cur.fetchall()

            ddl = f"CREATE TABLE IF NOT EXISTS public.{table_name}\n(\n"
            for column in columns:
                col_name, data_type, is_nullable = column
                ddl += (f"    {col_name} {data_type} "
                        f"{'' if is_nullable == 'YES' else 'NOT '}NULL,\n")

            # Add foreign key constraints
            for fk in foreign_keys:
                table_name, column_name, foreign_table, foreign_column = fk
                ddl += (f"    CONSTRAINT "
                        f"{table_name}_{column_name}_fkey "
                        f"FOREIGN KEY ({column_name})\n")
                ddl += (f"        REFERENCES "
                        f"public.{foreign_table} "
                        f"({foreign_column}) MATCH SIMPLE\n")
                ddl += "        ON UPDATE NO ACTION\n"
                ddl += "        ON DELETE SET NULL,\n"

            ddl += f"    CONSTRAINT {table_name}_pkey PRIMARY KEY (id)\n"

            ddl += ");"
            return ddl

        cursor = connection.cursor()
        if ai_type == "vanna":
            vn_models = get_connection(api_key)
            is_error = vn_models.get('error', False)
            if is_error:
                print("Connection error")
                # Since there is a connection error there is no need to
                # carry forward with this operation
                return
            vn.set_api_key(api_key)
            vn_models = vn.get_models()
            if vn_model_name.lower() not in vn_models:
                vn.create_model(model=vn_model_name.lower(), db_type="Postgres")
            vn.set_model(vn_model_name.lower())
        cursor.execute(
            f"""SELECT id, table_name FROM 
            ir_model WHERE model = '{model_name}';""")
        model_id = cursor.fetchall()
        model = vn
        if ai_type == "openai":
            model = get_model(api_key)
        if len(model_id):
            tabel_id, tables_name = model_id[0]
            cursor.execute("""
                UPDATE ai_train_info
                SET model_id = %s, is_active = %s, "table" = %s, state = %s
                WHERE model_name = %s
            """, (tabel_id, True, tables_name, 'done', model_name))
            connection.commit()
            print(f"Training Completed for {model_name}")
            ddl_val = get_table_ddl(tables_name, cursor)
            model.add_ddl(ddl_val)
    except Exception as e:
        print(f"An error occurred while training model {model_name}: {str(e)}")
    finally:
        if connection:
            connection.close()
