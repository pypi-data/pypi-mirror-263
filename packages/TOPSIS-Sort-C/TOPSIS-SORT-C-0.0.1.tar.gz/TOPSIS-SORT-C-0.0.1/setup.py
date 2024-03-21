from setuptools import setup

with open('README.md', 'r') as arq:
    readme = arq.read()

setup(name='TOPSIS-SORT-C',
    version='0.0.1',
    license='MIT License',
    author='Giovanna Machado',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='giovannamachhado@gmail.com',
    keywords='topsis sort c',
    description=u'algoritmo topsis-sort-c',
    packages=['TOPSIS-Sort-C'],
    install_requires=['numpy'],)