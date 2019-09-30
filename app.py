import os
from flask import Flask, request, render_template, jsonify
from tweeter import TwitterClient

app= Flask(__name__)

api= TwitterClient('Data')

def strtobool(v):
    return v.lower() in ['yes', 'true', 't', 'l']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tweets')
def tweets():
    retweets_only= request.args.get('retweets_only')
    api.set_retweet_checking(strtobool(retweets_only.lower()))
    with_sentiment= request.args.get('with_sentiment')
    api.set_with_sentiment(strtobool(with_sentiment.lower()))
    query= request.args.get('query')
    api.set_query(query)
    
    tweets= api.get_tweets()
    
    return jsonify({'data' :tweets, 'count': len(tweets)})


port= int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=True)

#if __name__ == "__main__":
	#decide what port to run the app in
    #	port = int(os.environ.get('PORT', 5000))
	#run the app locally on the givn port
    #	app.run(host='0.0.0.0', port=port)
	#optional if we want to run in debugging mode
	#app.run(debug=True)
    
