import json


class Member(object):
    
    def __init__(self, data=None):
        if isinstance(data, str):
            data = json.loads(data)
        self.id = data.get('id_member', None)
        self.number = data.get('kulup_no', None)
        self.name = data.get('member_name', None)
        self.realName = data.get('real_name', None)
        self.registration = data.get('date_registered', None)

        self.raw = data # Just in case we might need other fields too


    def __loadSurveyData():
        print 'Not implemented yet!'

    def __repr__(self):
        return json.dumps(self.raw)