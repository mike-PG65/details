class Person:
    def __init__(self, name, age, gender):
    
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        """
        Print an introduction message with the person's name, age, and gender.
        """
        print(f"Hello, my name is {self.name}. I am {self.age} years old and i am a {self.gender}.")

def main():
    # Prompt the user to enter the person's details
    name = input("Enter the person's name: ")
    age = int(input("Enter the person's age: "))  # Convert input to integer
    gender = input("Enter the person's gender: ")

    # Create an instance of the Person class
    person = Person(name, age, gender)

    # Call the introduce method to display the person's information
    person.introduce()

# Execute the main function
if __name__ == "__main__":
    main()
