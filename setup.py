from setuptools import setup

setup(name='dm_requests',
      version='0.1.0',
      description="Device Magic's API Wrapper",
      url='',
      author='Anthony Seliga',
      author_email='anthony.seliga@gmail.com',
      license='MIT',
      packages=['dm_requests'],
      install_requires=[
          'requests',
          'vcrpy',
          'pytest',
      ],
      zip_safe=False)