from setuptools import setup


setup(
    name='salure_helpers_elastic',
    version='1.1.1',
    description='elastic wrapper from Salure',
    long_description='elastic wrapper from Salure',
    author='D&A Salure',
    author_email='support@salureconnnect.com',
    packages=["salure_helpers.elastic"],
    license='Salure License',
    install_requires=[
        'requests>=2,<=3',
        'paramiko>=2,<=3'
    ],
    zip_safe=False,
)
