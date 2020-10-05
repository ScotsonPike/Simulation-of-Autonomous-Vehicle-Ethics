import random

class randomPerson:
    
    gender = ""
    age = ""
    fit = ""
    employ = ""
    
    def allocate(self):
        if random.random() > 0.5:
            self.gender = "male"
        else:
            self.gender = "female"
        num = random.random()
        if num < 0.33:
            self.age = "child"
        elif num < 0.66:
            self.age = "adult"
        else:
            self.age = "older"
        if self.age != "child":
            if random.random() > 0.5:
                self.fit = "fit"
            else:
                self.fit = "unfit"
            num = random.random()    
            if num < 0.25:
                self.employ = "Homeless"
            elif num < 0.5:
                self.employ = "Business"
            elif num < 0.75:
                self.employ = "Doctor"
            else:
                self.employ = "Criminal"
        
            
    def printPerson(self):
        print("Gender: "+ self.gender)
        print("Age: " + self.age)
        if self.age != "child":
            print("Health: "+ self.fit)
            print("Employ: "+self.employ)
        

if __name__ == "__main__":
    rp = randomPerson()
    rp.allocate()
    rp.printPerson()