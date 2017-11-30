from app.instances.db import db


class User(db.Model):
    """
    Self-explanatory, a user.
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(320))

    posts = db.relationship('Post', backref=db.backref('user'))

    def to_json(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}

    def __repr__(self):
        return '<User({!r}) "{!r}">'.format(self.id, self.name)


class UserJWTToken(db.Model):
    """
    Represents an authentication scheme for a user based on a JWT-key style with
    an issuer and an identity. You **must** validate the key before inserting it
    here.
    """

    identity = db.Column(db.String(255), primary_key=True, nullable=False)
    issuer = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    user = db.relationship(User, backref=db.backref('jwt_tokens', lazy=True))

    def __repr__(self):
        return '<UserToken for {!r}>'.format(self.user_id)
