import json

with open('secrets/mailchimp.json') as d:
    d = json.load(d)
    MAILCHIMP_USER = d.get('mailchimp_user')
    MAILCHIMP_KEY = d.get('mailchimp_key')
