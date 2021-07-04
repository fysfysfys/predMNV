import pandas as pd
from sklearn.linear_model import LogisticRegression
p = open('result_final.txt', 'w')   ### -o
p.write('predict_weeks'+'\t'+'y_pred'+'\n')
data = pd.read_csv("matrix_data.csv", index_col=0)   ### -t
data_input_test = pd.read_csv("matrix_input.csv", index_col=0)  ### -i

i = 297
x_train = pd.DataFrame(data.iloc[0:i, 1:])
y_train = data.iloc[0:i, 0:1].values.ravel()
clf = LogisticRegression(solver='liblinear')
clf.fit(x_train, y_train)

for j in range(0, data_input_test.shape[0]):
    x_test = pd.DataFrame(data_input_test.iloc[0+j:1+j, 1:])
    y_pred = int(clf.predict(x_test))
    p.write('future_week'+str(j+1)+'\t' + str(y_pred) + '\n')
p.close()
