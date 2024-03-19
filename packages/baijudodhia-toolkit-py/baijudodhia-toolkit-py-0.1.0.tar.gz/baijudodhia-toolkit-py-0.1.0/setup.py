from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="baijudodhia-toolkit-py",
    version="0.1.0",
    author="Baiju Dodhia",
    description="A Simple to Integrate Python Rule Engine based on JSON Configuration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/baijudodhia/toolkit-py",
    packages=find_packages(),
    install_requires=[
        "certifi==2024.2.2",
        "charset-normalizer==3.3.2",
        "colorama==0.4.6",
        "exceptiongroup==1.2.0",
        "idna==3.6",
        "iniconfig==2.0.0",
        "jsonpath-ng==1.6.1",
        "packaging==24.0",
        "pluggy==1.4.0",
        "ply==3.11",
        "pytest==8.1.1",
        "requests==2.31.0",
        "tomli==2.0.1",
        "urllib3==2.2.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
