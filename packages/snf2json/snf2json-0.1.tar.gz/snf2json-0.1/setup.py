from setuptools import setup

setup(
    name='snf2json',
    version='0.1',
    packages=['src/snf2json'],
    url='https://github.com/philippesanio/snf2json',
    license='MIT',
    author='Philippe Sanio',
    author_email='philippe.sanio@gmail.com',
    description='A convertion tool for Sniffles objects (SNF) to JSON like objects (SNFJ)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)