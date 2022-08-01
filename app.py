from flask import Flask,request
from flask_restful import Resource, Api
import pickle
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
#
CORS(app)
# creating an API object
api = Api(app)

#prediction api call
class prediction(Resource):
    def get(self,Tori_Bohsa,Kutar,Cokar,Mix_Ati,Buffalo,Pala,Red_Sindhi,Thari,Kacchi,Gabrali):
        #budget = request.args.get('budget')
        print(Kutar)
        # Let's load the 
        
        Tori_Bohsa = [int(Tori_Bohsa)]
        Kutar = [int(Kutar)]
        Cokar = [int(Cokar)]
        Mix_Ati = [int(Mix_Ati)]
        Buffalo = [int(Buffalo)]
        Pala = [int(Pala)]
        Red_Sindhi = [int(Red_Sindhi)]
        Thari = [int(Thari)]
        Kacchi = [int(Kacchi)]
        Gabrali = [int(Gabrali)]

        df = pd.DataFrame(
        list(zip(Tori_Bohsa,Kutar,Cokar,Mix_Ati,Buffalo,Pala,Red_Sindhi,Thari,Kacchi,Gabrali,)) ,
        columns=['Tori/ Bohsa'
        ,'Kutar','Cokar','Mix Ati','Buffalo','Pala','Red Sindhi','Thari','Kacchi','Gabrali'
        ])
        model = pickle.load(open('MilkYieldPredicted', 'rb'))
        prediction = model.predict(df)
        prediction = int(prediction[0])
        return str(prediction)
#data api

class getData(Resource):
    def get(self):
            df = pd.read_excel('data.xlsx')
            df =  df.rename({'MilkYieldPredicted': 'MilkYieldPredicted', 'MilkYield': 'milk'}, axis=1)  # rename columns
            #print(df.head())
            #out = {'key':str}

            res = df.to_json(orient='records')

            #print( res)

            return res
# 
api.add_resource(getData, '/api')


api.add_resource(prediction, '/prediction/<int:Tori_Bohsa>,<int:Kutar>,<int:Cokar>,<int:Mix_Ati>,<int:Buffalo>,<int:Pala>,<int:Red_Sindhi>,<int:Thari>,<int:Kacchi>,<int:Gabrali>')
# api.add_resource(prediction, '/prediction/","toriBohsa=","<int:Tori_Bohsa>,<int:Kutar>,<int:Cokar>,<int:Mix_Ati>,<int:Buffalo>,<int:Pala>,<int:Red_Sindhi>,<int:Thari>,<int:Kacchi>,<int:Gabrali>')

if __name__ == '__main__':
    app.run(debug=True)