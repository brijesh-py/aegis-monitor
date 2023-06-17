from flask import render_template, redirect, url_for, request, jsonify, json
from .forms import LoginForm, JoinForm
from .models import Account, Data, db
from app import login_required, login_user, current_user
from .auth import get_time, get_key, get_js
from slugify import slugify


@login_required
def home_view():
    data = Data.query.filter_by(user_id=current_user.id)
    return render_template("index.html", key=current_user.get_key(), data=data)


def login_view():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        username = form.username.data
        password = form.password.data
        check_username = Account.query.filter_by(username=username).first()
        check_email = Account.query.filter_by(email=username).first()
        if check_username and check_username.get_password(password):
            login_user(check_username)
            return redirect(url_for("home"))
        elif check_email and check_email.get_password(password):
            login_user(check_email)
            return redirect(url_for("home"))
        else:
            return render_template(
                "admin/login.html", form=form, error="Invalid Username or Password?"
            )
    return render_template("admin/login.html", form=form)


def join_view():
    form = JoinForm(request.form)
    if request.method == "POST" and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        if (
            Account.query.filter_by(username=username).first()
            or Account.query.filter_by(email=email).first()
        ):
            return render_template(
                "admin/join.html", form=form, error="Try anathor Username or Password?"
            )
        else:
            join_user = Account(
                username=username,
                email=email,
                password=password,
                created_at=get_time(),
                key=slugify(get_key(20)),
            )
            db.session.add(join_user)
            db.session.commit()
            db.session.close()
            return render_template(
                "admin/join.html", form=form, success="Successfuly Account created!"
            )
    return render_template("admin/join.html", form=form)


def data_view(key):
    if request.method == "POST":
        res = json.loads(request.form["res"])
        user_id = Account.query.filter_by(key=key).first()
        check_data = Data.query.filter_by(data=res).first()
        if user_id and (not check_data):
            store_data = Data(data=res, user_id=user_id.id, get_at=get_time())
            db.session.add(store_data)
            db.session.commit()
        return jsonify("200")


def query_view():
    return render_template("main/main.html", js=get_js())


def search_view():
    query = request.args.get("query")
    data = Data.query.filter(Data.data.like(f"%{query}%")).all()
    return render_template("index.html", key=current_user.get_key(), data=data)
