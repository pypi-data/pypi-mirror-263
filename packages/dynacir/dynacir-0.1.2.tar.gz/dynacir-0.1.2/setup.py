from setuptools import setup, find_packages

found_packages = find_packages()
print("Found packages:", found_packages)

setup(
    name='dynacir',
    version='0.1.2',
    packages=find_packages(),
)
