from setuptools import setup

__version__ = '0.1'

setup(
      name='overStat',
      version=__version__,

      packages=['overStat'],

      description='Overwatch API Wrapper using SunDwarf/OWAPI',
      url='https://github.com/t04glovern/overStat',
      author='Nathan Glover <t04glovern>',
      license='MIT',
      install_requires=['requests']
  )