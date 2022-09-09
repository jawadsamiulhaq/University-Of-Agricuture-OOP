name = input("Enter Name : ")
ag = input("Enter Your Ag No : ")
cgpa = input("Enter Your CGPA : ")

class University:
    uni = "University Of Agriculture"
    def __init__(self,name,ag,cgpa):
        self.name = name
        self.ag = ag
        self.cgpa = cgpa
    @staticmethod
    def getInfo():
        print("\t\tWelcome")
        print(f"{universityy.uni} Is Present In Toba Tek Singh ")
        print(f"Location = Kekhar Bangla Road Near 149 Village ")
    def totalDegress(self):
        print(f"Total Degress In {universityy.uni} = 16")
    def degressName(self):
        print("\t*Degress*")
        lst = ["BS Computer Science","BS IT","BS Math","BS Chemistry"
        ,"BS Animal Science","BS Poetry Science",
        "BS English","Bachelor In Bussines Art",
        "BS Bio Chemistry","BS Zology"]
        for i in range(0,len(lst)):
            # print(f"{i+1} - "+ lst[i])
            print(f"{i+1} - {lst[i]}")
        

class Degree(University):
    def bsCS(self):
        print(f"\n{self.uni}")
        print(f"\n{self.name} Is A Student Of BS Computer Science")
        print(f"\nAG No = {self.ag}")
        print(f"\nCGPA Of {self.name} Is {self.cgpa}")
    def bsIT(self):
        print(f"\n{self.uni}")
        print(f"{self.name} Is A Studet Of BS IT")
        print(f"\nAG No = {self.ag}")
        print(f"CGPA Is {self.cgpa}")
    def bsPoetryscience(self):
        print(f"\n{self.uni}")
        print(f"\n{self.name} Is A Student Of BS Poetry Science")
        print(f"\nAG No = {self.ag}")
        print(f"\nCGPA Of {self.name} Is {self.cgpa}")
    def bsChemistry(self):
        print(f"\n{self.uni}")
        print(f"\n{self.name} Is A Student Of BS Chemistry")
        print(f"\nAG No = {self.ag}")
        print(f"\nCGPA Of {self.name} Is {self.cgpa}")
    def bsAnimalscience(self):
        print(f"\n{self.uni}")
        print(f"\n{self.name} Is A Student Of BS Animal Science")
        print(f"\nAG No = {self.ag}")
        print(f"\nCGPA Of {self.name} Is {self.cgpa}")
    def bsBiochemistry(self):
        print(f"\n{self.uni}")
        print(f"\n{self.name} Is A Student Of BS Bio Chemistry")
        print(f"\nAG No = {self.ag}")
        print(f"\nCGPA Of {self.name} Is {self.cgpa}")
    def bsEnglish(self):
        print(f"\n{self.uni}")
        print(f"\n{self.name} Is A Student Of BS English")
        print(f"\nAG No = {self.ag}")
        print(f"\nCGPA Of {self.name} Is {self.cgpa}")
    def bba(self):
        print(f"\n{self.uni}")
        print(f"\n{self.name} Is A Student Of Bachelor In Bussiness Art")
        print(f"\nAG No = {self.ag}")
        print(f"\nCGPA Of {self.name} Is {self.cgpa}")
    def bsMath(self):
        print(f"\n{self.uni}")
        print(f"\n{self.name} Is A Student Of BS Math")
        print(f"\nAG No = {self.ag}")
        print(f"\nCGPA Of {self.name} Is {self.cgpa}")
    def bsZology(self):
        print(f"\n{self.uni}")
        print(f"\n{self.name} Is A Student Of BS Zology")
        print(f"\nAG No = {self.ag}")
        print(f"\nCGPA Of {self.name} Is {self.cgpa}")
    
    
        
# a = University(name,ag,cgpa)
# a.getInfo()
universityy = Degree(name,ag,cgpa)
# universityy.getInfo()
# universityy.bsCS()
# universityy.degressName()

# universityy.totalDegress()
# universityy.bsIT()
universityy.getInfo()

