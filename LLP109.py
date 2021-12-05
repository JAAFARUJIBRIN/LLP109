#All our imports here
import sys 
# define user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

class CourseCannotBeEmpty(Error):
    """Raised when the course entered is empty"""
    pass
class CreditUnitNotInRange(Error):
    """Raised when the input value is too large"""
    pass

class ScoreNotInRange(Error):
    """Raised when the score is not within the range of 0-100"""
    pass

def calculateCGPA():
        """This function calculate the students cgpa by first finding the corresponding grade for a score range"""
        grades_list=[]
        grade_A=5
        grade_B=4
        grade_C=3
        grade_D=2
        grade_E=1
        grade_F=0
        points=0
        A_range=range(70,101)
        B_range=range(60,70)
        C_range=range(50,60)
        D_range=range(45,50)
        E_range=range(40,45)
        #F_range=range(0,40)
        for i in range(len(course_list)):               #This function gets the grade for a score range and stores it in grades list
                if (score_list[i] in A_range):
                        grades_list.append('A')
                        points +=grade_A * credits_list[i]
                elif (score_list[i] in B_range):
                        grades_list.append('B')
                        points +=grade_B * credits_list[i]
                elif (score_list[i] in C_range):
                        grades_list.append('C')
                        points +=grade_C * credits_list[i]
                elif (score_list[i] in D_range):
                        grades_list.append('D')
                        points +=grade_D * credits_list[i]
                elif (score_list[i]in E_range):
                        grades_list.append('E')
                        points +=grade_E * credits_list[i]
                else:
                        grades_list.append('F')
                        points +=grade_F * credits_list[i]
        print("----------------------------------------------------------------------------\n----------------------------------------------------------------------------\n\tSUMMARY OF RESULTS AND CUMULATIVE GRADE POINT AVERAGE\n\n")
        print("Course Name\tCredit Unit\tFinal Score\tGrade\n")
        for i in range(len(course_list)):
               print(course_list[i],"\t\t",credits_list[i],"\t\t",score_list[i], "\t\t", grades_list[i])        

        print("----------------------------------------------------------------------------\n\t\tYour CGPA is:  %.2f\n----------------------------------------------------------------------------\n " % float(points/sum(credits_list)))


def displayEntry():
     """This function displays the entry inputed thus far"""
     for i in range(len(course_list)):
               print(course_list[i],"\t\t",credits_list[i],"\t\t",score_list[i])
def exitProgram():
     """Invoking this function exits the program"""
     input("\nHope that looks good! Press any key to exit>>\t")
     print("Successfully exited...")
     sys.exit(0)

    
if __name__ == "__main__":
    
    print("\nWelcome!!!\n This program does your CGPA calculation job for you! \n Follow the prompts and that's all\n ")
    a=True #Loop control flow for flexibilty of my program
    course_list=[]#This list holds the courses
    credits_list=[]#This list holds the credit units
    score_list=[]#This list holds the scores
    max_score=100
    min_score=0
    max_creditunit=6
    min_creditunit=0
    while(a):
        b=input("Let's start\nPress any key then hit Enter to start or\nPress Q to quit >>\t")
        if(b == 'Q' or b== 'q'):
            exitProgram()
        else:
            loop= True
            while(loop):
                    try:
                            course = str(input("Enter course name or course code >> \t"))
                            if (len(course)!= 0):
                               course_list.append(course)
                            else:
                               raise CourseCannotBeEmpty
                               break
                    except CourseCannotBeEmpty:
                                print ("\n Invalid entry. Course cannot be empty. Please Try again\n")
                                continue
                    g=True
                    while(g):
                            try:
                                creditunit= int(input("Enter the credit units for %s >>\t" %(course_list[len(course_list)-1])))
                                if (creditunit in range(min_creditunit,max_creditunit+1)):
                                        credits_list.append(creditunit)
                                else:
                                        raise CreditUnitNotInRange
                                        break
                            except (CreditUnitNotInRange, ValueError):
                                    print("\n Invalid entry. Please enter an integer value between 0 and 6 \n")
                                    continue
                            h=True
                            while(h):
                              try:
                                    score = float(input("Enter your score for %s >>\t"%(course_list[len(course_list)-1])))
                                    if (score in range (min_score,max_score+1)):
                                            score_list.append(score)
                                            f=input("\n\nWhat next do you want to do?\nPress key Q to exit\nPress key S to show Entry[ies]\nPress key C to calculate CGPA\nPress any letter to input the next course>>\t")
                                            if(f=='q' or f=='Q'):
                                                exitProgram()
                                            elif (f=="s" or f=="S"):
                                                print("\n\tDisplaying courses...\n")
                                                print("Course Name\tCredit Unit\tFinal Score\n")
                                                displayEntry()
                                                y=input("\n\nWhat next do you want to do?\nPress key Q to exit\n press key C to calculate CGPA \nPress any key to input the next course>>\t")
                                                if (y=='q' or y=='Q'):
                                                     exitProgram()
                                                elif(y=='c' or y=='C'):
                                                     print("\n\tCalculating CGPA....\n")
                                                     calculateCGPA()
                                                     exitProgram()

                                                else:
                                                     pass
                                                     g=False
                                                     h=False
                                            elif (f=="C" or f=="c"):
                                                print("\n\tCalculating CGPA...\n")
                                                calculateCGPA()
                                                exitProgram()
                                            else:
                                                pass
                                                g=False
                                                h=False
                                    else:
                                            raise ScoreNotInRange
                                            break
                                                    
                              except (ScoreNotInRange, ValueError):
                                    print("\nInvalid entry. Please enter a score between 0 and 100 \n")
                                    pass
