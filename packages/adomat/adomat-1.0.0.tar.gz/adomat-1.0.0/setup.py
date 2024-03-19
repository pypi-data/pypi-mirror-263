from setuptools import setup, find_packages

setup(
    name='adomat',
    version='1.0.0',
    packages=find_packages(),
    author='twinsszi',
    author_email='adhm90879@gmail.com',
    description='simple library to get your ip',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
       'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)