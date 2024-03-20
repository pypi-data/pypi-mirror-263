from setuptools import setup, find_packages

setup(
    name="dt_extra_sdk",
    version="0.0.4",
    author="Datatower.ai",
    author_email="",
    description="Datatower web server extra plugin sdk",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=["aiohttp", "pycryptodome", "crypto"],
)
