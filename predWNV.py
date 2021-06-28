import pandas as pd
from sklearn.linear_model import LogisticRegression
num_input = 8   #### Number of weeks you want predict
p = open('result_final.txt', 'w')
p.write('year_week'+'\t'+'predict_weeks'+'\t'+'y_test'+'\t'+'y_pred'+'\n')
data = pd.read_csv("matrix_data.csv", index_col=0)
rows = data.shape[0]
for i in range(1, rows + 1):
    week_name = data.index[i-1]
    x_train = pd.DataFrame(data.iloc[0:i, 1:])
    y_train = data.iloc[0:i, 0:1].values.ravel()

    flag = False
    for k in y_train:
        if k != 0:
            flag = True

    if i != rows and flag == True and i+num_input <= rows:
        for k_num_input in range(0, num_input):
            p.write(str(week_name) + '\t')
            p.write('predict:'+str(k_num_input)+'\t')
            x_test = pd.DataFrame(data.iloc[i+k_num_input:i + k_num_input + 1, 1:])
            ### x_test: move_human_own(3 weeks ago)，dead_bird(7 weeks ago),mosquito(7 weeks ago)，Sentinel_Chickens(4weeks ago).
            y_test = pd.DataFrame(data.iloc[i+k_num_input, 0:1]).iat[0, 0]
            clf = LogisticRegression(solver='liblinear')
            clf.fit(x_train, y_train)
            y_pred = int(clf.predict(x_test))
            p.write(str(y_test) + '\t' + str(y_pred) + '\n')
    else:
        pass
p.close()

