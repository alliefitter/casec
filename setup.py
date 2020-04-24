from setuptools import setup, find_packages

setup(
    name='casc',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'casec = casec.main:main'
        ]
    },
    url='',
    license='',
    author='Allie Fitter',
    author_email='afitter@cellcontrol.com',
    description='CLI that converts the case of strings.',
)
