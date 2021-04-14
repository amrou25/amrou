from flask import Flask,render_template,request
from youtube_search import YoutubeSearch
from pytube import YouTube
app = Flask(__name__,template_folder='template')

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


if __name__ == "__main__":    
   app.run(debug=True)
