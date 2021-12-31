import pickle
import time
from sklearn.linear_model import LogisticRegression
import numpy
from flask import *
import json,time
import requests
from translate import Translator

app = Flask(__name__)

@app.route('/')
def home_page():
    #list = requests.get("list")
    data_set ={'Page': 'Home', 'Message':'Success loaded home page', 'TimeStamp':time.time()}
    json_dump = json.dumps(data_set)

    return json_dump

@app.route('/predict/' ,  methods=['GET'])
def user_page():
    user_query = str(request.args.get('predict')) #/user/?user=USER_NAME
    print("user",user_query)
    list = []
    toplam = 0
    splt = user_query.split(",")
    for i in splt:
        list.append(i)
    print("list",list)
    list = numpy.array(list)
    list = list.reshape(1,-1)
    print("list2",list)
    file = open("finalized_model.sav", 'rb')
    model = pickle.load(file)
    predicted = model.predict(list)
    str_pred = str(predicted[0])
    file.close()
    translator = Translator(to_lang="Turkish")
    translation = translator.translate(str_pred)
    data_set ={'Page': 'Request', 'Message':f' USer Success loaded request page for {translation}', 'TimeStamp':time.time()}
    json_dump = json.dumps(data_set)
    return json_dump

if __name__ == '__main__':
    app.run(debug=True)

