def add(n1,n2):

    try:
        print(n1 + n2)
    except:
        print('something happened!')
    finally:
        print('function has been called')
    

number1 = 10
number2 = "30"

add(number1, number2)
def test_file():

    try:
        # should be "w"
        f = open('testfile', 'r')
        f.write("Write a test line")
    except OSError:
        print('Hey you have an OS Error')
    except:
        print('There was a error')
    finally:
        print('I always run')

test_file()