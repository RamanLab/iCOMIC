from setuptools import setup

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
          'console_scripts': ['icomic=icomic_v0.py:main'],
      },
      include_package_data=True,
      zip_safe=False)
