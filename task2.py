class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, I'm {self.name}. an {self.age} year-old {self.course} student.")

student1 = Student("Ivy",26, "Diploma in Program - Information Technology")
student2 = Student("Nathasia", 22, "DIP-IT")
student3 = Student("Alyanna", 20, "DIP-IT" )

print("Student 1:")
student1.introduce()
print("\nStudent 2:")
student2.introduce()
print("\nStudent 3:")
student3.introduce()
