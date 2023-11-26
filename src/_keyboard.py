import string

class Keyboard:

    @staticmethod
    def characters():
        return list(string.ascii_letters)
    
    @staticmethod
    def symbols():
        return list(string.punctuation)
    
    @staticmethod
    def numbers():
        return list(string.digits)
    