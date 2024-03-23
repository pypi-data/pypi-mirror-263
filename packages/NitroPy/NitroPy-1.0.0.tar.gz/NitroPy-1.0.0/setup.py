from setuptools import setup, find_packages

setup(
    name='NitroPy',  
    version='1.0.0',
    author='Malakai',
    author_email='your.email@example.com',
    description='A package for interacting with Nitrotype racers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
#    url='https://github.com/yourusername/nitrotype-package',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'cloudscraper', 
        'beautifulsoup4',
    ],
)
