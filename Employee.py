class Student:
    def __init__(self, university_id, first_name, last_name, year, sem, branch):
        self.university_id = university_id
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.sem = sem
        self.branch = branch

    university_name = 'klh'

    def get_email(self):
        return f'{self.first_name},{self.last_name}@{Student.university_name},edu.in'

    @classmethod
    def change_name(cls, new_name):
        cls.university_name = new_name

    @staticmethod
    def static_method():
        print("welcome to PFSD class")


std_1 = Student(2110039471, 'Charita', 'Ravi',2022, 'ODD','CSE')

print("First name is ", std_1.first_name)
print("Student Last name is ", std_1.last_name)
print("University ID is ", std_1.university_id)
print("University Year is ", std_1.year)
print("University Branch is ", std_1.branch)
print("university Semester is ", std_1.sem)

print(std_1.get_email())
print(std_1.static_method())

std_1.change_name('K L University')

print("New name of university: ",Student.university_name)