#Author: Rushabh Shah
#Original creation date: 04/25/2017
#Last modification date: 04/25/2017
#Description: This program creates 2 classes and implements inheritance and shows how polymorphism works by overriding __init__() method of the superclass Beast

#superclass Beast
class Beast():
    #__init__ method, takes species parameter
    def __init__(self, species):
        self.__species = species  #sets the private attribute species via arguement

    #access method that returns the value of the private attribute of the calling object 
    def access_species(self):
        return self.__species

#subclass Dragon inheriting superclass Beast
class Dragon(Beast):
    #__init__() method of Dragon class, overrides the __init__() method of Dragon and takes parameter species
    def __init__(self, species):
        #since its inheriting the superclass Beast, first the __init__() method of superclass need to be called
        Beast.__init__(self, species)

    #method speak that prints what dragon speaks
    def speak(self):
        print('The dragon speaks AHHHH')

#main function that calls other fucntions
def main():
    print('The supreclass species is:')
    #3 objects created, one for superclass and 2 of subclass Dragon, prints species of all 3 objects by calling access_species method on each object
    beast = Beast('beast')
    print(beast.access_species())
    print('The two Dragon species are:')
    dragon1 = Dragon('Charizard')
    print(dragon1.access_species())
    dragon1.speak()
    dragon2 = Dragon('Goodra')
    print(dragon2.access_species())
    
    
main()
