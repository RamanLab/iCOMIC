from setuptools import setup
import os
# with open('requirements.txt') as f:
#      required = f.read().splitlines()
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
      # install_requires= required,
      entry_points={
          'console_scripts': ['icomic=icomic.mainwin_v35.py:main'],
      },
      include_package_data=True,
      zip_safe=False)
    
    
