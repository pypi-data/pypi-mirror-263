from setuptools import setup, find_packages

setup(
    name="mkdocs_asyncapi_html_plugin",
    version="0.2.3",
    description="mkdocs plugin to generate pages from asyncapi spec files",
    long_description="mkdocs plugin to generate pages from asyncapi spec files",
    long_description_content_type="text/markdown",
    author="hani",
    author_email="hani@regentmarkets.com",
    url="https://github.com/hani-deriv/mkdocs-asyncapi-plugin",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    keywords=["mkdocs", "asyncapi", "plugin", "python"],
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "mkdocs.plugins": [
            "asyncapi_html = mkdocs_asyncapi_html_plugin:AsyncAPIPlugin"
        ]
    },
    python_requires=">=3.7",
)