from setuptools import setup, find_packages

setup(
    name="camera-ui-python-types",
    version="0.1.2",
    description="camera.ui python types",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="seydx",
    author_email="dev@seydx.com",
    packages=find_packages(),
    python_requires=">=3.9",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
