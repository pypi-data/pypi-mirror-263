from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r" , encoding="utf-8") as f:
    long_description = f.read()
    setup(
        name='httprunner_lite',
        version='0.0.5',
        description='This is an HTTP interface automation testing engine from httprunner4, mainly provided for platform use.',
        long_description=long_description,
        author='phailin',
        author_email='phailin791@hotmail.com',
        url='https://github.com/phailin/httprunner_lite',
        license='MIT',
        packages=find_packages(),
        platforms=["all"],
        classifiers=[
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Natural Language :: Chinese (Simplified)',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Topic :: Software Development :: Libraries'
        ],
        install_requires=[
            'requests',
            'loguru',
            'jmespath',
            'filetype',
            'requests_toolbelt',
            'pydantic>2',
        ]
    )