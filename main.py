"""
Module Docstring
"""
import re

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    # Main entry point of the app
    print("what's popping? i am a string calculator.")

#Function to get the number list from the string
def get_number_list(input):

    if input[:2] == '//': #for custom delimeter

        input_list = input.split('\n')
        pattern_string = input_list[0][2:]

        str_nums = re.split(pattern_string, input_list[1])
        
    else: #for comma and new line as delimeters
        str_nums = re.split(',|\n', input)

    return str_nums

#Function to handle negative values in the input
def negatives_handler(negatives):
    res = "negatives not allowed: "
    if len(negatives) != 1:
        for neg in negatives:
            res = res + str(neg) + " "

    else:
        res += str(negatives[0])
    
    return res

def sum(input):
    if len(input) != 0:
        
        str_nums = get_number_list(input)

        numbers = []
        negatives = []

        for i in str_nums:
            n = int(i)
            if n > 0:
                numbers.append(n)
            else:
                negatives.append(n)
                
        s = 0
        
        if len(negatives) != 0:
            result = negatives_handler(negatives)

            return result

        else:
            for num in numbers:
                s+=num
                
            return s           
            
    return 0


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
