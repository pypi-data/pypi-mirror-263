# DEXPLOIZE DATA EXPLORATION PYTHON LIBRARY

Data Exploration is a Python library tailored to simplify and enhance the journey of data analysis tasks. Whether you're diving into datasets, conducting statistical analyses, or visualizing data, dexploize (Data Explorstion) equips you with a comprehensive toolkit to expedite the process and extract valuable insights efficiently.

# FEATURES

Univariate Analysis Visualization
- Entropy Based Binning
- Equal Width Based Binning
- Equal Frequency Based Binning
- Binary Encoding
- Imputation Values

Bivariate Analysis Visualization
1. [NUMERICAL AND NUMERICAL]
- Scatter Plot
- Linear Correlation

2. [CATEGORICAL AND CATEGORICAL]
- Combination Chart
- Stacked Column Chart

3. [CATEGORICAL AND NUMERICAL]
- Line Chart w/ Error Bars

# INSTALLATION
You can install DataExploration with pip and required libraries.

pip install dexploize
pip install matplotlib
pip install numpy
pip install pandas
pip install matplotlib
pip install scikit-learn

# USAGE
Univariate Function Data Preprocessing
- entropy_based(data1, target, bins)
- equal_width(data, bins)
- ewidth_bin(data, bins)
- ewidth_plot(data)
- equal_freq(data, bins)
- efreq_bin(data, bins)
- efreq_plot(data)
- binary_encoding(data, values)
target_encoding(data, encoded)
- impute_values(data)

Bivariate Function Data Visualization
- scatter_plot(data, attr1, attr2)
- linear_corr(data, attr1, attr2)
- stacked_column(data, val1, val2)
- line_chart(data, attr, num)

# IMPORT LIBRARY
::
    
    from DataExploration.univariate import *
    from DataExploration.bivariate import *
    ...

# INFORMATION
Data Exploration is about describing the data by means of statistical and visualization techniques. We explore data in order to bring important aspects of that data into focus for further analysis.