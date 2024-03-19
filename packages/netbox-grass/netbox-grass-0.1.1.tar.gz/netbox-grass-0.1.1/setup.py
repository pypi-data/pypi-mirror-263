from setuptools import find_packages, setup

setup(
    name='netbox-grass',
    version='0.1.1',
    description='NetBox plugin that backs up the configuration of network devices.',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)