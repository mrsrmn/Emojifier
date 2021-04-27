import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="emojifier",
    version="1.1.1",
    author="MakufonSkifto",
    description="Emojifier is a module for emojifying text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Issue tracker": "https://github.com/MakufonSkifto/Emojifier/issues",
        "Source": "https://github.com/MakufonSkifto/Emojifier"
    },
    packages=setuptools.find_packages(),
    install_requires=["emoji"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    keywords="emoji emojifyer emojipasta pasta reddit emojis emojify emojifier",
    python_requires='>=3.5',
)
