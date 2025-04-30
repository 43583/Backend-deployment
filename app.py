from flask import Flask, request
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app, resources={r'/sentiment': {'origins': 'http://localhost:5173'}})


@app.route("/sentiment", methods=['POST'])
def get_sentiment():
    # input_data = request.json
    input_data = 'This is very good!'
    with open('myData.pkl', 'rb') as f:
        sentiment_analysis = pickle.load(f)

    print(sentiment_analysis.predict(input_data))
    # print(input_data)

    return {'input_data': input_data, 'message': 'Hello!'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=False)