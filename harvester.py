import sys
import zulip
import requests
import json
import time


# Keyword arguments 'email' and 'api_key' are not required if you are using ~/.zuliprc
client = zulip.Client(email="Mafia-bot@students.hackerschool.com",
                      api_key="ynj6gS3cxyMyGX25lYkLopBUqhOILjEK")


# An interesting question is how to write the function
# It is pretty clear that I am going to have to make a second copy of this
# function to handle the case where I want to harvest all senders instead
# of all streams
# The question is, how many ways can I do that? Obviously, copying and pasting
# is one but that is less than ideal. So how many ways can I create one function
# that handles either task in an elegant way?
def harvest_stream(stream_name):
    anchor = 0
    num_before = 0
    num_after = 100000000000
    response = client.do_api_query({'anchor':anchor,
                                    'num_before': num_before,
                                    'num_after': num_after,
                                    #'narrow': [['sender', sender]]},
                                    'narrow': [['stream', stream_name]]},
                                    'https://zulip.com/api/v1/messages',
                                     method='GET'
                                    )
    if response['result'] == 'success':
        return response['messages']

    else:
        return None

def harvest_sender(sender):
    anchor = 0
    num_before = 0
    num_after = 100000000000
    response = client.do_api_query({'anchor':anchor,
                                    'num_before': num_before,
                                    'num_after': num_after,
                                    'narrow': [['sender', sender]]},
                                    'https://zulip.com/api/v1/messages',
                                     method='GET'
                                    )
    if response['result'] == 'success':
        return response['messages']
    else:
        return None


def save_json(filename, data):
    with open(filename, 'wb') as outfile:
        json.dump(data, outfile)


def load_json(filename):
    with open(filename) as infile:
        data = json.load(infile)
    return data


if __name__ == '__main__':
    #do smart stuff here
    #Should harvest via streams and the harvest by list of users
    #and compare the results to see how they differ in number of messages
    #Also, am I going to get private messages, at least acknowledgement
    #of their existence instead of getting actual content?

    response = client.register()
    assert response['result']=='success', 'Error with client registration!'

    #create list of all available streams
    streams = response['streams']
    stream_names = [s['name'] for s in streams]
    print(len(stream_names))

    messages = {}
    for s in stream_names:
        print(s)
        m = harvest_stream(s)

        if messages is not None:
            messages[s] = m

        time.sleep(5)

    save_json('messages_by_stream.json', )
