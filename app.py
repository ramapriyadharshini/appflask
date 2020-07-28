from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
@app.route('/')
def alchemist():
   return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    client=MongoClient('54.236.26.79','27017')
    db=client['dummyy']
    users_collection=db['users']
    users=users_collection.find()
    print(users)
    authname = "ramapriya"
    Pass= "l0l0"
    username = request.form['username'] 
    password = request.form['password']
    if authname == username and Pass == password:
        return render_template('mydata.html')
    else:
        return 'Veliya podaaaa.......'

if __name__ == '__main__':
    app.run(debug=True)

