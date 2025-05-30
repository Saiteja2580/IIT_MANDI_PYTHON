class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"Name of User : {self.name}")
        print(f"Email of User : {self.email}")


class Instructor(User):
    def __init__(self,name,email,subject):
        super().__init__(name,email)
        self.subject_expert = subject

    def display_info(self):
        print(f"Name of Instructor : {self.name}")
        print(f"Email of Instructor : {self.email}")
        print(f"Subject Expertise of Instructor : {self.subject_expert}")

    def upload_content(self):
        print("Content Uploaded")

class CourseCreator(Instructor):
    def __init__(self, name, email, subject):
        super().__init__(name, email,subject)


    def display_info(self):
        print(f"Name of Course Creator : {self.name}")
        print(f"Email of Course Creator : {self.email}")
        print(f"Subject Expertise of Course Creator : {self.subject_expert}")

    def create_module(self):
        print("Complete Course Created with modules")


creator = CourseCreator("Sai","saiteja@","Chemistry")
creator.upload_content()
creator.create_module()
creator.display_info()