from setuptools import setup, find_packages

setup(
    name='fagr',
    version='0.3',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'fagr = fagr.fagr:run',
        ],
    },
    author_email='masemennikov@gmail.com'
)



