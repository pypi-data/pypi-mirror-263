from setuptools import setup, find_packages

setup(
    name="gmail-label-manager",
    version="0.1.3",
    author="SokinjoNS",
    author_email="sokinjo.155@gmail.com",
    description="A module for managing Gmail labels.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # Specify the format of the long_description
    url="https://github.com/SokinjoNS/gmail-label-manager",
    packages=find_packages(),
    install_requires=[
        'gmail-api-auth>=0.1.3',
    ],
    project_urls={
        "GitHub": "https://github.com/SokinjoNS/gmail-label-manager",
        "Source": "https://github.com/SokinjoNS/gmail-label-manager"
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
