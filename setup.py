from distutils.core import setup

setup(
    # Application name:
    name="MyApplication",
    
    # Version number (initial):
    version="0.1.0",
    
    # Application author details:
    author="Casey Stadick",
    author_email="name@addr.ess",
    
    # Packages
    packages=["flaskapp"],
    
    # Include additional files into the package
    include_package_data=True,
    
    #
    # license="LICENSE.txt",
    description="lipsum lorem",
    
    # long_description=open("README.txt").read(),
    
    # Dependent packages (distributions)
    install_requires=[
        "flask",
        "pydoc",
        "time",
        "jinja2",
        "uuid",
        "json",
        "os"
    ],
)