from setuptools import setup, find_packages

setup(
    name="epub_simplifier",
    setuptools_git_versioning={
        "enabled": True,
    },
    setup_requires=["setuptools-git-versioning<2"],
    packages=find_packages(),
    install_requires=[
        "EbookLib>=0.17.1",
        "openai>=0.2.6",
        "progress>=1.6",
        "markdownify>=0.11.6",
        "markdown2>=2.4.13",
        "tenacity>=8.2.3",
        "tiktoken>=0.1.1",
    ],
    extras_require={
        "dev": [
            "black",
            "flake8-pyproject",
            "flake8",
            "pytest",
            "pytest-asyncio",
            "pytest-mock",
            "pytest-cov",
            "build",
            "twine",
        ]
    },
    entry_points={
        "console_scripts": [
            "epub-simplify=epub_simplifier.simplifier:main",
        ],
    },
    author="Anatolii Bubenkov",
    author_email="bubenkoff@gmail.com",
    description="A command-line tool to simplify language in EPUB books",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords="epub language simplification tool",
    url="https://github.com/bubenkoff/epub-simplifier",
)
