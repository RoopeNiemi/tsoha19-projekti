from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='Keskustelufoorumi',
      version='1.0',
      description='Tietokantasovellus kurssille keväällä 2019 tehty ohjelma.',
      author='Roope Niemi',
      packages=find_packages(),
      install_requires=(required),
      scripts=["run.py"],
      package_data={
          '':['*.html']
      }
     )