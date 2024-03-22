from setuptools import setup, find_packages

setup(
    name='mkdocs-asyncapi-html-plugin',
    version='0.2.1',
    description='generate html file from asyncapi yml file',
    long_description='generate html file from asyncapi yml file',
    long_description_content_type='text/markdown',
    author='Hani',
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'asyncapi-html = mkdocs_asyncapi:Asyncapi'
        ]
    },
    python_requires='>=3.6',
)