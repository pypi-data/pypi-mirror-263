from setuptools import setup, find_packages

setup(
    name="nestconfig",
    version="0.2.0",
    author="Zeyun Zhong",
    author_email="zeyun.zhong@kit.edu",
    description="Type-safe configuration management with support for nested dataclasses",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zeyun-zhong/nestconfig",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=["test", "test.*"]),
    python_requires='>=3.7',
    install_requires=[
        'PyYAML',  # Add PyYAML to the list of required packages
    ],
)
