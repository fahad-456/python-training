
import datetime
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')#This is an info message

def palindrome(input_list):
    """this function returns palindrome from the given list"""

    logger = logging.getLogger('palindromes of given list')
    logger.debug("input list '%s'",  input_list)
    out_list=[]

    try:
        #use anonymous function to filter palindromes.
        """we call a function to reverse a string, which iterates to every element and intelligently join each character in the beginning so as to obtain the reversed string."""

        out_list = list(filter(lambda x: (x.lower() == "".join(reversed(x.lower()))), input_list))
        logging.info("list contain palindromes'%s'",out_list)
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)   
    return out_list

 
  



