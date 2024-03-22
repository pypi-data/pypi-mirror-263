import setuptools
with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()
    
setuptools.setup(
    name = "eskmo",
    version = "0.0.0",
    author = "eskmo",
    author_email="fatfingererr@gmail.com",
    description="eskmo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ProjectEskmo/eskmo",                                         packages=setuptools.find_packages(),     
    classifiers=[
        "Development Status :: 1 - Planning",
        "Natural Language :: English",
        "Natural Language :: Chinese (Traditional)",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Microsoft :: Windows",
    ],
    platforms=["Windows"],
    python_requires='>=3.9'
    )