import sys  # this allows you to use the sys.exit command to quit/logout of the application
import time
import turtle
import os


def main():
    def menu():
        print("***********MENU**************")
        # time.sleep(1)
        print()

    choice = input("""
                      A: Play Games
                      B: Learn Specific Topics
                      C: Calculators
                      D: Create Graph
                      Q: Quit/Log Out

                      Please enter your choice: """)

    if choice == "A" or choice == "a":
        games()
    elif choice == "B" or choice == "b":
        learn()
    elif choice == "C" or choice == "c":
        calc()
    elif choice == "D" or choice == "d":
        graph()
    elif choice == "Q" or choice == "q":
        sys.exit
    else:
        print("You must only select either A,B,C, or D.")
        print("Please try again")
        menu()


def games():
    choice = input("""
                       A: Name the triangle!!!
                       B: Hangman!!!
                       C: Quiz  .-.
                       Q: Quit/Log Out

                       Please enter your choice: """)

    if choice == "A" or choice == "a":
        triangle_g()
    elif choice == "B" or choice == "b":
        hangman()
    elif choice == "C" or choice == "c":
        quiz()

    elif choice == "Q" or choice == "q":
        menu()
    else:
        print("You must only select either A,B,C, or D.")
        print("Please try again")
        game()


def triangle_g():
    screen = turtle.getscreen()
    turtle.title("My little turtle")
    lilt = turtle.Turtle()

    turtle.bgcolor("grey")

    u = input("Would you like me to draw a shape? Type yes or no: ")
    if u == "yes":
        lilt.speed(1)
        lilt.goto(-100, -100)
        lilt.goto(90, -100)
        ## lilt.home()
        time.sleep(5)
        lilt.reset()

        q1 = input("What type of angle was printed?   ")
        if q1 == "Accute" or "accute" or "an accute angle" or "Accute angle":
            print("Good Job")
            time.sleep(2)

            lilt.speed(1)
            lilt.goto(-100, 100)
            lilt.goto(0, 0)
            lilt.goto(90, 0)
            ## lilt.home()
            time.sleep(5)

            q2 = input("What type of angle was printed?   ")
            if q2 == "Obtuse" or "obtuse" or "an obtuse angle" or "Obtuse angle":
                print("Good Job")
                time.sleep(5)


        else:
            print("Incorrect Answer")
            time.sleep(5)
            triangle_g()


def learn():
    choice = input("""Choose a topic:
                          A: Trigonometry
                          B: Matrix Operation
                          C: Calculus
                          D: Statistics
                          Q: Quit/Log Out

                          Please enter your choice: """)

    if choice == "A" or choice == "a":
        trig()
    elif choice == "B" or choice == "b":
        matrix()
    elif choice == "C" or choice == "c":
        calculus()
    elif choice == "D" or choice == "d":
        stats()
    elif choice == "Q" or choice == "q":
        sys.exit
    else:
        print("You must only select either A,B,C, or D.")
        print("Please try again")
        menu()


def trig():
    os.system('cls')

    print("""


                                              Trigonometry

                                Trigonometry is a branch of mathematics that
                                focuses on relationships between the sides and
                                angles of triangles.

                                The word trigonometry comes from the Latin derivative of Greek words 
                                for triangle (trigonon) and measure (metron)


                                Concerned with relations involving angles, which
                           are best expressed by means of six trigonometric functions


                                Trigonometry may be described as a study of these
                                            functions and their uses""")

    choice = input("""What do specifically do you want know?

                       1. Angles
                       2. Identities
                       3. Proving Identities
                       4. None   
                """)
    if choice == "Angles" or choice == "angles" or choice == "1":
        # os.system('cls')
        print("""                         Angles

                                An angle as defined in plane geometry is a figure,
                                such as BAC in Figure 1 formed by two rays, AB
                                    and AC, with common end-point at A.



                        """)

        option = input("Do you want to continue? Yes or No ")
        if option == "yes" or option == "Yes":
            os.system('cls')
            print("""                 Right Triangle Trigonometry

                The sides of the right triangle are: the side opposite the acute angle θ,
                                                     the side adjacent to the acute angle θ,
                                                     and the hypotenuse of the right triangle.")
                                              """)

            f = open('cover.png', 'rb')

            newfile = open('newfile.jpg', 'wb')

            for line in f:
                newfile.write(line)

        elif option == "no" or option == "No" or option == "NO":
            os.system('cls')
            menu()

    elif choice == "Identities" or choice == "identities" or choice == "2":
        print("Identitiessssssss")
    elif choice == "proving identities" or choice == "Proving Identities" or choice == "3":
        print("More identitiessssssss")
    elif choice == "4" or choice == "none" or choice == "None":
        menu()

main()


def calc():
    pass


def hangman():
    pass


def graph():
    pass


def game():
    pass


def menu():
    pass


main()
