import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="convert_youtube_ttml_to_srt",
    install_requires=[
    ],
    version="1.0.0",
    description="convert youtube's ttml subtitle to rst format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leftatrium2/convert_youtube_ttml_to_srt",
    author="leftatrium",
    author_email="leftatrium2@gmail.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
