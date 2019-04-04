from app import app
from flask import render_template, flash, redirect,url_for,request
from app.forms import SearchForm
from urllib.request import urlopen

def response(host,username):
    if host[-1] != "/":
        host = host + "/"
    if host[0:4] != "http":
        host = "https://" + host

    try:
        conn = urlopen(host+username)
        return "unavailable" if str(conn.getcode()) == "200"  else 0
    except Exception as e:
        return "available" if str(e)[11:14] == "404" else 0

@app.route('/',methods=['GET','POST']) 
@app.route('/index', methods=['GET','POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        post = {"username":form.username.data}
        if form.facebook.data:
            out=response("https://facebook.com/",form.username.data)
            if out == 0:
                post ["facebook"]= "Error"
            else:
                post ["facebook"]= out
        if form.soundcloud.data:
            out=response("https://soundcloud.com/",form.username.data)
            if out == 0:
                post["soundcloud"]= "Error"
            else:
                post["soundcloud"]=out
        if form.github.data:
            out=response("https://github.com/",form.username.data)
            if out == 0:
                post["github"]= "Error"
            else:
                post["github"] = out
        if form.instagram.data:
            out=response("https://instagram.com/",form.username.data)
            if out == 0:
                post["instagram"]= "Error"
            else:
                post["instagram"] = out
        if form.twitter.data:
            out=response("https://twitter.com/",form.username.data)
            if out == 0:
                post["twitter"]= "Error"
            else:
                post["twitter"]=out
        if form.othersite.data:
            out=response(form.othersite.data,form.username.data)
            post["site"]=form.othersite.data
            if out == 0:
                post["othersite"]= "Error"
            else:
                post["othersite"] = out
        print (post)
        return render_template('out.html', title="Result",posts=post)
    return render_template('index.html', title="Home",form=form)