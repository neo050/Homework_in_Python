"""
This file operates a system for receiving information about students and performing mathematical operations on their information
"""
from functools import reduce


class Course:
    """
    This class represents a course class which contains a course name and course grade as well as a default value
    """

    def __init__(self, name):
        """
        Apply a course to a default value
        :param name:Specifies a class object field
        :return: nothing
        """
        self.name, self.grade = name, 101.0

    def setGrade(self, grade):
        """
       Changes the score of the course object
        :param grade:The new score
        :return:none
        """
        if grade < 0.0 or grade > 100.0:
            return
        self.grade = grade

    def getGrade(self):
        """
        Returns the score of the course object
        :return: Returns the score of the course object
        """
        return self.grade

    def getName(self):
        """
         Returns the name of the course object
        :return:Returns the name of the course object
        """
        return self.name

    def setName(self, name):
        """
        Changes the name of the course object
        :param name: new name of object
        :return: none
        """
        self.name = name


class Student:
    """
    This class represents a student class that holds objects from a course class and variables that represent the student's name and ID card.
    """

    def __init__(self, name, id):
        """
        Initializes an object with a name ID and a blank course dictionary
        :param name: name of student
        :param id:id of student
        """
        self.name, self.__id, self.courses = name, id, {}

    def getID(self):
        """
        return id of student object
        :return:  return id of student object
        """
        return self.__id

    def setID(self, id):
        """
        Changes the ID of the object
        :param id:new id of object
        :return: none
        """
        self.__id = id

    def addCourse(self, Icourse):
        """
        The recipient of a course object performs logic on the information and under the correctness of the information, encloses it in the student's course list.
        :param Icourse: the object course
        :return:none
        """
        if Icourse.getGrade() < 0.0 or Icourse.getGrade() > 100.0:
            return
        self.courses[Icourse.getName()] = Icourse

    def setName(self, name):
        """
        Renames the student
        :param name:new name
        :return:none
        """
        self.name = name

    def getName(self):
        """
        return name of the student
        :return:         return name of the student

        """
        return self.name

    def getGradeInCourse(self, nameC):
        """
        Returns a student's grade in the course according to the name of the course received
        :param nameC: the name of the course
        :return: grade in the course
        """
        k = list(filter(lambda x: x.getName() == nameC, self.courses.values()))
        if any(k):
            return k[0].getGrade()
        return -1

    def average(self):
        """
        Returns average student in courses
        :return: Returns average student in courses
        """
        if any(self.courses.values()):
            return sum(map(lambda x: x.getGrade(), self.courses.values())) / len(self.courses.values())


def ChargingStudentsIntoTheSystem():
    """
    This function asks the user for the name of an input file and tries to open it, executes logic on the data and returns an array of organized information within the student-type objects
    Otherwise prints an error message
    :return:
    """

    studentArr = []
    try:
        with open(input("Enter name of file: "), 'r', encoding='utf8') as f:
            for line in f:
                demoS = Student("demo", 0)
                good = line.strip().split("\t")
                demoS.setName(good[0])
                demoS.setID(int(good[1]))
                if len(good) > 2:
                    coursdata = good[2].split(";")
                    for i in coursdata:
                        demoC = Course("\t")
                        i = i.split("#")
                        demoC.setName(i[0])
                        demoC.setGrade(float(i[1]))
                        demoS.addCourse(demoC)
                studentArr.append(demoS)
    except OSError as err:
        print(f" the file Not found OS error: {err}.")
        return 0
    except BaseException as err:
        print(f"Unexpected {err}, {type(err)}")
        return 0
    return studentArr


def f1():
    """
    Requests student name input from the user and prints the student's average
    :return: none
    """
    name = input("Enter name of student: ")
    k = list(filter(lambda x: x.getName() == name, demoS))
    if any(k):
        print("Id: ", k[0].getID(), "\naverage: ", k[0].average())
    else:
        print("There is no student by that name in our information system.")


def f2():
    """
    Requests course name input from the user and prints the course average
    :return: none
    """
    name = input("Enter name of Course: ")
    k = list(filter(lambda x: x > -1, map(lambda x: x.getGradeInCourse(name), demoS)))
    if any(k):
        k = sum(k) / len(k)
        print("name of Course: ", name, "\naverage: ", k)
    else:
        print("There is no Course by that name in our information system.")


def f3():
    """
    Requests course name input from the user and prints the course average
    :return: none
    """
    try:
        f = open(input("Enter name of file: "), 'w', encoding='utf8')
        f.write(reduce(lambda x, y: x + y, map(lambda x: str(x.getID()) + " " + str(x.average()) + '\n', demoS)))
        f.close()
    except OSError as err:
        print(f" the file Not found OS error: {err}.")
    except BaseException as err:
        print(f"Unexpected {err}, {type(err)}")


demoS = ChargingStudentsIntoTheSystem()
if demoS:#Check if the file read was successful
    while True:
        """
        The user is presented with a menu until the input is entered correctly and an orderly exit from the program is selected
        """
        a = input("Enter your choice:\n1->Averaging a particular student\n2->Calculating the average in a particular course\n3->Average of all students.\n4->Exit the program.\n")
        if a == '1':
            f1()
        if a == '2':
            f2()
        if a == '3':
            f3()
        if a == '4':
            print("Have a nice day Dear user You have selected the option to exit the program Thank you for your participation")
            break
