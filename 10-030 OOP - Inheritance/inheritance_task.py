"""
Course Management Program

Defines a generic `Course` class and a subclass `OOPCourse`
for an object-oriented programming course.
"""


class Course:
    """
    A class representing a generic course.
    """

    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_office = "Cape Town"

    def contact_details(self):
        """Prints the contact details for the course."""
        print("Please contact us by visiting", self.contact_website)

    def print_head_office_location(self):
        """Prints the location of the head office."""
        print("Head office location:", self.head_office)


class OOPCourse(Course):
    """
    A subclass representing an object-oriented programming course.
    """

    def __init__(self):
        """Initializes attributes specific to the OOPCourse subclass."""
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        """Prints the course description and trainer details."""
        print("Course description:", self.description)
        print("Trainer:", self.trainer)

    def show_course_id(self):
        """Prints the course ID."""
        print("Course ID:", "#12345")


# Create an object of the subclass
course_1 = OOPCourse()

# Call the methods
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
