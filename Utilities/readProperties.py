import configparser

config=configparser.RawConfigParser()

config.read('.\\Configurations\\config.ini')

class ReadConfig():

    @staticmethod
    def getApplicationurl():
        url=config.get('common info', 'base_url')
        return url

    @staticmethod
    def getemail():
        email=config.get('common info', 'email')
        return email

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getuploadpath():
        path=config.get('common info', 'upload_path')
        return path
