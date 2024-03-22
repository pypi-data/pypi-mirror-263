from setuptools import setup, find_packages

setup(
    name='fagr',
    version='0.1',
    packages=find_packages(),
    author_email='masemennikov@gmail.com',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'farg = farg.fagr:run',
        ],
    },
)
