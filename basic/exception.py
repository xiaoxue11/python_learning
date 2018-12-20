#exception   
#raise Exception('hyperdrive overload')
#AttributeError
#TypeError
#NameError
#KeyError
#IndexError
#ValueError
#SyntaxError
#ZeroDivisionError
#OSError
#if you want to define an exception class,the format should be below,inherit
class SomeCustomException(Exception): pass
#==========================工作原理============================================
#1.try的工作原理是，当开始一个try语句后，python就在当前程序的上下文中作标记，
#这样当异常出现时就可以回到这里，
#try子句先执行，接下来会发生什么依赖于执行时是否出现异常。
#1.1如果当try后的语句执行时发生异常，python就跳回到try并
#1.1.2执行第一个匹配该异常的except子句，异常处理完毕，
#1.1.3控制流就通过整个try语句（除非在处理异常时又引发新的异常）。
#1.2.1如果在try后的语句里发生了异常，却没有匹配的except子句，
#1.2.2异常将被递交到上层的try，或者到程序的最上层
#（这样将结束程序，并打印缺省的出错信息）。
#1.3.1如果在try子句执行时没有发生异常，python将执行else语句后的语句
#（如果有else的话），然后控制流通过整个try语句。
#capture exception:try/except/finally
while True:
    try:
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        print(x / y)
    except ZeroDivisionError:
        print("The second number can't be zero!")
    except TypeError:
        print('This is a string not number.')
#多个异常，用元组表示
    except (NameError,KeyError):
        print('There are some wrong.')
#将捕获的对象打印出来
    except (NameError,ValueError) as e:
        print(e)
#捕获所有的异常,后面什么都不加
    except:
        print('Invalid input. Please try again.')
#条件判断，正常时才执行else语句，异常就反复循环，直至输入正确的结果
    else:
        break
#finally与try相对应，异常时执行清理工作
    finally:
        print('Cleaning up:')




