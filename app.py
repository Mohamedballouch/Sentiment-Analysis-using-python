from termcolor import colored
import nltk
from flask import Flask, render_template, request , jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import json
set(stopwords.words('english'))
to_remove=["aren",
"aren't","couldn","couldn't","didn","don't","didn't","doesn","doesn't","hadn","hadn't","hasn","hasn't","haven","haven't","isn","isn't","not"]
mystopwords=set(stopwords.words('english')).difference(to_remove)
app = Flask(__name__)

@app.route('/') # default route
def my_form():
	return render_template('index.html') 

@app.route('/get_data', methods = ['POST']) 
def my_form_post():
         
	stop_words=set(stopwords.words('english'))
	text1= request.form['text1'].lower()
	processed_doc1=' '.join([word for word in text1.split() if word not in stop_words])
	sa=SentimentIntensityAnalyzer()
	dd=sa.polarity_scores(text=processed_doc1)
	compound=round((1 + dd['compound'])/2,2)*100
	k=""
	c=text1.split()
	for wd in c:
		a=sa.polarity_scores(text=wd)
		b=round((1 + a['compound'])/2,2)*100
		if b>50:
			k+='<font color="green">'+wd+'<font/>'+ ' '
		elif b==50:
			k+='<font color="black">'+wd+'<font/>' +' '
		else:
			k+='<font color="red">'+wd+'<font/>' +' '
	
	return jsonify(final=compound,text1=k)
	
#resp={final:compound,text1:k}
            #render_template(final=compound,text1=k)
if __name__ == '__main__':
	app.run(debug=True,host="127.0.0.1", port=5002, threaded=True)
