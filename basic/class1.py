class Person:
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def greet(self):
        print("Hell0,world! I'm {}".format(self.name))

class Calculator:
    def calculate(self,expression):
        self.value=eval(expression)

class Talker:
    def talk(self):
        print('Hi,my value is',self.value)
class TalkingCalculator(Calculator,Talker):
    pass

tc = TalkingCalculator()
#检查所需的函数和方法是否存在
hasattr(tc,'talk')
hasattr(tc,'fond')
#检查属性是否可以调用
callable(getattr(tc,'talk',None))
callable(getattr(tc,'fond',None))
#设置属性
setattr(tc, 'name', 'Mr. Gumby')
