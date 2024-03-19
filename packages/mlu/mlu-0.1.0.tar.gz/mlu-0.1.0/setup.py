from setuptools import setup, find_packages

setup(
    name='mlu',
    version='0.1.0',
    author='David Condrey',
    author_email='david@protonmail.com',
    description='A comprehensive Python machine learning utility application designed to simplify and enhance the machine learning workflow.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/DavidCondrey/mlu',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'flask',
        'joblib',
        'scikit-learn',
        'qiskit',
        'torch',
        'torch_xla',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)