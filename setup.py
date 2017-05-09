
from setuptools import setup

setup(
    name='movie_app',
    version='0.0.1',
    python = 'python 3.6'
    packages=[
        'movieapp',
        ],
    install_requires=[
        "requests",
        "psycopg2",
        "django",
        "django-crispy-forms"
        "Pillow"
        "beautifulsoup4"
        ],

    author='Momo Johnson',

    packages=find_packages(exclude=['tests*']),

    long_description=open('README.md').read(),

)
