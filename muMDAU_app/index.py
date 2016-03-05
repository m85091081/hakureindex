# -*- coding: utf-8 -*-
# muMDAU_app main / first page 
from muMDAU_app import app 
from flask import request, render_template, Blueprint, url_for, redirect
from database import countUSER, ManageSQL, LoginSQL

main = Blueprint('main', __name__)

# index page main route page 
@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    else:
        # check admin is visable ?
        answer = countUSER.countAdmin()
        if answer[0] == 0:
            return redirect(url_for('init'))
        else:
            return render_template('index.html')

# init route to first time use
@app.route('/init', methods=['GET', 'POST'])
def init():
    if request.method == 'POST':
        user = request.form['buser']
        passd = request.form['bpass']
        import hashlib
        hashsha = hashlib.sha256(passd.replace('\n', '').encode())
        ManageSQL.addUser(user, hashsha.hexdigest(), '1', '0')
        return redirect(url_for('main.index'))
    else:
        return render_template('first.html')

# test of adduser route page 
@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
    if request.method == 'POST':
        user = request.form['buser']
        if LoginSQL.getPass(user) is None:
            import hashlib
            import random
            ans = random.uniform(1, 10)
            hashpass1 = hashlib.sha1(str(ans).encode())
            passd1 = hashpass1.hexdigest()
            hashpass0 = hashlib.sha256(passd1.replace('\n', '').encode())
            ManageSQL.addUser(user, hashpass0.hexdigest(), '0', '1')
            return passd1
        else:
            return '使用者已經他媽的存在了喔！'
