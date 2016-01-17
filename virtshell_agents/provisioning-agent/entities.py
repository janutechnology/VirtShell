""" Filename: entities
    Description: Different entities of the agent
    moduleauthor: Carlos Alberto Llano R. <carlos_llano@hotmail.com> 
"""

################################################################################
# Request Class
################################################################################
class Request(object):    
    def __init__(self, id, message, status, date):
        self._id = id
        self._message = message
        self._status = status
        self._date = date
        self._message_log = None

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value
    
    @property
    def message(self):
        return self._message
    @message.setter
    def message(self, value):
        self._message = value

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        self._status = value

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        self._date = value

    @property
    def message_log(self):
        return self._message_log
    @date.setter
    def message_log(self, value):
        self._message_log = message_log