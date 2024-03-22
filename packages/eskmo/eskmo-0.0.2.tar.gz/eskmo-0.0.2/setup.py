from setuptools import find_packages, setup

setuptools_kwargs = {
    "install_requires": [
            "requirements.txt"
            ],
    "zip_safe": False,
}

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()
    
setup(
    name = "eskmo",
    version = "0.0.2",
    packages=find_packages(),
    long_description_content_type="text/markdown",
    long_description=long_description,
    author = "eskmo",
    author_email="fatfingererr@gmail.com",
    description="eskmo",
    url="https://github.com/ProjectEskmo/eskmo",                                         
    keywords=[],    
    classifiers=[
        "Development Status :: 1 - Planning",
        "Natural Language :: English",
        "Natural Language :: Chinese (Traditional)",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: Microsoft :: Windows",
    ],
    platforms=["Windows"],
    python_requires=">=3.9",
    **setuptools_kwargs
    )