import logging
logging.basicConfig(filename ="tupleHomework.log", level = logging.DEBUG, format ="%(asctime)s %(levelname)s %(message)s")


class tuple_t:
    def __init__(self,b):
        logging.info("only for tuple")
        self.b = b

    def extract_tuple(self):
        try:
            logging.info("Extracting tuples from the collection")
            for i in self.b:
                if type(i) == tuple:
                    logging.info(i)
        except Exception as e:
            logging.error(e)

tupleObj = tuple_t(b = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":"kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
tupleObj.extract_tuple()