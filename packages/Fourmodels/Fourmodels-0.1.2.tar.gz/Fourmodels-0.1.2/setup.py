from setuptools import setup, find_packages

setup(
    name='Fourmodels',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'librosa',
        'numpy',
        'keras',
        'scikit-learn',
        'xgboost'
    ],
    author='FourLayer',
    author_email='fourlayerpbl@gmail.com',
    description='A package for comparing four machine learning models',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/FourLayer/FinalCode/',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
