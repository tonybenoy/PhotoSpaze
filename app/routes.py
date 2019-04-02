from app import app,login
from flask import render_template, flash, redirect,url_for,request
from app.forms import LoginForm,RegisterationForm
import pymongo
from flask_login import login_user,current_user,UserMixin,logout_user,login_required 
from werkzeug.security import generate_password_hash,check_password_hash
from werkzeug.urls import url_parse
from bson.objectid import ObjectId

@app.route('/',methods=['GET']) 
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', title="Home")

@app.route('/register',methods=['GET','POST'])
def register():
    #if current_user.is_authenticated:
    #    return(url_for('index'))
    form = RegisterationForm()
    if form.validate_on_submit():
        myclient = pymongo.MongoClient("mongodb://localhost:27017")
        mydb = myclient["mydatabase"]
        mycol = mydb["users"]
        myquery = {"email":form.email.data}
        mydoc = mycol.find_one(myquery)
        if mydoc:
            flash('Email address already exist!') 
            myclient.close()
            return redirect(url_for('register'))
        myquery = {"username":form.username.data}
        mydoc = mycol.find_one(myquery)
        if mydoc:
            flash('Username already exist!')
            myclient.close()
            return redirect(url_for('register'))
        hashedpass = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=12)
        mydict = { "username":form.username.data, "email": form.email.data,"password":hashedpass}
        x = mycol.insert_one(mydict)
        flash('Congratulations, you are now a registered user!')
        myclient.close()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    #if current_user.is_authenticated:
    #    return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        myclient = pymongo.MongoClient("mongodb://localhost:27017")
        mydb = myclient["mydatabase"]
        mycol = mydb["users"]
        myquery = {"username":form.username.data}
        mydoc = mycol.find_one(myquery)
        print(mydoc)
        myclient.close()
        if mydoc == None:
            flash('Username not found! Do you want to register?')
            return redirect(url_for('login'))
        else:
            if check_password_hash(mydoc["password"], form.password.data) == False:
                flash('Invalid Password')
                return redirect(url_for('login'))
            else:
                user = User()
                user.id = mydoc["_id"] 
                user.name = form.username.data
                login_user(user, remember = form.remember_me.data) 
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                    next_page = url_for('index')
                return redirect(next_page) 
    return render_template('login.html',title='Sign In', form=form)

@app.route("/<username>", methods=['GET'])
def userpage(username):
    return render_template('user.html', title=username)
    
@app.route("/image/<imgid>", methods=['GET'])
def image(imgid):
    return render_template('image.html')