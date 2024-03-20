from setuptools import setup, find_packages

setup(
    name='dock-cli',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click==8.1.7',
    ],
    entry_points='''
        [console_scripts]
        dock=main:cli
    ''',
)
