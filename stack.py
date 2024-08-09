class create_stack:
    def __init__(self):
        global stack
        self.stack =[]
        
    def __repr__(self):
        return print(self.stack)
    
    def insert(self):
        value_append_in_stack = input("Entar a Value :")
        self.stack.append(value_append_in_stack)

    def user_input(self):
        while True:
            print("\n1-Inser a element .")

            user_input = input("Entar your choice ..")

            if user_input == "1":
                self.insert()
                self. __repr__()

stack = create_stack()
stack.user_input()
