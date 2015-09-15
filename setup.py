
try:
    from setuptools import setup
except (ImportError):
    from distutils.core import setup

__about__ = {}

setup(
    name="kahuna",
    version="0.1.5",
    author="Ismael de Esteban",
    author_email="ismael.deesteban@gmail.com",
    url="http://kahuna.com/",
    description="Python package for using the Kahuna API",
    long_description=open('README.rst').read(),
    packages=["kahuna"],
    license='BSD License',
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'requests>=1.2',
    ],
)
