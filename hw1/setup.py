import setuptools

setuptools.setup(
    name="sastvisualizer",
    version="1.1.2",
    author="OlesiaSub",
    author_email="lesya.sub@mail.ru",
    description="Python course hw1. AST visualizer.",
    packages=['sastvisualizer'],
    url="https://github.com/OlesiaSub/hse-python-2022/tree/master/hw1",
    install_requires=["networkx", "pydot", "numpy", "matplotlib"]
)

