from setuptools import setup, find_packages

setup(
    name='streak',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'tinydb'
    ],
    entry_points='''
        [console_scripts]
        yourscript=streak.streak:cli
    ''',
)