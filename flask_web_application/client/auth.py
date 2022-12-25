from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        passwd = request.form.get('password')
        if len(passwd) < 3 :
            flash('Please Enter a password of minimum 5 characters', category='error')
        else:
            print(passwd)
    return render_template("signup.html")