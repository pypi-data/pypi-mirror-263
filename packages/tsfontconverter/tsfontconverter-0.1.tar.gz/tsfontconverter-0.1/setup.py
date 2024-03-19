from setuptools import setup, find_packages

setup(
    name='tsfontconverter',
    version='0.1',
    packages=find_packages('tsfontconverter'),
    package_dir={'': 'tsfontconverter'},
    install_requires=[
        # Add your dependencies here
    ],
    author='Thor Arisland',
    description='A Python package for converting fonts',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tcarisland/tsfontconverter',
    license='Apache License 2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)

