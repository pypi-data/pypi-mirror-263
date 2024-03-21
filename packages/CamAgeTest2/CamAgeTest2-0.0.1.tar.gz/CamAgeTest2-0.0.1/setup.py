from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Package for performing image segmentation'

# Setting up
setup(
    name="CamAgeTest2",
    version=VERSION,
    author="Sarthak Tyagi",
    author_email="<sarthak20540@iiitd.ac.in>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['keras', 'pandas', 'scipy', 'tensorflow'],
    keywords=['python', 'image', 'segmentation', 'image segmentation'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)