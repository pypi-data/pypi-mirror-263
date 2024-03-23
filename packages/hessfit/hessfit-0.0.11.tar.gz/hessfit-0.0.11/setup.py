from setuptools import setup, find_packages

VERSION = '0.0.11'
DESCRIPTION = 'A package that allows to derive force field.'

setup(
      version=VERSION,
      packages = find_packages(),
      package_data={'hessfit': ['HessFit_harmonic.py', 'build_4Hessfit.py']},
      install_requires=["numpy", "scipy", "pandas"],
      entry_points = {
        'console_scripts': ['hessfit = hessfit.main:main',]
      },
     )

