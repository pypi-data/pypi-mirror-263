import setuptools
# # 若Discription.md中有中文 須加上 encoding="utf-8"
# with open("Discription.md", "r",encoding="utf-8") as f:
#     long_description = f.read()
    
setuptools.setup(
    name = "CSSA_TEST",
    version = "0.1.1",
    author = "CSSA",
    author_email="",
    description="cut the verdict into different part",
    long_description="long_description",
    long_description_content_type="text/markdown",
    url="https://github.com/",            
    packages=setuptools.find_packages(),     
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
    )