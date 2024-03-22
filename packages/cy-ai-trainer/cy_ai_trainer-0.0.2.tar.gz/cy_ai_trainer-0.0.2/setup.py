from setuptools import setup, find_packages

setup(
    name='cy_ai_trainer',
    version='0.0.2',
    author='Cybrosys Technologies Pvt. Ltd.',
    description='A Helper tool that helps train the ai model in cyllo',
    long_description=open('README.md').read() + '\n\n' + open(
        'CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/CybroOdooDev/SmartDashboard/tree/cy_package/cy_ai_trainer',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'psycopg2-binary>=2.8.0',
        'vanna==0.0.30',
        'rq==1.16.0',
        'psutil',
        'cryptography>=3.4.8',
        'requests'
    ],
    python_requires='>=3.10',
)
