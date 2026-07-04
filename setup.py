from setuptools import find_packages, setup


setup(
    name="taha-math-shiraz",
    version="1.1.0",
    description="A pure-Python math utility library.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[],
)

