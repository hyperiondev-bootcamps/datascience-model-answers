class Adult:
    """
    Represents an adult person with attributes such as name, age, hair colour, and eye colour.
    """

    def __init__(self, name, age, hair_colour, eye_colour):
        """
        Initialise attributes of the Adult object.

        Args:
            name (str): The name of the adult.
            age (int): The age of the adult.
            hair_colour (str): The hair colour of the adult.
            eye_colour (str): The eye colour of the adult.
        """

        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    def can_drive(self):
        """
        Print whether the person is old enough to drive.
        """

        print(f"{self.name} is old enough to drive.")


class Child(Adult):
    """
    Represents a child person inheriting from the Adult class.
    """

    def can_drive(self):
        """
        Print that the person is too young to drive.
        """

        print(f"{self.name} is too young to drive.")



# Get user inputs for person's details
name = input("Enter name: ")
age = int(input("Enter age: "))
hair_colour = input("Enter hair colour: ")
eye_colour = input("Enter eye colour: ")

# Determine if the person is an adult or child based on age
if age >= 18:
    person = Adult(name, age, hair_colour, eye_colour)
else:
    person = Child(name, age, hair_colour, eye_colour)

# Call the can_drive method to print whether the person can drive
person.can_drive()
