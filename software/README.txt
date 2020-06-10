
Instructions for running the following codes:
=================================================================================
Note: These files are developed and tested in Python3.6.

The following packages are required to run the codes:
-jupyter noteboook
-numpy
-json
-re
-matplotlib
-itertools
-pandas
-scipy
-gekko
-IPython
-datetime

These packages can be installed by issuing the following command "pip install name_of_the_package"
=================================================================================
"estimation_prediction_for_RiskScore_and_R.ipynb”:

Required input files:
“Covid-19.csv”, “lacounty_covid.json”, “population.json”, “Covid-19-density.csv”

Output:
-Computing and displaying the risk score as well as Rt for both the entire LA county and its communities. For simplicity, we illustrate it for the following 4 communities, namely 'West Hollywood', 'East Los Angeles', 'Castaic', and 'San Pedro'.

Parameters:
number_of_days_passed_from_16th: #days passed March 16,2020 (e.g. it is 84 until June 7, 2020)
show_Risk :  True if showing risk score , otherwise False to show Rt and its confidence interval
Whole_LAcounty:  True to plot for entire LA county, and False to plot for the 4 communities
moving_average_days: used for smoothing the curves



================================================================================
“estimation_R_for_heatmap_histogram_of_RiskScore_and_R.ipynb”:
Required input files:
“Covid-19.csv”, “lacounty_covid.json”, “population.json”, “Covid-19-density.csv”

Output:
-Computing and displaying the histogram of risk scores as well as Rt across all communities
-Generating a csv file for showing a heatmap of risk scores

Parameters:
number_of_days_passed_from_16th: #days passed March 16,2020 (e.g. it is 84 until June 7, 2020)
moving_average_days: used for smoothing the curves

================================================================================
“generate_heatmap.py”:
Required input files:
“Covid-19.csv”, “lacounty_covid.json”, “population.json”, “Covid-19-density.csv”, "la.shp"

Output:
-Generate heatmaps for each day 

Execution command:
- python3.x generate_heatmap.py

=================================================================================
=============================     Results      ==================================
We added a simplified as well as a detailed csv files. 
Simiplifeid csv file: contains name of the community, Rt, and the risk level
Detailed csv file: contains Time stamp, name of the community, latitude, longitude, risk score, risk level (which is a quantized version of risk score into 4 levels 0-3)
=================================================================================


=================================================================================
================================= GitHub Repository =============================
We will also make the raw python scripts available via our GitHub repository: 
https://github.com/ANRGUSC/covid19_risk_estimation
=================================================================================


=================================================================================
================================= Contact Info ==================================
Mehrdad Kiamari (kiamari@usc.edu)
Professor Bhaskar Krishnamachari (bkrishna@usc.edu)
=================================================================================


