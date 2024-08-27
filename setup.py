from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="emailservice_core",
    version="0.1",
    author="Victor Gulart",
    author_email="victor.gulart@natoora.com",
    description="Core functionality for sending enabling and sending emails to multiple recipients.",
    long_description=long_description,
    url="https://github.com/Natoora/django-email-service-core",
    packages=find_packages(exclude=["tests*"]),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires=">=3.6",
    install_requires=["Django>=3.2", "djangorestframework>=3"],
)
