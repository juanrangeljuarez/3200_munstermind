from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('munstermind.html')

@app.route('/checkguess', methods={'POST'})
def checkguess():
    print('in check guess')
    print(request.json) #print out the json object to the console
    print(request.json['guess']) #print out the guess to the console
    print(request.json['enigma']) #print out the enigma to the console
    guess_list = request.json['guess']
    enigma_list = request.json['enigma']

    whitePeg = 0
    blackPeg = 0


    for x in range(4):
        if guess_list[x] == enigma_list[x]:
            blackPeg = blackPeg + 1

    for i in range(4):
        for e in range(4):
            if guess_list[i] == enigma_list[e] and i != e:
                whitePeg = whitePeg + 1
                break

    hint = {'whitePegs':whitePeg, 'blackPegs':blackPeg} #create the hint as a dicts
    print("the hint:", hint) #print out the hint to the console
    return jsonify(hint) #return the dict as a json


@app.route('/tinker_json')
def bar():
    # see https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
    tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
    ]
    return jsonify({'tasks': tasks})
