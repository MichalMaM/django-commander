from setuptools import setup, find_packages
import commander

install_requires = [
    'setuptools>=0.6b1',
    'Django>=1.3,<1.5',
    'south>=0.7',
]

tests_require = [
    'nose',
    'coverage',
]

long_description = open('README.rst').read()

setup(
    name='Django-commander',
    version=commander.__versionstr__,
    description='Application for management commands executables from admin based on Django framework',
    long_description=long_description,
    author='MichalMaM',
    author_email='MichalMaM@centrum.cz',
    license='BSD',
    url='https://github.com/MichalMaM/django-commander.git',

    packages=find_packages(
        where='.',
        exclude=('doc', 'tests',)
    ),

    include_package_data=True,

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=install_requires,

    test_suite='tests.run_tests.run_all',
    tests_require=tests_require,
)
