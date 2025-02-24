import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "zarinpal-payment",
    version = "0.0.7",
    author = "Meraj Sarab",
    author_email = "srb.meraj@gmail.com",
    description = "a Python package for integrating the ZarinPal payment gateway.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Mrj-Srb/zarinpal-payment-python",
    project_urls = {
        "Author": "https://github.com/Mrj-Srb",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'requests',
        'logging'
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.7"
)