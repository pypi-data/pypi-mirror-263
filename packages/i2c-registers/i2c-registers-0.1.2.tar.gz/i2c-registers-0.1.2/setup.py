from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="i2c-registers",
    version="0.1.2",
    description="Python wrapper library around the common I2C controller register pattern.",
    long_description=long_description,
    long_description_content_type="text/markdown; charset=UTF-8; variant=GFM",
    url="https://github.com/tsessebe/i2c-register-module",
    author="Francois de Wet",
    author_email="francois@recotrust.co.za",
    license="MIT",

    # List of: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # Project maturity
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",

        # Intended audience
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",

        "Programming Language :: Python :: 3",
    ],

    keywords="library i2c registers",

    packages=find_packages(exclude=["contrib", "docs", "tests"]),

    install_requires=[],
    package_data={},
    data_files=[
        ("", ["README.md"])
    ],
    entry_points={}
)
