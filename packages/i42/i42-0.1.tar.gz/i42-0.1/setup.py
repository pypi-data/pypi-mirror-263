from setuptools import setup, find_packages

setup(
    name='i42',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Any dependencies you have can be listed here, for example:
        # 'click',
    ],
    entry_points='''
        [console_scripts]
        i42=i42.main:main
    ''',
)