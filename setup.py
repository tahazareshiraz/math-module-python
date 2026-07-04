from pathlib import Path

from setuptools import find_packages, setup


README = Path(__file__).with_name("README.md")

setup(
    name="taha-math-shiraz",
    version="1.1.2",
    description="A pure-Python math utility library.",
    long_description=README.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.10",
)
