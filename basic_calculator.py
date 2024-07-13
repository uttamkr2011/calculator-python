class Calculator:
    
    def __init__(self):
        self.num_1 = 0
        self.num_2 = 0

        self.menu()

    def menu(self):
        print("Please choose your operation number: ")
        print("1. Addtion\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")

        user_input = input("Enter here: ")

        if user_input.isdigit():
            user_input = int(user_input)

            if user_input == 1:
                self.add()
            elif user_input == 2:
                self.sub()
            elif user_input == 3:
                self.mul()
            elif user_input == 4:
                self.div()
            elif user_input == 5:
                print("Bye, Thank you!")
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
                self.menu()
            
        else:
            print("Please enter valid operation number.")
            self.menu()

    # Addition
    def add(self):
        print("=================\n")
        num_1 = input("First num: ")
        num_2 = input("Second num: ")

        try:
            int_num_1 = int(num_1)
            int_num_2 = int(num_2)

            print("=================\n")
            print(f"Addition: {int_num_1 + int_num_2}\n")

            self.menu()
        
        except ValueError:
            try:
                float_num_1 = float(num_1)
                float_num_2 = float(num_2)

                print("=================\n")
                print(f"Addition: {float_num_1 + float_num_2:.1f}\n")

                self.menu()
            
            except ValueError:
                print("=================")
                print("Please enter correct number.")
                print("=================\n")
                self.menu()

    
    # Subtraction
    def sub(self):
        print("=================\n")
        num_1 = input("First num: ")
        num_2 = input("Second num: ")

        try:
            int_num_1 = int(num_1)
            int_num_2 = int(num_2)

            print("=================\n")
            print(f"Subtraction: {int_num_1 - int_num_2}\n")

            self.menu()
        
        except ValueError:
            try:
                float_num_1 = float(num_1)
                float_num_2 = float(num_2)

                print("=================\n")
                print(f"Subtraction: {float_num_1 - float_num_2:.1f}\n")

                self.menu()
            
            except ValueError:
                print("=================")
                print("Please enter correct number.")
                print("=================\n")
                self.menu()

    
    # Multiplication
    def mul(self):
        print("=================\n")
        num_1 = input("First num: ")
        num_2 = input("Second num: ")

        try:
            int_num_1 = int(num_1)
            int_num_2 = int(num_2)

            print("=================\n")
            print(f"Multiplication: {int_num_1 * int_num_2}\n")

            self.menu()
        
        except ValueError:
            try:
                float_num_1 = float(num_1)
                float_num_2 = float(num_2)

                print("=================\n")
                print(f"Multiplication: {float_num_1 * float_num_2:.2f}\n")

                self.menu()
            
            except ValueError:
                print("=================")
                print("Please enter correct number.")
                print("=================\n")
                self.menu()


    # Division
    def div(self):
        print("=================\n")
        num_1 = input("First num: ")
        num_2 = input("Second num: ")

        try:
            int_num_1 = int(num_1)
            int_num_2 = int(num_2)

            print("=================\n")
            print(f"Division: {int_num_1 / int_num_2:.2f}\n")

            self.menu()
        
        except ValueError:
            try:
                float_num_1 = float(num_1)
                float_num_2 = float(num_2)

                print("=================\n")
                print(f"Division: {float_num_1 / float_num_2:.2f}\n")

                self.menu()
            
            except ValueError:
                print("=================")
                print("Please enter correct number.")
                print("=================\n")
                self.menu()


cal = Calculator()
