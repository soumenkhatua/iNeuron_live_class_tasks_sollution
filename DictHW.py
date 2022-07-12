import logging
logging.basicConfig(filename="DictHomework.log" ,  level = logging.DEBUG, format ="%(asctime)s %(levelname)s %(message)s")

class  dictclass:

    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def exctractdictentity(self):
        try:
            logging.info("trying to extract all the dict entities")
            for i in self.l1:
                if type(i) == dict:
                    logging.info(i)

        except Exception as e:
            logging.error(e)

    def numberofkeyindict(self):
        try:
            logging.info("'tying to emitate no of keys in dict")
            keycount = 0
            for i in l1:
                if type(i) ==  dict:
                    for j in i.keys():
                        keycount += 1
            return keycount

        except Exception as e:
            logging.error(e)

    def extractsudh(self):
        try:
            logging.info("trying to extract sudh in dict without using using for loop")
            return self.l2[8]['key1']
        except Exception as e:
            logging.error(e)
    def valueexctarcting(self):
        try:
            logging.info("try to extract all the values from the dict without using for loop")
            logging.info('extracting first value ')
            logging.info(self.l2[8]['key1'])
            logging.info('extracting second value ')
            logging.info(self.l2[8][234])
        except Exception as e:
            logging.error(e)

dictobj = dictclass([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),{'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]],
                      [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),{"key1": "sudh", 234: [23, 45, 656]}])

logging.info(dictobj.extractsudh())
logging.info(dictobj.valueexctarcting())
logging.info(dictobj.numberofkeyindict())
logging.info(dictobj.exctractdictentity())