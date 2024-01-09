#
# import pickle
#
# data_dict = pickle.load(open('./data.pickle', 'rb'))
# c = 0
# d = 0
# for i in data_dict["data"]:
#     if len(i) == 84:
#         c += 1
#     else:
#         d += 1
# print(c)
# print(d)


# i = 0
# while data_dict["labels"][i] != '10':
#     i += 1
# print(data_dict["data"][i])

#
# print(data_dict["data"])
# print(data_dict["labels"])

# import pickle
#
# data_dict = pickle.load(open('./data.pickle', 'rb'))
#
# print(data_dict.keys())
# print(data_dict)










#
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

data_dict = pickle.load(open('./data.pickle', 'rb'))

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

model = RandomForestClassifier()

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly !'.format(score * 100))

f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()
