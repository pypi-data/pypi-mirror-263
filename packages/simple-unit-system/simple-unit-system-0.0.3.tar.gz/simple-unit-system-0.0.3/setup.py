from setuptools import setup

setup(
    name='simple-unit-system',
    version='0.0.3',
    description="A framework for applying physical units and performing unit conversions, for scientific and engineering analyses, based on NIST conversions and constants",
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    install_requires=[
    ],
    package_dir={"": "src"},
    python_requires=">=3, <4",
    project_urls={  # Optional
        "Bug Reports": "https://github.com/jeffcodez/PhysicalUnits/issues",
        "Source": "https://github.com/jeffcodez/PhysicalUnits",
    },
)