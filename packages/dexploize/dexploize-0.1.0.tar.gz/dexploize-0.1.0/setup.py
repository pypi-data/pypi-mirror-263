from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='dexploize',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
      'matplotlib>=3.4.3',
      'numpy>=1.21.0',
      'pandas>=1.3.3',
      'scikit-learn>=0.24.2'
      ],
    entry_points={
        'console_scripts': [
            'DataExploration = DataExploration.__main__:main'
        ]
    },
    author='Christian Garcia',
    author_email='iyaniyan3112003@gmail.com',
    description='dexploize (data exploration) python library use for applying different foundational techniques such as univariate and bivariate analysis.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/iyaniyan11/dexploize.git',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
