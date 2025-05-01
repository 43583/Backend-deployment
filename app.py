from flask import Flask, request
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app, resources={r'/sentiment': {'origins': 'https://sentiment-front-f9yy.onrender.com'}})

@app.route("/sentiment", methods=['POST'])
def get_sentiment():
    input_data = request.json
    print(input_data['text'])
    input_data = input_data['text']

    with open('myData.pkl', 'rb') as f:
        sentiment_analysis = pickle.load(f)

    sentiment = sentiment_analysis.predict([input_data])


    return {'input_data': input_data, 'message': sentiment[0]}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=False)