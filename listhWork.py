import logging
logging.basicConfig(filename ="listHomework.log", level = logging.DEBUG, format ="%(asctime)s %(levelname)s %(message)s")


class list_s:


    def __init__(self,l1,l2):
        logging.info('list Constructor is called         ')
        self.l1 = l1
        self.l2 = l2

    def extract_list(self):
        """ Extract list from the collection """
        try:
            for i in self.l1:
                if type(i) == list:
                    logging.info(i)
        except Exception as e:
            logging.error(e)

    def findOddFromList(self):
        """ Find odd number from a list"""
        try:
            logging.info("find out all the odd values from a list ")
            for i in self.l1:
                if type(i) == list:
                    for j in i:
                        if type(j) == int:
                            if j%2 != 0:
                                logging.info(j)
        except Exception as e:
            logging.error(e)

    def reverseAList(self):
        try:
            logging.info("Reversing list without for looping")
            return self.l2[:-1]
        except Exception as e:
            logging.error(e)

    def exttact234fromlist(self):
        try:
            logging.info("Extracting 234  from list")
            return sef.l2[7][0]
        except Exception as e:
            logging.error(e)

    def extract456fromlist(self):
        try:
            logging.info("extracting 434 from the list")
            return self.l2[5][1]
        except Exception as e:
            logging.error(e)

    def extractOnlyList(self):

        try:
            logging.info('extract List 1 from the collection without for loop')
            logging.info(self.l2[5])
            logging.info('extract List 2 from the collection without for loop')
            logging.info(self.l2[6])
            logging.info('extract List 3 from the collection without for loop')
            logging.info(self.l2[8][234])
        except Exception as e:
            logging.error(e)

    def extractnumericvalue(self):
        try:
            logging.info("extracting only numeric value from the collection")
            for i in self.l1:
                if type(i) == dict:
                    for j in i:
                        if type(j) == int:
                            logging.info(j)
                        if type(i[j]) == int:
                            logging.info(i[j])
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for k in i:
                        if type(k) == int:
                            logging.info(k)
                elif type(i) == int:
                    logging.info(i)
        except Exception as e:
            logging.error(e)

    def sum_of_all_numeric_value(self):
        try:
            logging.info("try to do sum opf all numeric value")
            a = 0
            for i in self.l1:
                if type(i) == dict:
                    for b in i.keys():
                        if type(b) == int:
                            a = a + b
                        if type(i[b]) == int:
                            a = a + b
                if type(i) == list or type(i) == tuple or type(i) == set:
                            for k in i:
                                if type(k) == int:
                                    a = a + k
                elif type(i) == int:
                    a = a + j

            return a
        except Exception as e:
            logging.error(e)

    def extract_ineuron(self):
        try:
            logging.info("trying to extract ineuron from the collection")
            for i in self.l1:
                if type(i) == dict:
                    for j in i.keys():
                        if type(j) == str:
                            if j == 'ineuron':
                                logging.info(j)
                        if type(i[j]) == str:
                            if (i[j]) == 'ineuron':

                                logging.info(i[j])
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for k in  i:
                        if k == 'ineuron':
                            logging.info(k)
                elif type(i) == str:
                    if i == 'ineuron':
                        logging.info(i)
        except Exception as e:
            logging.error(e)

    def occurance_of_number_from_collection(self):
        try:
            logging.info("trying to find out all the occurance of number from the collection")
            l3 = []

            for i in self.l1:
                if type(i) == dict:
                    for j in i.keys():
                        if type(j) == int or type(j) == str:
                            l3.append(j)
                        if type(i[j]) == int or type(i[j])== str:
                            l3.append(i[j])
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for k in i:
                        if type(k) == int or type(k) == str:
                            l3.append(k)
                elif type(i) == int or type(i) == str:
                            l3.append(i)

            for i in set(l3):
                logging.info('{0:{1}',format(i,l3.count(i)))
        except Exception as e:
            logging.error(e)

    def extract_alpha_num(self):
        try:
            logging.info("try to extrac al alpha numeric value")
            l4 = []
            for i in self.l1:
                if type(i) == dict:
                    for j in i.keys():
                        if type(j) == str:
                            if j.isalnum():
                                l4.append(j)
                        if type(i[j]) == str:
                            if (i[j]).isalnum():
                                l4.append(i[j])
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for k in i:
                        if type(k) == str:
                            l4.append(k)
                elif type(i) == str:
                    if i.isalnum():
                        l4.append(i)

            return l1
        except Exception as e:
            logging.error(e)

    def multiplication_of_all_numeric_collection(self):
        try:
            logging.info("trying to do multiplication of all numeric value")
            c = 1
            for i in self.l1:
                if type(i) == dict:
                    for j in i.keys():
                        if type(j) == int:
                            c = c*j
                        if type(i[j]) == int:
                            c = c*(i[j])
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for k in i:
                        if type(k) == int:
                            c = c*k
                elif type(i) == int:
                    c = c*i

            return c

        except Excetion as e:
            logging.error(e)














list_var = list_s([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),{'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]],
                      [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),{"key1": "sudh", 234: [23, 45, 656]}])


logging.info(list_var.extract_list())
logging.info(list_var.findOddFromList())
logging.info(list_var.reverseAList())
logging.info(list_var.extractOnlyList())

