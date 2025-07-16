from setuptools import setup, find_packages

setup(
    name="bedrockprotopy",
    version="0.0.1",
    author="Deniz1111212(elitrycraft)",
    author_email="elitrycraft@outlook.com",
    description="Minecraft bedrock edition protocol library written in python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/elitrycraft/bedrockprotopy",
    license="MIT",
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent'
    ],
    python_requires=">=3.7",
)
