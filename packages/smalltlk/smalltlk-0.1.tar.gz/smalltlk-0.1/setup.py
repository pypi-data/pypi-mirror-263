from setuptools import setup, find_packages

setup(
    name='smalltlk',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add dependencies here
        # e.g. 'numpy>=1.11.1'
    ],
    entry_points={
        "console_scripts":[
            "smalltlk-hello = smalltlk_hello:hello",
        ],
    },
)