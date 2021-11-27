from setuptools import setup
import os
with open('requirements.txt', 'r') as f:
      required = f.readlines()
setup(name='icomictest',
      version='0.1',
      description='icomic gui',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='GUI toolkit',
      install_requires= [i.strip() for i in required],
      entry_points={
          'console_scripts': ['icomic=mainwin_v35.py:main'],
      },
      include_package_data=True,
      zip_safe=False)
