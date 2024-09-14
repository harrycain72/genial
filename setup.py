from setuptools import setup, find_packages

setup(
    name="connection_mngr",               # The name of your package
    version="0.1.0",                        # The initial release version
    author="roland",                     # Your name or the organization
    author_email="your.email@example.com",  # Your contact email
    description="Manages connections to different large language models",  # Short description
    long_description=open('README.md').read(),  # A detailed description (from README.md)
    long_description_content_type='text/markdown',
    url="https://github.com/harrycain72/pypi",  # URL to your repository
    packages=find_packages(),               # Automatically find package directories
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',                # Minimum Python version required
    install_requires=[                      # Dependencies (optional)
        "loguru",
        "langchain"
    ],
)