# COVID-19 Risk Estimation for L.A. County using a Bayesian Time-varying SIR-model

This repository presents a rigorous hybrid model-and-data-driven Bayesian approach to risk scoring that yields a simplified color-coded risk level for each community. The risk score corresponds to the probability of someone currently healthy getting infected with COVID-19 in the near future. 

## Data Source

This project used CoVID-19 case data from LA County Dep. of Public Health, which is also available in the following repository: [Data](https://github.com/ANRGUSC/lacounty_covid19_data/).

## Instructions for running the following codes
The requirements.txt file contains the modules needed to run these scripts and can be installed by running any of the following in the terminal:
* pip install -r requirements.txt
* conda install --file requirements.txt
**Note: Jupyter Notebook module needed to run the Jupyter Notebooks



## Running **estimation_prediction_for_RiskScore_and_R.ipynb**

Required input files:
[Covid-19.csv](https://github.com/ANRGUSC/covid19_risk_estimation/blob/master/data/Covid-19.csv), [lacounty_covid.json](https://github.com/ANRGUSC/covid19_risk_estimation/blob/master/data/lacounty_covid.json), [population.json](https://github.com/ANRGUSC/covid19_risk_estimation/blob/master/data/population.json), [Covid-19-density.csv](https://github.com/ANRGUSC/covid19_risk_estimation/blob/master/data/Covid-19-density.csv)

Output:
-Computing and displaying the risk score as well as Rt for both the entire LA county and its communities. For simplicity, we illustrate it for the following 4 communities, namely 'West Hollywood', 'East Los Angeles', 'Castaic', and 'San Pedro'.

Parameters:
* number_of_days_passed_from_16th: #days passed March 16,2020 (e.g. it is 84 until June 7, 2020)
* show_Risk :  True if showing risk score , otherwise False to show Rt and its confidence interval
* Whole_LAcounty:  True to plot for entire LA county, and False to plot for the 4 communities
* moving_average_days: used for smoothing the curves

## Running **estimation_R_for_heatmap_histogram_of_RiskScore_and_R.ipynb**

Required input files:
“Covid-19.csv”, “lacounty_covid.json”, “population.json”, “Covid-19-density.csv”

Output:
* Computing and displaying the histogram of risk scores as well as Rt across all communities
* Generating a csv file for showing a heatmap of risk scores

Parameters:
* number_of_days_passed_from_16th: #days passed March 16,2020 (e.g. it is 84 until June 7, 2020)
* moving_average_days: used for smoothing the curves

## Running **generate_heatmap.py**

Required input files:
“Covid-19.csv”, “lacounty_covid.json”, “population.json”, “Covid-19-density.csv”, "la.shp"

Output:
* Generate heatmaps for each day 

Execution command:
* python3.x generate_heatmap.py

## Questions
For any questions about this project, please contact Prof. Bhaskar Krishnamachari (bkrishna@usc.edu).
