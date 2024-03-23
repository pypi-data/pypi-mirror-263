from setuptools import setup, find_packages

setup(
    name='python-state-manager',
    version='0.3.0',
    packages=find_packages(),
    install_requires=[],
    # Additional metadata about your package.
    author='Chinmay Shrivastava',
    author_email='cshrivastava99@gmail.com',
    description='A simple state machine to handle states of programs.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ChinmayShrivastava/pdf-page-annotator',
    license='GPLv3',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
    ],
    entry_points={},
)