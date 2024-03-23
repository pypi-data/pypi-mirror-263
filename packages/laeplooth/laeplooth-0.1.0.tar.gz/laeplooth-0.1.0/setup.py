from setuptools import find_packages, setup

setup(
    name='laeplooth',
    packages=find_packages(include=['laeplooth']),
    version='0.1.0',
    description='Translator for loo language',
    author='most.warong',
    install_requires=[
       'Thaispoon==0.0.2'
    ],
    entry_points={
        'console_scripts': [
            'laeplooth = laeplooth:loo'
        ]
    },
)
