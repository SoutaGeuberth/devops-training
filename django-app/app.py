from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.config['MONGO_URI'] = 'mongodb://logindb:27017/login'  # Reemplaza con la URI de tu base de datos
logindb = PyMongo(app)
app.config['MONGO_URI'] = 'mongodb://crud-router:27017/data'  # Reemplaza con la URI de tu base de datos
datadb = PyMongo(app)

@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        
        users = logindb.db.users
        user_data = users.find_one({'username': username})
        
        if user_data:
            user_id = user_data['_id']
            
            additional_info = datadb.db.data
            additional_info_data = additional_info.find_one({'user_id': user_id})
            if additional_info_data:
                return render_template('home.html', user_data=user_data, additional_info_data=additional_info_data)
            else:
                return 'pagina de inicio sin data'
    else:
        return redirect(url_for('login'))
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        identification = request.form['identification']
        address = request.form['address']
        phone = request.form['phone']
        occupation = request.form['occupation']
        
        hashed_password = generate_password_hash(password, method='sha256')
        
        user_data = {
            'username': username,
            'password': hashed_password
        }
        users = logindb.db.users
        result = users.insert_one(user_data)
        profile_data = {
            'identification':identification,
            'address':address,
            'phone':phone,
            'occupation':occupation,
            'user_id':result.inserted_id
        }
    
        data = datadb.db.data
        data.insert_one(profile_data)
        flash('Usuario registrado con éxito', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        users = logindb.db.users
        user_data = users.find_one({'username': username})
        
        if user_data and check_password_hash(user_data['password'], password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Credenciales inválidas. Inténtalo de nuevo.', 'danger')
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
