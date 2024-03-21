from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="star_dresden_gs_lib",  # Required
    version="0.1.2",  # Required
    description="A Library for creating a Groundstation using PyQt6",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown", 
    url="https://www.star-dresden.de",  # Optional, Gitlab adress if open source
    author="STAR Dresden e.V.",  # Optional
    author_email="info@star-dresden.de",  # Optional
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        "Development Status :: 1 - Planning",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Framework :: IDLE",
        "Framework :: PyQt :: 6"

        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="PyQt6, PyQt, star-dresden, rover, gui",  # Optional
    package_dir={"": "src"},  # Optional

    packages=find_packages(where="src"),  # Required
    python_requires=">=3.10, <4",
    install_requires=[
        "PyQt6"
        ],  # Optional
    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    
    #extras_require={  # Optional
    #    "dev": ["check-manifest"],
    #    "test": ["coverage"],
    #},

    # Entry points. The following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    #entry_points={  # Optional
    #    "console_scripts": [
    #        "sample=sample:main",
    #   ],
    #},
    #project_urls={ # i.e. BugReports, Source, Funding
    #    "Funding": "https://donate.pypi.org",
    #    "Say Thanks!": "http://saythanks.io/to/example",
    #    "Source": "https://github.com/pypa/sampleproject/",
    #},
)
