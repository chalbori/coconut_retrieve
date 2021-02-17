import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coconut_retrieve", # Replace with your own username
    version="0.0.1",
    author="Sangwon Lee",
    author_email="sw.lee@yonsei.ac.kr",
    description="Coconut retriever",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chalbori/coconut_retrieve",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
