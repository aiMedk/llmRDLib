from setuptools import setup, find_packages

setup(
    name='llmRDLib',
    version='0.1.0',
    description='A Python library for interacting with the Ollama chat API.',
    author='Mohamed EL FAKIR',
    author_email='mohamed.el-fakir@talan.com',
    url='',
    packages=['llmRDLib'],
    install_requires=['ollama'],  
    entry_points={
        'console_scripts': [
            'llmRDLib=llmRDLib.cmd_line:main',  
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
