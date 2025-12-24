from flask import Flask,render_template,request
from question_embed import get_answer

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/handle",methods=["GET","POST"])
def handle():
    if request.method=="POST":
        query=request.form["query"]
        answer=get_answer(query)
    return render_template("answerpage.html",answer=answer)

app.run(debug=True)
