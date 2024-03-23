from setuptools import setup, find_packages

setup(
    name="twaxs",
    version="2.0.0",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
    'h5py',
    'matplotlib',
    'ipywidgets',
    'IPython',
    'plotly',
    'numpy',
    'pandas',
    'scipy',
    'python-dateutil',
    'openpyxl',
    'ipykernel',
    'pathlib'
    ],
)
