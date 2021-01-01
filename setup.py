from setuptools import setup


version = "1.0.2"


def read(filename):
    with open(filename, encoding="utf-8") as file:
        return file.read()


setup(
    name="fish_text_ru",
    version=version,
    description="Simple fish-text.ru python wrapper",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="kiriharu",
    author_email="kiriharu@yandex.ru",
    url="https://github.com/kiriharu/fish_text_ru",
    packages=["fishtext"],
    license="MIT",
    keywords="fish text tests autotext",
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Environment :: Console",
    ],
)
