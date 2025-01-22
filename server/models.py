from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

# MetaData naming convention for foreign keys
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# Initialize SQLAlchemy with the custom metadata
db = SQLAlchemy(metadata=metadata)

# Message model with SerializerMixin
class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    # Defining the columns for the Message table
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(500), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # SerializerMixin will automatically use these fields for serialization
    serialize_only = ('id', 'body', 'username', 'created_at', 'updated_at')

    def __repr__(self):
        return f"<Message {self.id} - {self.body}>"
