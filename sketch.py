# myMarks = input("Write the subject here : ")
# updateSubject = input("Write the subject to change the marks for : ")
# updateMarks = input("Write the marks you want to change for the subject : ")

# totalMarksScored = int(input("Write the number of marks you scored : "))

# totalNumberOfMarks = int(
#     input("Write the maximum amount of marks of the test : "))
# totalMarks = 0
# marksScored = 0


class Person(object):
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades
        self.totalMarks = 0
        self.marksScored = 0

    def getGrades(self, course):
        print("I have got" + " " +
              self.grades[course] + " " + "in " + course)
        return self.grades[course]

    def setGrades(self, marks, course):
        self.grades[course] = marks

    def calculatePercentage(self):
        for i in self.grades:
            print(i)
            self.totalMarks = self.totalMarks + 25
            self.marksScored = self.marksScored + self.grades[i]
        print(self.totalMarks)
        print(self.marksScored)
        print((self.marksScored / self.totalMarks) * 100)


roshan = Person("Roshan", {"math": 24, "science": 24.5, "english": 25})
# roshan.setGrades(updateMarks, updateSubject)
roshan.calculatePercentage()
# print(roshan.grades)
