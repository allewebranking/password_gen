# class Dog:

#

#
    # def bark(self):
        # print("BARK!!")
    # def __init__(self,name="",age=0,furcolor=""):
        # self.name=name
        # self.age=age
        # self.furcolor=furcolor

#
    # def  toString(self):
        # print(self.name+"\n"+str(self.age)+"\n"+self.furcolor)

#
# mydog=Dog("fido",90,"bianco")

#

#
# mydog.toString()


# mydog=Dog()
# mydog.bark()
# mydog.anni=5
# mydog.nome="fido"

#
# print(mydog.anni)
# print(mydog.nome)
class Car:
    def __init__(self,year=0, make="", model=""):
        self.year = year
        self.make = make
        self.model = model
    def age(self):
        return 2021-self.year
    def toString(self):
        print( "età macchina: "+str(self.age())+"\n"+"chi l'ha creata: "+self.make+"\n" +"Modello: "+self.model)


car=Car(1989,"bho","fiat")

car.toString()
