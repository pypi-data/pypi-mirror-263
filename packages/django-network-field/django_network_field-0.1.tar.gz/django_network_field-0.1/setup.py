from setuptools import setup, find_packages

setup(
    name='django_network_field',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django',
    ],
)
