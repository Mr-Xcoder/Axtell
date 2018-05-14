from app.instances.db import db
from sqlalchemy.dialects.mysql import LONGTEXT
from config import posts
from app.models.PostRevision import PostRevision
import datetime


class Post(db.Model):
    """
    Represnts a post (e.g. challenge)
    """

    __tablename__ = 'posts'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(posts['max_title']), nullable=False)
    body = db.Column(LONGTEXT, nullable=False)
    deleted = db.Column(db.Boolean, nullable=False, default=False)

    date_created = db.Column(db.DateTime, default=datetime.datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_json(self):
        return {
            'title': self.title,
            'body': self.body,
            'owner': self.user.to_json(),
            'date_created': self.date_created.isoformat(),
            'deleted': self.deleted
        }

    def revise(self, user, **new_post_data):
        revision = PostRevision(post_id=self.id,
                                title=self.title,
                                body=self.body,
                                deleted=self.deleted,
                                user_id=user.id)
        for key, value in new_post_data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self, revision

    def __repr__(self):
        return '<Post(%r) by %r %s>' % (self.id, self.user.name, "(deleted)" if self.deleted else "")
