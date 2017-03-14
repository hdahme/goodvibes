import logging
import settings

from mailchimp3 import MailChimp
from flask import Flask, render_template, request


app = Flask(__name__)
client = MailChimp(settings.MAILCHIMP_USER, settings.MAILCHIMP_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribed', methods=['POST'])
def subscribed():
    return render_template('subscribed.html')

    first_name = request.form['first-name']
    last_name = request.form['last-name']
    email = request.form['user-email']

    client.lists.members.create('fc1aa56de1', {
        'email_address': email,
        'status': 'subscribed',
        'merge_fields': {
            'FNAME': first_name,
            'LNAME': last_name,
        },
    })

    return render_template(
        'subscribed.html',
        fname=first_name
    )


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
