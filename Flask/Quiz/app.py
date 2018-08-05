from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    DATA = {
                "0": {
                    "question": "Which one is correct team name in NBA?",
                    "options": ["New York Bulls","Los Angeles Kings","Golden State Warriros","Huston Rocket"],
                    "answer": "Huston Rocket"},
                "1": {
                    "question": "5 + 7 = ?",
                    "options": ["10","11","12","13"],
                    "answer": "12"
                },
                "2": {
                    "question": "12 - 8 = ?",
                    "options": ["1","2","3","4"]
                    ,"answer": "4"}}

    return  render_template('index.html',quiz = DATA)

if __name__ == '__main__':
    app.run(port=5011, debug=True)