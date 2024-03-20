from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    # name='abcLR',
    name='abcLR',
    version='1.0.0',
    description='ABC-LR is a classification method that combines the Artificial Bee Colony algorithm with a logistic regression classification model.',
    # py_modules=['abcLR'],
    # package_dir={'': 'src'},
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kagandedeturk/ABC-LR",
    author="Bilge Kagan Dedeturk",
    author_email="kagandedeturk@gmail.com; bilgededeturk@erciyes.edu.tr",
)
