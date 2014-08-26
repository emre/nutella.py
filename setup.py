from setuptools import setup

setup(
    name = 'nutella',
    version = '0.0.1',
    author='Emre Yilmaz',
    author_email='mail@emreyilmaz.me',
    url='https://github.com/emre/nutella.py',
    entry_points={
        'console_scripts': [
            'nutella = nutella:main',
        ],
    },
)