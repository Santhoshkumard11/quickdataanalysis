import setuptools
from pathlib import Path

setuptools.setup(
    name="quickdataanalysis",
    version="0.0.6",
    description=('Kick start your data analysis with these functions'),
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    license="MIT",
    maintainer="Santhoshkumard11",
    author='Santhoshkumard11',
    url='https://github.com/Santhoshkumard11/quickdataanalysis',
    install_requires=[
        ' pandas>=1.0.1',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ]
)