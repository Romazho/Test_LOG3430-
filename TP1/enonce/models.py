from datetime import datetime
class Contact:

    # Pour permettre un constructeur à 3 arguments, on regarde si les 3 premiers arguments sont non nuls et que les autres sont nuls
    def __init__(self, id = None, first_name = None, last_name = None, phone = None, mail = None, updated = None, updated_date = None, pay = None):
        if id is not None and first_name is not None and last_name is not None and phone is None and mail is None and updated is None and updated_date is None and pay is None:
            self.first_name = id
            self.last_name = first_name
            self.pay = last_name
        else:
            self.id = id
            self.first_name = first_name
            self.last_name = last_name
            self.pay = pay
            self.phone = phone
            self.mail = mail
            self.updated = bool(updated)
            self.updated_date = updated_date

    def __str__(self):
        return '''{self.first_name} {self.last_name} has {self.phone} and {self.mail}.
        This information is updated on {}'''.format(datetime.fromtimestamp(self.updated_date),self=self)
    
    # Le email @property retourne une string formatée (représentant email) comme suit: "first_name.last_name@polymtl.ca"
    @property
    def email(self):
        print(self.first_name)
        print(self.last_name)
        return "{0}.{1}@polymtl.ca".format(self.first_name, self.last_name)
    
    # Le fullname @property retourne une string formatée (représentant fullname) comme suit: "first_name last_name"
    @property
    def fullname(self):
        return "{0} {1}".format(self.first_name, self.last_name)
    
    # apply_raise augmente pay de 5%
    def apply_raise(self):
        self.pay *= 1.05
    