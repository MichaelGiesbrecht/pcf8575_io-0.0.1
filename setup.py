from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Other OS',
    'Topic :: System :: Hardware :: Hardware Drivers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='pcf8574_io',
    version='0.1.1',
    description=' PCF8574 driver to set pin mode, read and write digital signal 3.3v ',
    long_description= open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ahmed9378/pcf8574_io',
    author='Ahmed Omar',
    author_email='ahmed.bm78@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='PCF8574',
    packages=find_packages(),
    install_requires=['smbus2']
)