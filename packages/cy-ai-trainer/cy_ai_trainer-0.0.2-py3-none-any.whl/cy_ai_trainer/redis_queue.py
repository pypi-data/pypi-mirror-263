import time
from datetime import timedelta
from redis import Redis
from rq import Queue, Retry, Worker, Connection
from cy_ai_trainer.model_trainer import train_model
from concurrent.futures import ThreadPoolExecutor
import logging
import psutil
import subprocess
from cryptography.fernet import Fernet
import json
from threading import Thread

logging.basicConfig(level=logging.CRITICAL)


class TrainModels:
    """
        Class to train machine learning models and manage their configurations.

        Args:
            models_list (list): List of machine learning models to be trained.
            ai_type (str): Type of artificial intelligence being used.
            api_key (str): API key for accessing external services.
            shell_path (str): Path to the shell environment.
            vn_model_name (str, optional): Name of the VN model.
            Defaults to None.
            db_name (str, optional): Name of the database. Defaults to None.
            user (str, optional): Username for database authentication.
            Defaults to None.
            pwd (str, optional): Password for database authentication.
            Defaults to None.
            host (str, optional): Host address for the database.
            Defaults to "localhost".
            pg_port (int, optional): Port number for the PostgreSQL database.
            Defaults to 5432.
            redis_host (str, optional): Host address for the Redis server.
            Defaults to "localhost".
            redis_port (int, optional): Port number for the Redis server.
            Defaults to 6379.
            redis_db (int, optional): Redis database index. Defaults to 0.

        Raises:
            Exception: If database credentials are not provided.

        Attributes:
            models_list (list): List of machine learning models.
            ai_type (str): Type of artificial intelligence being used.
            api_key (str): API key for accessing external services.
            shell_path (str): Path to the shell environment.
            vn_model_name (str): Name of the VN model.
            db_name (str): Name of the database.
            user (str): Username for database authentication.
            pwd (str): Password for database authentication.
            host (str): Host address for the database.
            pg_port (int): Port number for the PostgreSQL database.
            redis_host (str): Host address for the Redis server.
            redis_port (int): Port number for the Redis server.
            redis_db (int): Redis database index.
            queue (Queue): Redis queue for managing tasks.

        Methods:
            is_rq_worker_running(): Check if RQ worker with scheduler
            is running.
        """

    def __init__(self,
                 models_list,
                 ai_type,
                 api_key,
                 shell_path,
                 vn_model_name=None,
                 db_name=None,
                 user=None,
                 pwd=None,
                 host="localhost",
                 pg_port=5432,
                 redis_host="localhost",
                 redis_port=6379,
                 redis_db=0
                 ):
        self.models_list = models_list
        self.vn_model_name = vn_model_name
        self.api_key = api_key
        self.ai_type = ai_type
        self.db_name = db_name
        self.user = user
        self.pwd = pwd
        self.host = host
        self.pg_port = pg_port
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis_db = redis_db
        self.shell_path = shell_path

        if not self.db_name and not self.user and not self.pwd:
            raise Exception("Please provide db creds")
        self.queue = Queue(
            connection=Redis(port=redis_port, host=redis_host, db=redis_db))

    @classmethod
    def start_rq_workers(cls, shell_path):
        if not cls.is_rq_worker_running():
            command = ["rq", "worker", "--with-scheduler"]
            complete_process = subprocess.run(command, check=True,
                                              cwd=shell_path)
            return complete_process

    def train_models(self):
        """
           Enqueue training tasks for each model in the models list.
           Returns:
               None

           Raises:
               None

           Notes:
               This method generates a secret key for encrypting the training
               task arguments and schedules tasks for training each model in
               the models list.
           """
        secret_key = Fernet.generate_key()
        kwargs = {
            'ai_type': self.ai_type,
            'vn_model_name': self.vn_model_name,
            'api_key': self.api_key,
            'connection': True,
            'dbname': self.db_name,
            'user': self.user,
            'pwd': self.pwd,
            'host': self.host,
            'port': self.pg_port
        }

        for model_name in self.models_list:
            kwargs['model_name'] = model_name
            encrypted_kwargs = self.encrypt_data(json.dumps(kwargs), secret_key)
            self.queue.enqueue(train_model,
                               encrypted_kwargs, secret_key,
                               retry=Retry(max=2))

    def close_queue_connection(self, delay=200):
        """
        Schedule a task to close the queue connection after a specified delay.

        Args:
            delay (int, optional): Number of seconds to wait before closing the
            connection. Defaults to 200.

        Returns:
            None

        Notes:
            This method schedules a task to terminate the RQ worker process
            after a delay.
        """
        self.queue.enqueue_in(timedelta(seconds=self.delay + delay),
                              self.terminate_rq_worker)

    @staticmethod
    def terminate_rq_worker():
        """
           Terminate the RQ worker process if it is running.

           Returns:
               None

           Notes:
               This method finds and terminates the RQ worker process if it is
               currently running.
           """
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == 'rq':
                rq_worker_pid = process.pid
                rq_worker = psutil.Process(rq_worker_pid)
                rq_worker.terminate()

    @staticmethod
    def is_rq_worker_running():
        """
        Check if the RQ worker process is currently running.

        Returns:
            bool: True if the RQ worker process is running, False otherwise.

        Notes:
            This method checks if there is any process with the name 'rq'
            running on the system.
        """
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == 'rq':
                return True
        return False

    @staticmethod
    def encrypt_data(data, key):
        """
        Encrypt the given data using the provided key.

        Args:
            data (str): Data to be encrypted.
            key (bytes): Encryption key.

        Returns:
            bytes: Encrypted data.

        Notes:
            This method uses Fernet symmetric encryption to encrypt the
            provided data.
        """
        cipher = Fernet(key)
        return cipher.encrypt(data.encode())
