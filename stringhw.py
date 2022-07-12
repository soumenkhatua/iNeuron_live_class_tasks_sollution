import logging
logging.basicConfig(filename = "string_hw.log",level = logging.DEBUG,format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')

class strclass:

    def __init__(self,str_s):
        logging.info("String operation ")
        self.str_s = str_s

    def extractdatafromstring(self):
        try:
            logging.info("extracting string frm index one to another index")
            return self.str_s[0:300:3]
        except Exception as e:
            logging.error(e)

    def reversestring(self):
        try:
            logging.info("revesing string without using reverse function")
            return self.str_s[::-1]
        except Exception as e:
            logging.error(e)

    def upperthensplit(self):
        try:
            logging.info("split a string after conversion of entire string in uppercase")
            return self.str_s.upper().split("   ")

        except Exception as e:
            logging.error(e)

    def wholestringintolowerclass(self):
        try:
            logging.info("trying to convert whole string into lower class")
            return self.str_s.lower()
        except Exception as e:
            logging.error(e)

    def capitalizestr(self):
        try:
            logging.info("trying to capitalize the whole string")
            return self.str_s.capitalize()
        except Exception as e:
            logging.error(e)

    def isitalphanum(self):

        try:
            logging.info("trying to check alpha numeric in string")
            return self.str_s.isalnum()
        except Exception as e:
            logging.error(e)

    def isitalpha(self):
        try:
            logging.info('checking alphabet in string')
            return self.str_s.isalpha()
        except Exception as e:
            logging.error(e)

    def Strexpandtab(self, str):
        try:
            logging.info('expand tab is performing on a string')
            return str.expandtabs()
        except Exception as e:
            logging.error(e)

    def trim(self):
        try:
            logging.info('removing space around str')
            return self.str_s.strip()
        except Exception as e:
            logging.error(e)

    def lefttrim(self):
        try:
            logging.info('removing space left of str')
            return self.str_s.lstrip()
        except Exception as e:
            logging.error(e)

    def righttrim(self):
        try:
            logging.info('removing space right of str')
            return self.str_s.rstrip()
        except Exception as e:
            logging.error(e)

    def Strreplace(self, sentence, str1, str2):
        try:
            logging.info('Replacing a string character by another character')
            return sentence.replace(str1, str2)
        except Exception as e:
            logging.error(e)

    def Strcenter(self, str):
        try:
            logging.info('performing string center function')
            return str.center(18, '@')
        except Exception as e:
            logging.error(e)


strobj = strclass("         this is My First Python programming class and i am learNING python string and its function        ")
logging.info(strobj.extractdatafromstring())
logging.info(strobj.reversestring())
logging.info((strobj.upperthensplit()))
logging.info(strobj.wholestringintolowerclass())
logging.info(strobj.capitalizestr())
logging.info(strobj.isitalphanum())
logging.info(strobj.isitalpha())
logging.info(strobj.Strexpandtab("I am a big\t fan of\t you sir"))
logging.info(strobj.trim())
logging.info(strobj.lefttrim())
logging.info(strobj.righttrim())
logging.info(strobj.Strreplace('soumen','ineuron','fsds'))
logging.info(strobj.Strcenter('Soumen Khatua'))