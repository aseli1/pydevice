import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pydevice',
    version='0.2.4',
    description="Device Magic API Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/aseli1/pydevice',
    author='Anthony Seliga',
    author_email='anthony.seliga@gmail.com',
    license='MIT',
    packages=['pydevice'],
    python_requires='>3.0',
    install_requires=[
        'requests',
        'vcrpy',
        'pytest'
    ],
    zip_safe=False)
