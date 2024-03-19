from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.4'
DESCRIPTION = 'Chroma Palette - Text Styling Library'

# Setting up
setup(
    name="chroma_palette",
    version=VERSION,
    author="Vinay Kumar (vk_billava)",
    author_email="<vinaykumarbillava@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open("READMEPYPI.md").read(),
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'terminal', 'color', 'palette', 'color palette', 'termina palette', 'terminal', 'chroma', 'chroma palette'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)