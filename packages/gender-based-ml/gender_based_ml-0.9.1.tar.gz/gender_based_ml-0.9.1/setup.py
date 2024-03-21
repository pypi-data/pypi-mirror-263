import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="gender_based_ml",
    version="0.9.1",
    author="Shruthipriya",
    author_email="priya@shavik.ai",
    description="ML based project to determine the gender of a speaker in an audio file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
      package_data={
        "gender_based_ml": ["*.*"],
    },
    include_package_data=True,
    install_requires=["tensorflow>=2.7.0", "keras>=2.7.0", "torch>=0.8.1","gitpython>=3.1.30"],
)
