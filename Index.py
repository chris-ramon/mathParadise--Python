import web
from models.Test import Test

render = web.template.render('templates/')

urls = (
    '/','index',
    '/welcome/', 'welcome',
    '/test/(\d)','test',
    '/result/(\d)','result'
)

app = web.application(urls,globals())

class index:
    '''main class index to handle the first request / '''
    def GET(self):
        return render.main_page()
        
class welcome:
    '''Obtains the name of the user'''
    def POST(self):        
        inputs = web.input()
        name = inputs.name
        return render.welcome(name)

class test:
    '''Handles the class Test that we imported from modules/Test.py '''
    def POST(self, number):  
        if int(number) == 1:
            newTest = Test()
            question = newTest.createTest(1)
            correctAnswer = newTest.answer
            return render.test(question,correctAnswer,int(number))
            
        elif int(number) == 2:
            newTest = Test()
            question = newTest.createTest(2)
            correctAnswer = newTest.answer
            return render.test(question,correctAnswer,int(number))
        
class result:
    '''Handles the result of the answers'''
    def POST(self, number):        
        inputs = web.input()
        answer = inputs.answer
        correctAnswer = inputs.correctAnswer
        if answer==correctAnswer:            
            return render.result('Well done!', int(number))
        else:            
            return 'Wrong answer'        
        

if __name__=='__main__':
    app.run()

