from setuptools import setup, find_packages

setup(
    name='PyEnhance',
    version='0.1.3.1',
    packages=['PyEnhance'],
    package_data={
        'PyEnhance': ['*.py'],
    },
    install_requires=[
        "colorama == 0.4.6",
        "cursor == 1.3.5",
        "Requests == 2.31.0"
    ],
    author='Not A Bird',
    description='A collection of essential scripts for any python project.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/BirdsAreFlyingCameras/PyEnhance',
    include_package_data=True
)
