from flask import Flask,render_template,request
from youtube_search import YoutubeSearch
from pytube import YouTube
from flask_cors import CORS
app = Flask(__name__,template_folder='template')
CORS(app)
@app.route('/',methods=["POST","GET"])
def hello_world():
    return render_template('yt.html')

@app.route('/res',methods=["POST","GET"])
def res():
    h=request.form['srch']
    results = YoutubeSearch(h, max_results=200).to_json()
    return results
    
@app.route('/resapi',methods=["POST","GET"])
def resapi():
    #h=request.form['srch']
    h2=request.args.get('srch')
    results = YoutubeSearch(h2, max_results=200).to_json()
    return results

@app.route('/download',methods=["POST","GET"])
def download():
    url=request.form['url']
    YouTube(url).streams.first().download()
    return url
    
    #get links
@app.route('/mult',methods=["POST","GET"])
def mult():
    yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
    yt.streams.all()  # list of all available streams
    a=yt.streams[0].url
    return a
if __name__ == "__main__":    
   app.run(debug=True)
