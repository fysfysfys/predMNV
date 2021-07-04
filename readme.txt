predWNV：
We developed a model to predict the number of West Nile virus infected human. 
First, we collect data from https://westnile.ca.gov/, which offers number of West Nile virus infections in California by weeks. 
Then we found that the number of infected human was strongly correlated with the infected dead bird, Mosquito and Sentinel Chickens. 
Based on this, we used linear regression to build a prediction model for the number of virus infected human. 
The script is “predWNV.py” and data used to model named “matrix_data.csv”. Users should provide number of infected animals several weeks ago such as "matrix_input.csv".
Python packages pandas,sklearn are needed to be installed before running of predWNV.py. The program needs to run on the Linux operating system.

Dependencies:
Python 3, pandas, scikit-learn
pip install pandas
pip install -U scikit-learn

Usage:
Users can provide the number of infected human (3 weeks ago), dead_bird (7 weeks ago), mosquito (7 weeks ago)，Sentinel_Chickens (4 weeks ago) to predict the number of virus infected people in the next 1-3 weeks. 
For example, if you want to predict the number of West Nile virus infected human in 2020_week25, 
provide the number of infected human (2020_week22), dead_bird (2020_week18), mosquito (2020_week18), Sentinel_Chickens (2020_week21) as “X_test” in “matrix_input.csv”.

use the simplify command:
python3 predWNV.py -t ./matrix_data.csv -i ./matrix_input.csv -o ./result_final.txt

-t: The file name of the training model data.
-i: The file name of the inspection data of the week to be predicted.
-o: The name of result of predicting infected human file.

Interpretation of Result:
After running the prediction program, you will see the output files "result_final.txt" in the output folder.
The first column represents the number of weeks, and the second column represents the number of infected human.
