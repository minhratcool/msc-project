from app import app, db
from app.models import Channel, ChannelUser, Chat, User
from datetime import datetime
import random

with app.app_context():
    # Create channels
    # channel1 = Channel(type='public', name='General')
    # channel2 = Channel(type='private', name='DM')
    # channel3 = Channel(type='private', name='DM1')
    # channel4 = Channel(type='private', name='DM2')
    # db.session.add_all([channel3, channel4])
    # db.session.commit()

    # # Create users
    # user1 = User(email='supervisor@google.com', name='Superman', age=50, title='Manager', job_description='Overlooking', supervisor='upper.supervisor@gmail.com')
    # user2 = User(email='johndoe@google.com', name='John Doe', age=28, title='Developer', job_description='Web Development', supervisor='supervisor@gmail.com')
    # user3 = User(email='alicejohnson@google.com', name='Alice Johnson', age=32, title='Designer', job_description='Graphic Design', supervisor='supervisor@gmail.com')
    # user4 = User(email='minh@google.com', name='Minh Tran', age=30, title='Data Engineer', job_description='Data Engineering', supervisor='supervisor@gmail.com')
    # db.session.add_all([user1, user2, user3, user4])
    # db.session.commit()

    # Associate users with channels
    # channel_user1 = ChannelUser(user_email='johndoe@google.com', channel_id=1)
    # channel1_minh = ChannelUser(user_email='minh@google.com', channel_id=1)
    # channel2_minh = ChannelUser(user_email='minh@google.com', channel_id=2)
    # channel3_minh = ChannelUser(user_email='minh@google.com', channel_id=3)
    # channel4_minh = ChannelUser(user_email='minh@google.com', channel_id=4)
    # channel1_alice = ChannelUser(user_email='alicejohnson@google.com', channel_id=1)
    # channel2_alice = ChannelUser(user_email='alicejohnson@google.com', channel_id=2)
    # channel3_john = ChannelUser(user_email='johndoe@google.com', channel_id=3)
    # channel4_supervisor = ChannelUser(user_email='supervisor@google.com', channel_id=4)
    # db.session.add_all([channel1_minh, channel2_minh,channel3_minh,channel4_minh,channel1_alice,channel2_alice,channel3_john,channel4_supervisor])
    # db.session.commit()

    # Create chats
    # sentiments = ['POSITIVE', 'NEGATIVE', 'NEUTRAL']
    # user_emails = ['johndoe@google.com', 'minh@google.com', 'alicejohnson@google.com','supervisor@google.com']
    # chats = []
    # for i in range(1000):
    #     chat1 = Chat(channel_id=random.choice(range(1, 5)), user_email='minh@google.com', created_date=datetime.utcnow(), sentiment=random.choice(sentiments))
    #     chats.append(chat1)
    # for i in range(500):
    #     chat1 = Chat(channel_id=random.choice(range(1, 3)), user_email='alicejohnson@google.com', created_date=datetime.utcnow(), sentiment=random.choice(sentiments))
    #     chats.append(chat1)
    # for i in range(500):
    #     chat1 = Chat(channel_id=random.choice([1,3]), user_email='johndoe@google.com', created_date=datetime.utcnow(), sentiment=random.choice(sentiments))
    #     chats.append(chat1)
    # for i in range(200):
    #     chat1 = Chat(channel_id=4, user_email='supervisor@google.com', created_date=datetime.utcnow(), sentiment=random.choice(sentiments))
    #     chats.append(chat1)
    # db.session.add_all(chats)
    # db.session.commit()
    user_email_to_delete = 'minhtn286@google.com'

    # Delete rows from ChannelUser where user_email matches
    rows_deleted = ChannelUser.query.filter_by(user_email=user_email_to_delete).delete()
    db.session.commit()

print("Data added to the database.")
