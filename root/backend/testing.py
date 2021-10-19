# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np
import sys


# %%
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.preprocessing import LabelEncoder ,OneHotEncoder


# %%
dataset = pd.read_csv("database/dataset.csv");


# %%
df1 = pd.DataFrame(dataset)
X = df1.iloc[:,1:4]
Y = df1.iloc[:,0]
features = np.array(X.columns)
# features
np.array(X)


# %%
LabelEncoder_Y= LabelEncoder()
Y= LabelEncoder_Y.fit_transform(Y)
np.amin(Y)


# %%
# LabelEncoder_X= LabelEncoder()
# # X= np.array(X)
# # X = LabelEncoder_X.fit_transform(X[0])
# for i in range(0,3):
#     X.loc[:,features[i]]= LabelEncoder_X.fit_transform(X.iloc[:,i])
# print(X.shape)
# X
# np.array(X_train)


# %%
# after_encoding = pd.get_dummies(X,columns=features)
# X=after_encoding 
# X
enc = OneHotEncoder(handle_unknown='ignore').fit(X)
X = enc.transform(X).toarray()
X


# %%
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=5)
# after_one_hot_encoding_X_train = pd.get_dummies(X_train,columns=features)
# X_train = after_one_hot_encoding_X_train
# after_one_hot_encoding_X_test = pd.get_dummies(X_test,columns=features)
# X_test = after_one_hot_encoding_X_test
# from sklearn.preprocessing import StandardScaler
# sc_X = StandardScaler()
# X_train = sc_X.fit_transform(X_train)
# X_test = sc_X.fit_transform(X_test)


# %%
X_train = np.array(X_train)
X_test = np.array(X_test)
Y_train = np.array(Y_train)
Y_test = np.array(Y_test)


# %%
Y_test


# %%
model = keras.Sequential([
    keras.layers.Dense(900,activation = "relu"),
    keras.layers.Dense(500,activation = "relu"),
    tf.keras.layers.Dense(42,activation = 'softmax')
    # tried with sigmoid as well, but the results are quite same.
])
model.compile(
    optimizer ='adam',
    loss = 'sparse_categorical_crossentropy',
    metrics =['accuracy']
)
model.fit(X_train,Y_train,epochs = 5)


# %%
model.evaluate(X_test,Y_test)


# %%
Y_pred = model.predict(X_test)
Y_pred.shape


# %%
Y_pred_values =[np.argmax(i) for i in Y_pred]
Y_pred_values = np.array(Y_pred_values)
Y_pred_values


# %%
tf.math.confusion_matrix(labels=Y_test,predictions=Y_pred_values)


# %%
print(LabelEncoder_Y.inverse_transform([15]))


# %%
## for mongo db to puthon connection using pymongo
import pymongo as pm
from bson.objectid import ObjectId 

myconnection = pm.MongoClient("mongodb://localhost:27017/")

mydb = myconnection["health_db"]
mycol = mydb["Symptoms"]

print(sys.argv[1])

# insertion_id = {
#     "_id":ObjectId(sys.argv[1])
# }

symptoms_dict_array=[]
for x in mycol.find({'_id':ObjectId(sys.argv[1])},{"_id":0}):
  symptoms_dict_array.append(x)
symptoms_array = np.array(list(symptoms_dict_array[0].values()))

# symptoms_array = ["fatigue","weight_loss","restlessness"]
print(symptoms_array)
#['itching', ' skin_rash', ' dischromic _patches']

newvalues_X = enc.transform([symptoms_array]).toarray()
newvalues_X


# %%
# newvalues_X = enc.transform([['itching', ' skin_rash', ' dischromic _patches']]).toarray()
# newvalues_X.shape


# %%
Y_pred_new = model.predict(newvalues_X)


# %%
Y_pred_values_new =[np.argmax(i) for i in Y_pred_new]
Y_pred_values_new = np.array(Y_pred_values_new)
Y_pred_values_new[0]


# %%
output_value = LabelEncoder_Y.inverse_transform([Y_pred_values_new[0]])[0]
#print(LabelEncoder_Y.inverse_transform([Y_pred_values_new[0]]))
print(output_value)


# %%
dataset2 = pd.read_csv("database/symptom_Description.csv")
dataset2.index = dataset2.loc[:,"Disease"]


# %%
disease_description = dataset2.loc[[output_value],"Description"].to_numpy()
print(disease_description)


# %%
dataset3 = pd.read_csv("database/symptom_precaution.csv")
dataset3.index = dataset3.loc[:,"Disease"]


# %%
disease_precaution = dataset3.loc[[output_value],["Precaution_1","Precaution_2","Precaution_3","Precaution_4"]].to_numpy()
disease_precaution = disease_precaution.reshape(-1)
print(disease_precaution)


# %%
output_data_dictionary = {
    "$set":{
    "disease": output_value,
    "description": disease_description[0],
    "precautions_1": disease_precaution[0],
    "precautions_2": disease_precaution[1],
    "precautions_3": disease_precaution[2],
    "precautions_4": disease_precaution[3]
    }
}

insertion_id = {
    "_id":ObjectId(sys.argv[1])
}
print(insertion_id)
mycol.update_one(insertion_id,output_data_dictionary)


