from setuptools import setup, find_packages 

setup(
    name='exocanoe',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description="Comprehensive Atmosphere N' Ocean Engine",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Cheng Li',
    author_email='chengcli@umich.edu',
    url='https://github.com/chengcli/canoe',
    install_requires=[
        # List your package dependencies here
        # 'numpy',
        # 'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

