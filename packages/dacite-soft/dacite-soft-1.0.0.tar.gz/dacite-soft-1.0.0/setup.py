from setuptools import setup

setup(
    name="dacite-soft",
    version="1.0.0",
    description="Simple creation of data classes from dictionaries. Not failing on missed fields",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Mikita Kuzniatsou, Konrad Hałas",
    author_email="nikikuzi@gmail.com, halas.konrad@gmail.com",
    url="https://github.com/nikikuzi/dacite-soft",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
    keywords="dataclasses",
    packages=["dacite"],
    package_data={"dacite": ["py.typed"]},
    install_requires=['dataclasses;python_version<"3.7"'],
    extras_require={
        "dev": ["pytest>=5", "pytest-benchmark", "pytest-cov", "coveralls", "black", "mypy", "pylint", "pre-commit"]
    },
)
