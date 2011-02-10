from setuptools import setup

setup(
    name="testing_metaclasses",
    version="dev",
    description="Examples Testing metaclasses",
    author="Matthew J. Morrison",
    author_email="mattj.morrison@gmail.com",
    package_dir={'':'src'},
    #packages=('src',),
    install_requires = (
        'mock',
        'django-unittest-depth',
    ),
)
