from setuptools import setup, find_packages

setup(
    name='autossh',
    version='0.0.1.2',
    license='MIT',
    author='Gavin Bao',
    author_email='xingce.bao@gmail.com',
    packages=find_packages(),
    install_requires=[
        'sshtunnel',
    ],
    entry_points={ 
        'console_scripts': [
            'autossh-py=autossh.autossh_py:main',  
        ],
    },
    description='A simple auto reconnect ssh tunnel client',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
