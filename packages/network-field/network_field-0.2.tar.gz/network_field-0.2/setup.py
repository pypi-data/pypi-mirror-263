from setuptools import setup, find_packages

setup(
    name='network_field',
    version='0.2',
    packages=find_packages(),
    package_data={
        '': ['network_field.py'],
    },
    include_package_data=True,
    install_requires=[
        'Django',
    ],
)
