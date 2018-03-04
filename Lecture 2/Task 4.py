class Member:  #класс, который содержит информацию о человеке
    name = ""  #переменные
    sex = ""
    age = ""

    def __init__(self, name, sex, age): #конструктор класса, первоначальная инициализация
        self.name = name
        self.sex = sex
        self.age = age

    def printSettings(self):            #метод класса, печатает информацию о человеке
        print("Name =", self.name)
        print("Sex =", self.sex) 
        print("Age =", self.age)


class Family:   #класс семья

    children = []

    def __init__(self, father, mother):        #Конструктор класса семья
        self.Father = father                   #Инициализация переменных
        self.Mother = mother

    def addChild(self, child):
        self.children.append(child)

    def printFamily(self):                     #метод класса, печатает все о семье
        print("Father: ")
        (self.Father).printSettings()          #Father имеет тип Member
                                               #C помощью метода из класса Member печатаем инф. о человеке
        print("\nMother: ")
        (self.Mother).printSettings()
        print("\nChild: ")
        for item in self.children:
            item.printSettings()
            print()

if __name__ == '__main__':
                                            #нужно указать, откуда начать
    member1 = Member("Alex", "M", "27")     #Создаем переменные Людей    
    member2 = Member("Ann", "W", "21")
    member3 = Member("Stefan", "M", "5")
    member4 = Member("Vera", "W", "3")
    member5 = Member("Moritz", "M", "1")
    family = Family(member1, member2)           #создаем перемнную семья
                                                #передаем в конструктор наших членов семьи
    family.addChild(member3)
    family.addChild(member4)
    family.addChild(member5)

    family.printFamily()                        #печатаем информацию о семье

