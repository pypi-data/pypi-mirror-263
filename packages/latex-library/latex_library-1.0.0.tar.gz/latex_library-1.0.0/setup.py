from setuptools import setup, find_packages

setup(
    name='latex_library',
    version='1.0.0',
    packages=find_packages(),
    author='Daniil Plotnikov',
    author_email='dplotnikovon@gmail.com',
    description='HW2 python2024',
    long_description='Nothing',
    long_description_content_type='text/markdown',
    url='https://github.com/OFFdeil/latex_libraryr',
    install_requires=[
        'requests>=2.25.1',
    ],
    python_requires='>=3.9',
)