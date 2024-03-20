import os

from setuptools import setup


def read(fname):
    """
    Helper to read README
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()


setup(
    name="lcp_upload",
    version="0.0.1",
    description="Upload corpus to LCP",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://gitlab.uzh.ch/LiRI/projects/lcp-upload",
    author="Danny McDonald",
    include_package_data=False,
    zip_safe=True,
    packages=["lcp_upload"],
    scripts=["bin/lcp-upload"],
    author_email="daniel.mcdonald@uzh.ch",
    license="MIT",
    keywords=["corpus", "linguistics", "corpora", "nlp"],
    install_requires=["requests>=2.30.0", "py7zr>=0.20.5", "tqdm>=4.65.0"],
)
