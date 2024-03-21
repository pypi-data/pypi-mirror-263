from setuptools import setup, find_packages

setup(
    name='logngo',
    version='1.7.36',
    packages=find_packages(),
    description='Log chains for webserver',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Cong Hoang Tran',
    author_email='trconghoangg@gmail.com',
    url='https://github.com/hoangtc125/logtc',
    install_requires=[
        'requests',
        'contextvars',
        'websocket-client',
        'websockets',
        'python-socketio>=4.0,<5.0',
        'python-engineio>=3.0,<4.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
