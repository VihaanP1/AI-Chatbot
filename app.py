import flask
from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = "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"

@app.route("/", methods=["GET", "POST"])
def chat():
    response = ""
    if request.method == "POST":
        question = request.form["question"]
        response = ask_ai(question)
    return render_template("index.html", response=response)

def ask_ai(question):
    ai_response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}]
    )
    return ai_response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    app.run(debug=True)


