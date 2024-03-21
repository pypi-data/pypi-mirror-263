from setuptools import setup, find_packages

setup(
    name="data-exporter",
    version="0.1.3",
    author="SokinjoNS",
    author_email="sokinjo.155@gmail.com",
    description="A module for exporting email data to CSV format.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/SokinjoNS/data-exporter",
    packages=find_packages(),
    install_requires=[
        'gmail-message-processor>=0.1.3',
    ],
    project_urls={
        "GitHub": "https://github.com/SokinjoNS/data-exporter",
        "Source": "https://github.com/SokinjoNS/data-exporter"
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
