import os, sys
import codecs
import json

from forum.message import Message
from forum.member import Member


def get_forum_messages(fname='data/raw_data/otkn_messages.json', sDate=None, eDate=None):
    messages = json.loads(open(fname,'r').read().replace('\\','\\\\'), strict=False)
    for m in messages:
        mObj = Message(m)

        if sDate <> None and sDate > mObj.timestamp:
            continue

        if eDate <> None and eDate < mObj.timestamp:
            continue

        yield mObj

def get_message_dict(sDate=None, eDate=None):
    messages = get_forum_messages(sDate=sDate, eDate=eDate)
    return {m.id:m for m in messages if m.id <> None}



def get_forum_members(fname='data/raw_data/otkn_members.json'):
    members = json.loads(open(fname,'r').read().replace('\\','\\\\'), strict=False)
    for m in members:
        yield Member(m)

def get_member_dict():
    members = get_forum_members()
    return {m.id:m for m in members if m.id <> None}


if __name__ == '__main__':
    '''
    for m in get_forum_members():
        print m
        break
    '''

    testMsg = '''[quote author=Ahmet link=topic=1111.msg11111#msg11111 date=1430514875]
                    Ahmetin mesaji Ahmetin mesaji Ahmetin mesaji
                    [quote author=Ahmet2 link=topic=2222.msg22222#msg22222 date=1430514875]
                    Ahmet2nin mesaji
                    [/quote]
                    [/quote]
                    [quote author=Mehmet link=topic=3333.msg33333#msg33333 date=1430514875]
                    Mehmetin mesaji
                [/quote]'''
    for i,m in enumerate(get_forum_messages()):
        #m.body = testMsg
        print i, m.parseMessage()
