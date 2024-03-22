from setuptools import setup, find_packages
import unittest, test
#from requires import requires as requries
suite = unittest.TestLoader().loadTestsFromModule(test)
unittest.TextTestRunner(verbosity=2).run(suite)
requires = """numpy
Pillow
tqdm""".split("\n")
print(requires)
#with open("requirements.txt") as f:
#    requries = f.read().split("\n")
with open("README.md") as f:
    long_des = f.read()
setup(name="PMG-Maze", description="A library for maze generation", long_description=long_des, long_description_content_type='text/markdown', packages=find_packages(include=["pmg_maze", "pmg_maze.pmg"]), install_requires=requires, version="1.0.0a")
