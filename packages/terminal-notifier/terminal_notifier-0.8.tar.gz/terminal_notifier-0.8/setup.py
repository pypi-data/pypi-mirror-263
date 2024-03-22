from setuptools import setup, find_packages

# import readme file
with open("README.md", "r") as f:
    description = f.read()


setup(
    description="A package for notifying users about command execution in the terminal",
    name="terminal_notifier",  # Replace with your package name
    version="0.8",  # Replace with your package version
    author="Anish Tipnis",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "plyer",
        "playsound"
    ],
    long_description=description,
    long_description_content_type="text/markdown",

    include_package_data=True,  # Include package data specified by MANIFEST.in
    package_data={
        "": ["*.mp3"],  # Include all mp3 files in the package
    }
)
