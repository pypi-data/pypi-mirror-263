import setuptools
import sys

sys.path.append('src')
from b3o_fedlearn.client_setup import CustomInstall


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="b3o-fedlearn",
    version="0.0.10",
    author="skswjdekdud",
    author_email="skswjdekdud1103@gmail.com",
    description="a project for federated learning using AWS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ACS-High-School",
    project_urls={
        "Bug Tracker": "https://github.com/ACS-High-School/ML/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    cmdclass={
        'install': CustomInstall,
    },
    python_requires=">=3.8",
)
