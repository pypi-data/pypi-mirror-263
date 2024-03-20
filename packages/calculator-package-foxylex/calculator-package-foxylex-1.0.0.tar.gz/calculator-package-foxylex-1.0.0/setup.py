from setuptools import setup, find_packages


setup(
    name='calculator-package-foxylex',
    version='1.0.0',
    packages=find_packages(),
    author='Laura Aleksiune',
    author_email='lau.kanapienyte@gmail.com',
    description='A simple calculator package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/foxylex/calculator_package_foxylex',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
