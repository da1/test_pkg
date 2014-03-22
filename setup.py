from setuptools import setup, find_packages

with open("README.txt") as f:
    readme = f.read()

setup(
    name="hoge.fuga",
    packages=['hoge.fuga'],
    version="0.1",
    author="da1",
    author_email="dyamada1988@gmail.com",
    description="test",
    classifiers=[],
    long_description=readme,
    license='MIT',
    url='https://github.com/da1',
)
