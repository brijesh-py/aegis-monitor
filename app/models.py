from app import db, UserMixin

# user join model
class Account(db.Model, UserMixin):
    __tablename__ = 'users_account'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    key = db.Column(db.String(20), unique = True, nullable=False)
    created_at = db.Column(db.String(30))
    is_active = db.Column(db.Boolean, default=True)
    data = db.relationship('Data', backref='account', lazy=True)

    def is_authenticated(self):
        return True
    
    def is_active(self):
        return self.is_active
    
    def is_anonymous(self):
        return True

    def get_id(self):
        return self.id
    
    def get_password(self, g_password):
        return self.password == g_password
    
    def get_key(self):
        return self.key

    def __repr__(self):
        return f"<User {self.username}>"
    

class Data(db.Model, UserMixin):
    __tablename__ = 'users_data'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users_account.id'), nullable=False)
    get_at = db.Column(db.String(30))

    def get_data(self, data):
        return self.data == data

    def __repr__(self):
        return f"<User {self.id}>"