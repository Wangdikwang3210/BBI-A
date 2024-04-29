class PAM:
    _name= None
    def __init__ (self,name):
        self.name = name
    def _displayname(self):
        print (self.name)

class PAM_dc(PAM):
    def __init__ (self,name):
        PAM.__init__(self,name)
    def displayD(self):
        self._displayname()

obj = PAM_dc("BIA101")
obj.displayD()