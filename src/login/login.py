from flask import Blueprint, request
from flask import render_template, redirect

login = Blueprint('login', __name__, url_prefix='/')

@login.route('/login', methods=['GET'])
def loginMethod():
    """This function renders the edit task page."""
    return render_template("login.html")

@login.route('/login', methods=['POST'])
def loginPostMethod():
    """This function renders the edit task page."""
    return redirect("/")

@login.route('/logout', methods=['GET'])
def logoutMethod():
    """This function renders the edit task page."""
    return redirect("/login")