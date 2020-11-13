from setuptools import setup, find_packages

setup(
    name='delim',
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'delim = delim.main:main'
        ]
    },
    url='',
    license='',
    author='Allie Fitter',
    author_email='afitter@cellcontrol.com',
    description='CLI that converts the case of strings.',
)
