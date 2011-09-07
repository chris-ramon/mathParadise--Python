import random

class Test:
    '''Represents a collection of numbers and dictionary of operator
    in order to create a simple exam using 4 operators.'''
    
    def __init__(self):
        '''Initialize a test with empty list of numbers and
        dictionary of operators, answer attribute will received the value from
        createTest function'''
        self.numbers = []
        self.operators = {1:'+', 2:'-', 3:'*', 4:'/'}
        self.answer = None
        
    def generateNumbers(self, numbers):
        '''Generate random numbers between 1 and 20.'''
        if numbers>0:
            while numbers>0:
                num = random.randint(1,20)
                self.numbers.append(num)
                numbers -= 1
        else:
            return None
    
    def createTest(self,exam=0,numbers=2):
        '''Create an exam, the givin exam is use to define which exam
        should the function create, the givin numbers is to define
        how many numbers the function generateNumbers should create'''
        self.generateNumbers(numbers)
        if exam==1:
            num = random.randint(1,2)
            operator = self.operators[num]
            test = str(self.numbers[0]) + operator + str(self.numbers[1])
            if operator=='+':
                self.answer = self.numbers[0]+self.numbers[1]
            elif operator=='-':
                self.answer = self.numbers[0]-self.numbers[1]
            return test
            
        elif exam==2:
            num = random.randint(3,4)
            operator = self.operators[num]
            test = str(self.numbers[0]) + operator + str(self.numbers[1])
            if operator=='*':
                self.answer = self.numbers[0]*self.numbers[1]
            elif operator=='/':
                self.answer = float(self.numbers[0])/float(self.numbers[1])            
            return test
            
        else:
            return 'Exam 1 or 2?'  

