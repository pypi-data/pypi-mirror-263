from setuptools import find_packages, setup

with open("trialsconnect/README.md", "r") as f:
    long_description = f.read()

setup(
    name="trialsconnect",
    version="0.0.4",
    description="Easy connecting and querying to clinical trials database from AACT",
    package_dir={"": "trialsconnect"},
    packages=find_packages(where="trialsconnect"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ineelhere/trialsconnect",
    author="ineelhere",
    author_email="",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    install_requires=["psycopg2>=2.9.9", "pandas>=2.0.3"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.0",
)