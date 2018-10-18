from flask import Flask, jsonify, request
app = Flask(__name__) # define app using flask

languages = [{'name': 'python'}, {'name':'javascript'}, {'name': 'ruby'}]

#get all tasks

@app.route('/', methods = ['GET'])
def test():
    return jsonify({'message': 'it works'})

@app.route('/lang', methods = ['GET'])
def returnAll():
    return jsonify({'languages': languages})

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language': langs[0]})

@app.route('/lang', methods=['POST'])
def addOne():
    language = {'name' : request.json['name']}

    languages.append(language)
    return jsonify({'languages':languages})



