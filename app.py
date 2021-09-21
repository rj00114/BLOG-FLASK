import datetime
from flask import Flask, request, render_template
from flask_restful import Resource, Api
from werkzeug.utils import redirect
from queries import find_user_query, make_an_account, blog_creating, get_all_blogs

app = Flask(__name__)
api = Api(app)

@app.route("/", methods=["POST", "GET"])
def home_page():
    if request.method == "GET":
        return render_template('login.html')
    
    elif request.method == "POST":
        try:
            id = request.form.get('id')
            email = request.form.get('email')
            password = request.form.get('password')
            if len(id) == 0 or len(email) == 0 or len(password) == 0:
                raise Exception
        except:
            return render_template('login.html', result="Enter all entries")

        is_found = find_user_query(id, email, password)
        if is_found != "permitted":
            return render_template('login.html', result=is_found)
        else:
            url = 'blog_today/' + id
            return redirect(url)
        

@app.route('/blog_today/<string:id>', methods=["POST", "GET"])
def blog(id):
    if request.method == "POST":
        new_blog = request.form.get("content")
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        blog_creating(id, date, new_blog)
    blogs = get_all_blogs(id)
    return render_template('blog.html', id=id, entries=blogs)

@app.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template('signup.html')
    
    elif request.method == "POST":
        try:
            id = request.form.get('id')
            email = request.form.get('email')
            password = request.form.get('password')
            repassword = request.form.get('repassword')
            if len(id) == 0 or len(email) == 0 or len(password) == 0 or len(repassword) == 0:
                raise Exception
        except:
            return render_template('signup.html', result="Enter all entries")
        if password != repassword:
            return render_template("signup.html", result="Passwords do not match!")
        result = make_an_account(id, email, password)
        if result != "done":
            return render_template("signup.html", result=result)
        else:
            url = 'blog_today/' + id
            return redirect(url)