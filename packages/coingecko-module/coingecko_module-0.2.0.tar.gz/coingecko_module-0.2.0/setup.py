from setuptools import setup, find_packages

setup(
    name='coingecko_module',
    version='0.2.0',
    author='Your Name',
    author_email='arghyazzz@gmail.com',
    description='A Python wrapper for the CoinGecko API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/amukherjee1991/coingecko_module',
    packages=find_packages(),
    install_requires=[
        'pandas','requests'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
   
    ],
    keywords='coingecko cryptocurrency api wrapper',  # Optional
)
