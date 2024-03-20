import os

from setuptools import setup


def read(fname):
    """
    Helper to read README
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()


setup(
    name="corpert",
    version="0.0.1",  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT
    description="Conversion between corpus linguistic formats",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="",
    author="Teodora Vukovic",
    include_package_data=False,
    zip_safe=True,
    packages=["corpert","corpert.parsers"],
    scripts=["bin/corpert"],
    author_email="teodora.vukovic2@uzh.ch",
    license="MIT",
    keywords=["corpus", "linguistics", "corpora", "conll", "tei", "vert"],
    install_requires=["lxml>=4.7.1", "lupa>=1.13"],
)
