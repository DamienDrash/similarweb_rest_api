from setuptools import setup

setup(
    name='similarweb_rest_api',
    version='1.0',
    description='A library to simplify the access to the REST API of similarweb.',
    author='Damien Frigewski',
    packages=['similarweb_rest_api'],
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license='MIT',
    author_email='dfrigewski@gmail.com',
)
