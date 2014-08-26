from setuptools import setup

setup(
    packages=['nutella'],
    name = 'nutella',
    version = '0.0.1',
    author='Emre Yilmaz',
    author_email='mail@emreyilmaz.me',
    url='https://github.com/emre/nutella.py',
    entry_points={
        'console_scripts': [
            'nutella = nutella.nutella:main',
        ],
    },
    install_requires=[
        'requests',
    ],
)