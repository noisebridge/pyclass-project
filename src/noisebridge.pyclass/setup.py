from setuptools import setup, find_packages

setup(
    name = "noisebridge.pyclass",
    version = "1.0",
    url = 'http://github.com/jacobian/noisebridge.pyclass',
    license = 'BSD',
    description = "A short URL (rev=canonical) handler for Django apps.",

    packages = find_packages(exclude=['ez_setup']),
    namespace_packages = ['noisebridge'],
    include_package_data=True,
    install_requires = ['setuptools'],

)
