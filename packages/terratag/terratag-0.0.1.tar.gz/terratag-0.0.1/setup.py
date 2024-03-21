from setuptools import setup, find_packages

setup(
   name='terratag',
   version='0.0.1',
   packages=find_packages(),
   install_requires=[
      'click',
   ],
   entry_points='''
      [console_scripts]
      tf_wrapper=tf_wrapper.main:main
      ''',
)
