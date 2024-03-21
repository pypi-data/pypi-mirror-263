import setuptools

setuptools.setup(
    name = "NOMTrainer",
    version = "1.1.8",
    author = "CSSA",
    author_email="ladder.cssa@gmail.com",
    description="A Trainer for Neural Object Model (NOM) in Tensorflow.",
    long_description="long_description",
    long_description_content_type="text/markdown",
    url="https://github.com/LadderCSSA/NOMTrainer",            
    packages=setuptools.find_packages(),     
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9'
)
