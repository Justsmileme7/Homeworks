from random import randint
def function ():
    def function_2():
        while True:
            try:
                number_from = input('Enter number from\n')
                number_to = input('Enter number to\n')
                int(number_from)
                int(number_to)
            except ValueError:
                print('Error: you enter not numbers, TRY AGAIN')
                function_2()
            if int(number_to) - int(number_from) >= 5 and int(number_to) - int(number_from) <= 30:
                a1 = randint((int(number_from)),(int(number_to)))
                a2 = randint((int(number_from)),(int(number_to)))
                a3 = randint((int(number_from)),(int(number_to)))
                list_random_numbers = [a1, a2, a3]
                set1 = set(list_random_numbers)
                while len(set1) <3:
                    set1.add(randint((int(number_from)),(int(number_to))))
                print(a1, a2, a3)
                print(set1)
            else:
                print('Try again and Enter range from 5 to 30 numbers')
                continue
            return set1
    list = function_2()

    def function_4():
        while True:
            def function_3():
                while True:
                    try:
                        x = input('Введите число 1\n')
                        if x == 'exit':
                            quit()
                        y = input('Введите число 2\n')
                        if y == 'exit':
                            quit()
                        z = input('Введите число 3\n')
                        if z == 'exit':
                            quit()
                        int(x)
                        int(y)
                        int(z)
                    except ValueError:
                        print('Error: you enter not numbers')
                    else:
                        break
                if x!=y and x!=z and y!=z:
                    list_numbers = [x,y,z]
                    print(x,y,z)
                    return list_numbers
                else:
                    print('Try again and enter diferent numbers')
                    return function_3()
            count = 0
            for i in function_3():
                if int(i) in list:
                    count = count+1
                if count == 3:
                    print('You win!')
                    exit()
            else:
                print('Try again')
            print("You guessed", count, 'numbers')
    function_4()
function ()