from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'A Python library to generate the next permutation for an array.'


# Setting up
setup(
    name="nextPermutation",
    version=VERSION,
    author="Ishita Shokeen",
    author_email="ishitashokeen9@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python','dsa','problem-solving'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
