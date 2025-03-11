# Backend & Frontend: app.py (Flask with Jinja templates)
from flask import Flask, render_template, request, session, redirect, url_for
from flask_cors import CORS
import random
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from graphdb.demo import query_graphdb

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
CORS(app)

endpoint = "http://localhost:7200/repositories/HistoriaPT"
sparql_query = """
PREFIX historia: <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>

select ?rei ?nome ?nascimento where { 
  ?rei a historia:Rei ;
       historia:nome ?nome ;
       historia:nascimento ?nascimento .
}
"""

result = query_graphdb(endpoint, sparql_query)
list_rei = []
#result = json.loads(result)
for r in result['results']['bindings'] :
    t = (r['rei']['value'].split('#')[-1], r['nome']['value'].split('#')[-1], r['nascimento']['value'].split('#')[-1])
    list_rei.append(t)

questions = []

@app.route('/')
def home():
    session['score'] = 0
    return redirect(url_for('quiz'))

@app.route('/quiz', methods=['GET'])
def generate_question():
    reis_random = random.sample(list_rei, 4)
    answers = [ data for _,_, data in reis_random ]
    random.shuffle(answers)
    
    question_type1 = {
        'question': "Qual a data de nascimento do Rei " + reis_random[0][1] + "?",
        'options': answers,
        "answer": reis_random[0][2]
    } 
    
    random_entry = random.choice(answers)
    answer = "True" if reis_random[0][2] ==  random_entry else "False"
    
    question_type2 = {
        'question': "O Rei " + reis_random[0][1] + " nasceu em " + random_entry + "?",
        'options': ["True","False"],
        "answer": answer
    } 
    
    question = random.choice([question_type1, question_type2])
    questions.append(question)
    
    return render_template('quiz.html', question=question)
    

@app.route('/quiz', methods=['POST'])
def quiz():
    user_answer = request.form.get('answer')
    question_text = request.form.get('question')
        
        
    for question in questions:
        if question['question'] == question_text:
            correct = question['answer'] == user_answer
            session['score'] = session.get('score', 0) + (1 if correct else 0)
            return render_template('result.html', correct=correct, correct_answer=question['answer'], score=session['score'])

@app.route('/score')
def score():
    return render_template('score.html', score=session.get('score', 0))

if __name__ == '__main__':
    app.run(debug=True)

