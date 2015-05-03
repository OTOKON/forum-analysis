import re
import json


class Message(object):
    
    def __init__(self, data=None):
        if isinstance(data, str):
            data = json.loads(data)

        self.id = data.get('id_msg',None)
        self.topic = data.get('id_topic', None)
        self.board = data.get('id_board', None)
        self.member = data.get('id_member', None)
        self.timestamp = data.get('poster_time',None)
        self.body = data.get('body','')

        self.raw = data # Just in case we might need other fields too

        self.parseRules = {'quote': self.__parseQuote} # Functions to extract specific tag

    def parseMessage(self, fields=['quote']):
        parsed = dict()
        for f in fields:
            pfunc = self.parseRules[f]
            parsed[f] = pfunc(self.body)

        return parsed


    def __parseQuote(self, msgStr):
        # Find [quote and [/quote]
        sTag = [s.start() for s in list(re.finditer('\[quote', msgStr))]
        eTag = [s.start() for s in list(re.finditer('\[\/quote]', msgStr))]
        #print sTag, eTag

        tIndex = dict()
        for i, t in enumerate(sTag):
            tIndex['s{}'.format(i)] = t
        for i, t in enumerate(eTag):
            tIndex['e{}'.format(i)] = t

        # Decide the depth of each quote and get the ones on top
        topTags = list()
        temp = 0
        sortedTags = sorted(tIndex.items(), key=lambda x:x[1])
        for k,v in sortedTags:
            if k.startswith('s'):
                if temp == 0:
                    topTags.append(k)
                temp += 1
            elif k.startswith('e'):
                temp -= 1
                pass
            else:
                print 'WTF!'

        #print [(tIndex[t], t) for t in topTags]
        parsed = list()
        for t in topTags:
            temp = {'message_id':None, 'topic_id':None}
            next = tIndex[t]

            try:
                for i,s in enumerate(sortedTags):
                    if s[0] == t:
                        next = sortedTags[i+1][1]
                        break 
            except:
                print 'Warning: Quote mistake'
                continue


            # Collect the topic & message id topic=XXXX.msgXXXXX
            quote = msgStr[tIndex[t]:next]
            if ('msg' not in quote) or ('topic' not in quote):
                continue # Just quoting some text not an user message   

            try:
                temp['topic_id'] = int(re.search('topic=(.*?).msg', quote).group(1))
            except:
                print msgStr
                print 'Cant find topic_id'

            try:
                temp['message_id'] = int(re.search('.msg(.*?)#', quote).group(1))
            except:
                print msgStr
                print 'Cant find message_id'

            parsed.append(temp)

        return parsed

    def __repr__(self):
        return json.dumps(self.raw)
