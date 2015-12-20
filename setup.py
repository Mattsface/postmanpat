"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call
from postmanpat import __version__
from setuptools import Command, find_packages, setup


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        pass

setup(
    name='postmanpat',
    version=__version__,
    description='A Program to clean up your mail box using IMAP',
    url='https://github.com/Mattsface/postmanpat',
    author='Matthew Spah',
    author_email='spahmatthew@gmail.com',
    license='UNLICENSE',
    classifiers=[
    ],
    keywords='cli',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=['docopt'],
    extras_require={
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points={
        'console_scripts': [
            '',
        ],
    },
    cmdclass={'test': RunTests},
)
