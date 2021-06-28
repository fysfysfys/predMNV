We developed a model to predict the number of West Nile virus infected human. 
First, we collect data from https://westnile.ca.gov/, which offers number of West Nile virus infections in California by weeks. 
Then we found that the number of infected human was strongly correlated with the infected dead bird, Mosquito and Sentinel Chickens. 
Based on this, we used linear regression to build a prediction model for the number of virus infected human. 
The script is “predWNV.py” and data used to model named “matrix_data.csv”.



Users can provide the number of infected human (3 weeks ago), dead_bird (7 weeks ago), mosquito (7 weeks ago)，Sentinel_Chickens (4 weeks ago) to predict the number of virus infected people in the next 1-8 weeks. 
Eg: If you want to predict the number of West Nile virus infected human in 2020_week25, 
provide the number of infected human (2020_week22), dead_bird (2020_week18), mosquito (2020_week18), Sentinel_Chickens (2020_week21) as “X_test” in “matrix_data.csv”,
you will obtain predicting result in 2020_week25("2020_week25	predict:0") and in future 7week("2020_week25	predict:1-7").
