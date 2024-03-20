"""
py setup.py sdist
twine upload dist/expressmoney-14.0.1.tar.gz
"""
import setuptools

setuptools.setup(
    name='expressmoney',
    packages=setuptools.find_packages(),
    version='14.0.1',
    description='SDK ExpressMoney',
    author='Development team',
    author_email='dev@expressmoney.com',
    install_requires=(),
    python_requires='>=3.7',
)
