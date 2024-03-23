from setuptools import setup
setup(
    name="mkdocs_asyncapi_html_plugin",
    version="0.3.5",
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
    #packages=['mkdocs_asyncapi_html_plugin'],
    py_modules=["mkdocs_asyncapi_html_plugin"],
    install_requires=[],
    entry_points={
        "mkdocs.plugins": [
            "asyncapi_html = mkdocs_asyncapi_html_plugin:AsyncAPIPlugin"
        ]
    },
    python_requires=">=3.7",
)