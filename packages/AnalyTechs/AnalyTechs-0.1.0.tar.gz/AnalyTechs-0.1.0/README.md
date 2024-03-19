# DATA ANALYSIS PYTHON LIBRARY

DataAnalysis is a Python library tailored to simplify and enhance the journey of data analysis tasks. Whether you're diving into datasets, conducting statistical analyses, or visualizing data, DataAnalysis equips you with a comprehensive toolkit to expedite the process and extract valuable insights efficiently.

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

Multivariate Analysis Visualization
- Principal Component Analysis (PCA)

# INSTALLATION
You can install DataAnalysis with pip and required libraries.

pip install DataAnalysis
pip install matplotlib
pip install numpy
pip install pandas
pip install matplotlib
pip install scikit-learn

# USAGE
Univariate
- entr_plot(data, bin_name, numval, catval)
- equal_width(data, bins)
- ewidth_plot(data)
- equal_freq(data, bins)
- efreq_plot(data)
- binary_encoding(data, values)
- impute_values(data)

Bivariate
- scatter_plot(data, attr1, attr2)
- linear_corr(data, attr1, attr2)
- stacked_column(data, val1, val2)
- line_chart(data, cat, num)