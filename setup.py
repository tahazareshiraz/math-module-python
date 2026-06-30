from setuptools import setup, find_packages

setup(
    name="taha-math-shiraz",
    version="1.0.0",
    description="یک کتابخانه ریاضی شبیه به ماژول math پایتون، نوشته شده توسط طاها از شیراز",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Taha",
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
