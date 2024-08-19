import requests
from flask import Flask,render_template
from form import YourText,YourREsult
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor

app=Flask(__name__)
app.config['SECRET_KEY'] = "12345"
ckeditor=CKEditor(app)
Bootstrap5(app)

@app.route("/",methods=["POST","GET"])
def home():
    form=YourText()
    result_form=YourREsult()
    if form.validate_on_submit():
        text_tocorrect=form.task.data
        
        endpoint="https://api.sapling.ai/api/v1/summarize"
        param={"key":"5Q7E2TSLA3Q27U6NHJ7VW38P1VO4SD7C", 
       "text":text_tocorrect,
       "session_id": "test session"}
        response=requests.post(url=endpoint,json=param)

        response_json=response.json()
        result_form.task.data=response_json["result"]
        return render_template("index.html",form=form,result_form=result_form)
    return render_template("index.html",form=form,result_form=result_form)

@app.route("/about")
def about():
    return render_template("about.html")


if __name__=="__main__":
    app.run(debug=True)