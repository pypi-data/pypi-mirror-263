from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='dhapackage',
    version='0.1',
    description='Testing installation of Package',
    author='auth',
    author_email='dharunpandian.itss@gmail.com',
    home_page='https://upload.pypi.org/legacy/',
    license='MIT',
    packages=['dhapackage'],
    zip_safe=False
)
