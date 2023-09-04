import email
from itertools import count
from flask import render_template, request, redirect, url_for, jsonify
from app import app, db
from app.models import Channel, User, Chat, UserConversationDetails, ChannelUser, UserOverall
from app.sentiment_analysis_helper import SentimentAnalyzer
from datetime import datetime
import json
analyzer = SentimentAnalyzer()


@app.route('/test', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_email = request.form.get('email')
        user_info = User.query.filter_by(email=user_email).first()
        return render_template('index.html', user_info=user_info)
    return render_template('index.html', user_info=None)


@app.route('/', methods=['GET'])
def manage_users():
    users = User.query.all()
    users_with_stats = []
    for user in users:
        chats = Chat.query.filter(Chat.user_email == user.email).all()
        channels_chatted_with = set(chat.channel_id for chat in chats)
        total_positive = 0
        total_negative = 0
        total_neutral = 0
        private_chats = 0
        public_chats = 0
        for channel in channels_chatted_with:
            channel_details = Channel.query.get(channel)
            if channel_details:
                # chat_in_channel = [x for x in chats if x.channel_id == channel]
                channel_type = channel_details.type
                total_positive = total_positive + len([x for x in chats if x.channel_id == channel and x.sentiment == 'POSITIVE'])
                total_negative = total_negative + len([x for x in chats if x.channel_id == channel and x.sentiment == 'NEGATIVE'])
                total_neutral = total_neutral + len([x for x in chats if x.channel_id == channel and x.sentiment == 'NEUTRAL'])
                if channel_details.type == 'private':
                    private_chats = private_chats + len([x for x in chats if x.channel_id == channel])
                else:
                    public_chats = public_chats + len([x for x in chats if x.channel_id == channel])
        chat_total = total_positive + total_negative + total_neutral
        user_stats = UserOverall(email=user.email, name=user.name, age=user.age, title=user.title, job_description=user.job_description, supervisor=user.supervisor, negative_total=total_negative,
        positive_total=total_positive, neutral_total=total_neutral, total_chats=chat_total, private_chats=private_chats, public_chats=public_chats)
        users_with_stats.append(user_stats)
        print(user_stats.toJSON())
    
    return render_template('manage_users.html', users=users_with_stats)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        age = int(request.form['age'])
        title = request.form['title']
        job_description = request.form['job_description']
        supervisor = request.form['supervisor']

        new_user = User(email=email, name=name, age=age, title=title, job_description=job_description, supervisor=supervisor)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('manage_users'))

    return render_template('add_user.html')

@app.route('/chat', methods=['POST'])
def create_chat():
    data = request.json  # Get JSON data from the request body

    # Extract fields from the JSON data
    channel_id = data.get('channel_id')
    user_email = data.get('user_email')
    text = data.get('text')

    print(channel_id)

    if channel_id is None or user_email is None or text is None:
        return jsonify({'error': 'Missing required fields'}), 400

    # Create a new chat and add it to the database
    sentiment = analyzer.analyze_sentiment(text)[0].get('label').upper()
    new_chat = Chat(user_email = user_email, channel_id = channel_id, sentiment = sentiment, created_date = datetime.utcnow())
    print(new_chat)
    db.session.add(new_chat)
    db.session.commit()

    return jsonify({'message': 'Chat added successfully'}), 200


@app.route('/user/<string:user_email>', methods=['GET'])
def user_profile(user_email):
    user = User.query.filter_by(email=user_email).first()
    if user is None:
        return "User not found", 404

    chats = Chat.query.filter(Chat.user_email == user_email).all()
    channels_chatted_with = set(chat.channel_id for chat in chats)
    chatted_with = []
    for channel in channels_chatted_with:
        channel_details = Channel.query.get(channel)
        if channel_details:
            # chat_in_channel = [x for x in chats if x.channel_id == channel]
            positive_count = len([x for x in chats if x.channel_id == channel and x.sentiment == 'POSITIVE'])
            negative_count = len([x for x in chats if x.channel_id == channel and x.sentiment == 'NEGATIVE'])
            neutral_count = len([x for x in chats if x.channel_id == channel and x.sentiment == 'NEUTRAL'])
            chat_total = positive_count + negative_count + neutral_count
            if channel_details.type == 'private':
                dm_user = ChannelUser.query.filter(ChannelUser.channel_id == channel).filter(ChannelUser.user_email != user_email).first()
                conversation = UserConversationDetails(user_email=user_email, negative_rate=negative_count/chat_total*100, positive_rate=positive_count/chat_total*100
                ,neutral_rate=neutral_count/chat_total*100, channel_id=channel, channel_name=channel_details.name, channel_type=channel_details.type, chat_with=dm_user.user_email,total_chats=chat_total)
                chatted_with.append(conversation)
            else:
                conversation = UserConversationDetails(user_email=user_email, negative_rate=negative_count/chat_total*100, positive_rate=positive_count/chat_total*100
                ,neutral_rate=neutral_count/chat_total*100, channel_id=channel, channel_name=channel_details.name, channel_type=channel_details.type, chat_with=channel_details.name,total_chats=chat_total)
                chatted_with.append(conversation)

    return render_template('user_profile.html', user=user, chatted_with=chatted_with)
