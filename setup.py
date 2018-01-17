from setuptools import setup

setup(name='dm_requests',
      version='0.1.0',
      description="Library for using the Device Magic's API",
      url='',
      author='Anthony Seliga',
      author_email='anthony.seliga@gmail.com',
      license='MIT',
      packages=['dm_requests'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)