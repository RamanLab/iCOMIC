from setuptools import setup
import os

setup(name='icomic',
      version='0.1',
      description='icomic gui',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='GUI toolkit',
      install_requires=[
          'markdown',
      ],
      entry_points={
          'console_scripts': ['icomic=mainwin_v35.py:main'],
      },
      include_package_data=True,
      zip_safe=False)
      
      with open('requirements.txt') as f:
      required = f.read().splitlines()

      setup(...
      install_requires=required,
      ...)
