from setuptools import setup, find_packages

setup(
    name="gmail-api-auth",
    version="0.1.3",
    author="SokinjoNS",
    author_email="sokinjo.155@gmail.com",
    description="A module for authenticating Gmail API access.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/SokinjoNS/gmail-api-auth",
    packages=find_packages(),
    install_requires=[
        'google-auth',
        'google-auth-oauthlib',
        'google-auth-httplib2',
    ],
    project_urls={
        "GitHub": "https://github.com/SokinjoNS/gmail-api-auth",
        "Source": "https://github.com/SokinjoNS/gmail-api-auth"
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
