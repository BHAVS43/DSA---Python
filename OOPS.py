class Student:
    def __init__(self, sname, sroll, syear):
        self.name = sname
        self.roll = sroll
        self.year = syear

s1 = Student("Bhavana", 478, 3)
s2 = Student("Amulya", 412, 3)
s3 = Student("Tulsi", 413, 3)
print(s1.name, s1.roll, s1.year)
print(s2.name, s2.roll, s2.year)
print(s3.name, s3.roll, s3.year)
    
