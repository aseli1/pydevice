import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dm_requests',
    version='0.1.0',
    description="Device Magic API Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/aseli1/dm_requests',
    author='Anthony Seliga',
    author_email='anthony.seliga@gmail.com',
    license='MIT',
    packages=['dm_requests'],
    python_requires='>3.0'
    install_requires=[
        'requests',
        'vcrpy',
        'pytest'
    ],
    zip_safe=False)