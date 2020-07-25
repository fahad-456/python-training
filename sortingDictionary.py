import datetime
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')#This is an info message



def sortingDict(dict_a):#function to sort dictionary

    logger = logging.getLogger('palindromes of given list')
    logger.debug("input list '%s'",  dict_a)
    dict_b={}

    try:#use anonymous function to sort dictionary by age>10.
        dict_b = list(filter(lambda x: x['age']>10, dict_a))
        logging.info("list contain sorted dictionary'%s'",dict_b)
       
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)   
    return dict_b

def main():#Main function
    dict_a = [{'name': 'John', 'age': 12},

         {'name': 'Sonia', 'age': 10},

         {'name': 'Steven', 'age': 13},

         {'name': 'Natasha', 'age': 9}]
    print(dict_a)#print original dictionary
    modified_data = sortingDict(dict_a)
    print(modified_data)#print sorted dictionary

if __name__ == "__main__":
    main()


