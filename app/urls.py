from app import app, login_manager, current_user
from .views import home_view, login_view, join_view, Account, data_view, redirect, url_for, query_view, search_view
from functools import wraps

def check_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        return func(*args, **kwargs)

    return wrapper

@login_manager.user_loader
def load_user(user_id):
    return Account.query.get(int(user_id))

@app.route('/')
def home():
    return home_view()

@app.route('/query')
def search():
    return search_view()

@app.route('/login/', methods=['GET','POST'])
@check_user
def login():
    return login_view()

@app.route('/join/', methods=['GET','POST'])
@check_user
def join():
    return join_view()

@app.route('/redirect/')
def query():
    return query_view()

@app.route('/query/<key>', methods=['GET','POST'])
def main(key):
    return data_view(key)
