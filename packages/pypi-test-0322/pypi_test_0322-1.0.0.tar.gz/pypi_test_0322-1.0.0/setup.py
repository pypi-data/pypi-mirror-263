import setuptools

setuptools.setup(
    name="pypi_test_0322",
    version="1.0.0",
    author="suk-6",
    author_email="me@suk.kr",
    description="test",
    url="https://suk.kr",
    packages=setuptools.find_packages(include=["pypi_test_0322", "pypi_test_0322.*"]),
    python_requires=">=3.6",
    license="MIT",
)
