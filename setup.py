from setuptools import setup, find_packages

DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'My first Python package description'

install_requires = [
    "numpy>=1.19",  
    "pandas>1.0.3",
    'matplotlib',
    'seaborn',
    'scikit-learn',
    'fastapi',
    'uvicorn',
    'joblib',
    'streamlit',
]

setup(
    name='my_data_science_lib', 
    version='0.1',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(where='src'),  
    package_dir={'': 'src'},  
    python_requires=">=3.9",
    install_requires=install_requires
    # test_suite='tests',
)