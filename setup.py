from setuptools import setup, find_packages

setup(
    name="play_store_api",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "flask",
        "flask-sqlalchemy",
        "pymysql",
        "pyyaml",
        "cryptography",
        "pytest",
    ],
)
