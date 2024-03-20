import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fastapi-jwt-auth-compat",
    version="1.0.1",
    author="jeanek",
    author_email="jean.el.khoury08@gmail.com",
    description="A fork of the original fastapi-jwt-auth compatible with Pydantic 2.* versions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jean-ek/fastapi-jwt-authV2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)