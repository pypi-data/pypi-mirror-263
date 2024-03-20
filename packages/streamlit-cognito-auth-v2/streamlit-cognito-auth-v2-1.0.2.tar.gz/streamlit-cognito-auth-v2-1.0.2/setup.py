from setuptools import setup, find_packages

setup(
    name="streamlit-cognito-auth-v2",
    version="1.0.2",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "boto3 >= 1.26.52",
        "pycognito >= 2022.12.0",
        "pydantic < 2.0.0",
        "requests >= 2.31.0",
        "streamlit >= 1.27.0",
        "extra_streamlit_components >= 0.1.56",
    ],
    author="Jared Backofen",
    author_email="backofen.jared@gmail.com",
    description="A Streamlit component for authenticating users with AWS Cognito",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jbackofe/streamlit-cognito-auth.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
