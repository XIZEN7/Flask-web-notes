from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean="True")


@auth.route('/logout')
def logout():
    data = request.form
    print(data)
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            pass
        elif len(name) < 2:
            pass
        elif password1 != password2:
            pass
        else:
            # Add user to database
            pass

    return render_template("sign_up.html")
