from setuptools import setup

setup(
    name='argel1200',
    version='1.0.1',
    packages=['argel1200'],
    url='https://github.com/argel1200/argel1200-python',
    license='MIT',
    author='argel1200',
    author_email='argel@msn.com',
    description='My utility functions',
    install_requires = [
        "click>=7.1.2",
        "dumper>=0.10.2",
        "haggis>=0.9.1"
        ],
    )
