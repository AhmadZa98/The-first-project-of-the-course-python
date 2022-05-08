

from re import T


class PyCoursePro:

    def __init__(self):
        while True:
            print(''' Welecoom To Pythone Course app
                        Please choose the app you want to use:
                        1- List Type app
                        2- NumberOfWords app
                        3- NumberCounter app
                        4- NumberCounter2 app
                        5- NumberCounter3 app

                        (if you want to quit the program, please press the "X")

            ''')
            c = input()
            if c == "X":
                break
            if int(c) == 1:
                print('''Welecoom To List Type app

                        A app that takes a list of numbers and divides it into 2 lists,
                        one with even numbers And one that has the odd numbers and prints them
                    ''')
                self.List_type()

            elif int(c) == 2:
                print('''Welecoom To NumberOfWords app

                        A program that takes a sentence from the user and counts the number of words in the sentence from others Repetition
                    ''')
                self.NumberOfWords()

            elif int(c) == 3:
                print('''Welecoom To NumberCounter app

                        A program that takes a number from the user and prints the numbers from 0 to this number
                    ''')
                self.NumberCounter()

            elif int(c) == 4:
                print('''Welecoom To NumberCounter2 app

                        A program that takes two numbers from the user and prints all numbers that are divisible by
                        The second number from zero to the first number
                    ''')
                self.NumberCounter2()

            elif int(c) == 5:
                print('''Welecoom To NumberCounter3 app

                        A program that takes two numbers from the user and prints all numbers that are divisible by
                        My number is from 0 to 10
                    ''')
                self.NumberCounter3()

    def List_type(self):

        List1 = []
        Even_List = []
        Odd_List = []
        n = int(input("Enter Number of element: "))

        for x in range(1, n+1):
            e = int(input())
            List1.append(e)

        for y in List1:

            if y % 2 == 0:
                Even_List.append(y)

            else:
                Odd_List.append(y)
        print(f''' The main List = 
            {List1}''')
        print(f''' The Odd List = 
            {Odd_List}''')
        print(f''' The Even List = 
            {Even_List}''')

    def NumberOfWords(self):

        WordsList = []
        Words = input("plese enter your sentence").lower().split()
        for x in Words:
            if x not in WordsList:
                WordsList.append(x)
        print(len(WordsList))

    def NumberCounter(self):

        Number = int(input("Enter your number"))

        for x in range(0, Number + 1):

            print(x)

    def NumberCounter2(self):

        Number1 = int(input("Pleese Enter First Number"))
        Number2 = int(input("Pleese Enter Second Number"))

        for x in range(0, Number1 + 1):

            if x % Number2 == 0:
                print(x)

    def NumberCounter3(self):

        Number1 = int(input("Pleese Enter First Number"))
        Number2 = int(input("Pleese Enter Second Number"))

        for x in range(0, 101):

            if x % Number2 == 0 and x % Number1 == 0:
                print(x)


PyCoursePro()
