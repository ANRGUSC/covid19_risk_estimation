# COVID-19 Risk Estimation for L.A. County using a Bayesian Time-varying SIR-model

This repository presents a rigorous hybrid model-and-data-driven Bayesian approach to risk scoring that yields a simplified color-coded risk level for each community in the city of Los Angeles. The risk score corresponds to the probability of someone currently healthy getting infected with COVID-19 in the near future. It is currently being used by the City of Los Angeles to help mitigate the spread of Covid-19 throughout the county. 

<ins>***This model can be replicated by other cities/communities to help mitigate Covid-19 cases***</ins>.

## Data Source

This project used CoVID-19 case data from LA County Dep. of Public Health, which is also available in the following repository: [Data](https://github.com/ANRGUSC/lacounty_covid19_data/).

## Instructions for running the following codes
The requirements.txt file contains the modules needed to run these scripts and can be installed by running any of the following in the terminal:
* pip install -r requirements.txt
* conda install --file requirements.txt

*Note: Jupyter Notebook module needed to run the Jupyter Notebooks



## Running **estimation_prediction_for_RiskScore_and_R.ipynb(.py)**

This main file can be found in the [/software](https://github.com/ANRGUSC/covid19_risk_estimation/tree/master/software) folder.

Required input files:
[Covid-19.csv](https://github.com/ANRGUSC/covid19_risk_estimation/blob/master/data/Covid-19.csv), [lacounty_covid.json](https://github.com/ANRGUSC/covid19_risk_estimation/blob/master/data/lacounty_covid.json), [population.json](https://github.com/ANRGUSC/covid19_risk_estimation/blob/master/data/population.json), [Covid-19-density.csv](https://github.com/ANRGUSC/covid19_risk_estimation/blob/master/data/Covid-19-density.csv)

Output:
- Files containing computation and visual displays of the risk score and Rt for the entire LA county and its communities. These can be found in the [dailycasesR](https://github.com/ANRGUSC/covid19_risk_estimation/tree/master/data/dailycasesR) and [map](https://github.com/ANRGUSC/covid19_risk_estimation/tree/master/plots/map) folders. We've picked to showcase this for some communities for illustration purposes. The following four communities were chosen: West Hollywood, East Los Angeles, Castaic, and San Pedro. The files for these can be found in the [plots](https://github.com/ANRGUSC/covid19_risk_estimation/tree/master/plots) file as png files. 

Parameters:
* number_of_days_passed_from_16th: Number of days passed since March 16, 2020 (e.g. June 7, 2020 marks 84 days since March 16, 2020)
* show_Risk :  True if showing risk score, otherwise show Rt and its confidence interval
* Whole_LAcounty:  True to plot for entire LA county, and False to plot for the four sample communities
* moving_average_days: used for smoothing the curves

Example of risk assessments of communities gif through time:

<img src="https://github.com/ANRGUSC/covid19_risk_estimation/blob/master/plots/covidlarisk.gif" width="550">


## Running **estimation_R_for_heatmap.ipynb**

Required input files:
[Covid-19.csv](https://github.com/ANRGUSC/covid19_risk_estimation/blob/master/data/Covid-19.csv), [lacounty_covid.json](https://github.com/ANRGUSC/covid19_risk_estimation/blob/master/data/lacounty_covid.json), [population.json](https://github.com/ANRGUSC/covid19_risk_estimation/blob/master/data/population.json), [Covid-19-density.csv](https://github.com/ANRGUSC/covid19_risk_estimation/blob/master/data/Covid-19-density.csv)

Output:
* Computing and displaying the histogram of risk scores as well as Rt across all communities
* Generating a csv file for showing a heatmap of risk scores

Parameters:
* number_of_days_passed_from_16th: number of days passed March 16,2020 (e.g. June 7, 2020 marks 84 days since March 16, 2020)
* moving_average_days: used for smoothing the curves

## Running **generate_heatmap.py**

Required input files:
[Covid-19.csv](https://github.com/ANRGUSC/covid19_risk_estimation/blob/master/data/Covid-19.csv), [lacounty_covid.json](https://github.com/ANRGUSC/covid19_risk_estimation/blob/master/data/lacounty_covid.json), [population.json](https://github.com/ANRGUSC/covid19_risk_estimation/blob/master/data/population.json), [Covid-19-density.csv](https://github.com/ANRGUSC/covid19_risk_estimation/blob/master/data/Covid-19-density.csv), [la.shp](https://github.com/ANRGUSC/covid19_risk_estimation/blob/master/data/la.shp)

Output:
* Heat maps for each day 

## Google Colab

Colab notebook includes instructions, explanation of code pieces, and downloadable sample data to run. 

[![Open Sample code in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ExWvM99PE5fRvo9KAadakO28pYAT39XX?usp=sharing)


## Questions
For any questions about this project, please contact Prof. Bhaskar Krishnamachari (bkrishna@usc.edu).
