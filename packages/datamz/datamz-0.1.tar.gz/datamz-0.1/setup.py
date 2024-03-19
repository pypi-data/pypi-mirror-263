from setuptools import setup, find_packages

setup(
    name="datamz",
    version="0.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for generating random user data",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'datamz': ['data/*'],
    },
    install_requires=[
        'setuptools',
    ],
    entry_points={
        'console_scripts': [
            'datamz=datamz.module:main',
        ],
    },
)
