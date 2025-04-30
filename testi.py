import pickle

# with open('myData.pkl', 'rb') as f:
#     sentiment_analysis = pickle.load(f)

# print(sentiment_analysis.predict(['This is very good!']))


def get_sentiment():
    # input_data = request.json
    input_data = ['This is very bad!']
    with open('myData.pkl', 'rb') as f:
        sentiment_analysis = pickle.load(f)

    print(sentiment_analysis.predict(input_data))
    # print(input_data)

    # return {'input_data': input_data, 'message': 'Hello!'}

get_sentiment()