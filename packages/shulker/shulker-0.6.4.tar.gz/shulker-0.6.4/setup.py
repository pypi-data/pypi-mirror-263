from setuptools import find_packages, setup

# install requires should pull the list from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='shulker',
    version='0.6.4',
    author='PortalHubYT',
    author_email='portalhub.business@gmail.com',
    description='A minecraft interface using RCON',
    url='https://github.com/PortalHubYT/shulker',
    packages=find_packages(),
    package_data={
        'shulker': ['functions/*.json', 'components/*.json', 'server/*.json', 'functions/mc_data/*.json', "metadata/data/*.json"]
    },
    # install requires should pull the list from requirements.txt
    install_requires=requirements
)
