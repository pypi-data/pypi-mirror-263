from setuptools import setup, find_packages

setup(
    name="gmail-message-processor",
    version="0.1.3",
    author="SokinjoNS",
    author_email="sokinjo.155@gmail.com",
    description="A module for processing Gmail messages.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/SokinjoNS/gmail-message-processor",
    packages=find_packages(),
    install_requires=[
        'gmail-api-auth>=0.1.3',
        'gmail-label-manager>=0.1.3',
    ],
    project_urls={
        "GitHub": "https://github.com/SokinjoNS/gmail-message-processor",
        "Source": "https://github.com/SokinjoNS/gmail-message-processor"
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
