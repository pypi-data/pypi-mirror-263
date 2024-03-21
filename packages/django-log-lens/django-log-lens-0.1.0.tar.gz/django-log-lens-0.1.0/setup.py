import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-log-lens",
    version="0.1.0",
    author="Martin Broede",
    author_email="martin.broede@gmail.com",
    description="A lightweight Django app for viewing and managing log data conveniently.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/martinbroede/django-log-lens",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.9',
)