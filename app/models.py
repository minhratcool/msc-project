from app import db
import json

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(120), nullable=False)
    job_description = db.Column(db.String(250), nullable=False)
    supervisor = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'


class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Channel {self.name}>'

class ChannelUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), db.ForeignKey('user.email'), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'), nullable=False)

    def __repr__(self):
        return f'<ChannelUser {self.user_email} in Channel {self.channel_id}>'

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'), nullable=False)
    user_email = db.Column(db.String(120), db.ForeignKey('user.email'), nullable=False)  # You might replace this with a ForeignKey reference to a User table
    created_date = db.Column(db.DateTime, nullable=False)
    sentiment = db.Column(db.String(10), nullable = False)

    channel = db.relationship('Channel', lazy='select')

    def __repr__(self):
        return f'<Chat {self.id} from User {self.user_email} in Channel {self.channel_id}>'

class UserConversationDetails:
    def __init__(self, user_email, negative_rate, positive_rate, neutral_rate, channel_id, channel_name, channel_type, chat_with, total_chats):
        self.user_email = user_email
        self.negative_rate = negative_rate
        self.positive_rate = positive_rate
        self.neutral_rate = neutral_rate
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.channel_type = channel_type
        self.chat_with = chat_with
        self.total_chats = total_chats

class UserOverall:
    def __init__(self, email, name, age, title, job_description, supervisor, negative_total, positive_total, neutral_total, total_chats, private_chats, public_chats):
        self.email = email
        self.name = name
        self.age = age
        self.title = title
        self.job_description = job_description
        self.supervisor = supervisor
        self.negative_total = negative_total
        self.positive_total = positive_total
        self.neutral_total = neutral_total
        self.private_chats = private_chats
        self.public_chats = public_chats
        self.total_chats = total_chats

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

