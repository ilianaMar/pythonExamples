class User():
    # def __init__(self, email):
    #     self.email = email
        
    def sign_in(self):
        print('i am user class')
        
    def attack(self):
        print("do nothing")
    
class Wizard(User):
    def __init__(self, name, power):
    #    User.__init__(self, email)
    #    super().__init__(email)
       self.name = name
       self.power = power
       
    def sign_in(self):
        print('say hey I am wizard')
       
    def attack(self):
        # User.attack(self)
        print(f"attacking with power {self.power}")
       

class Archer(User):
    def __init__(self, name, num_arrows):
        # super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows
       
    def attack(self):
        print(f"attacking with arrows {self.num_arrows}")
        
    def run(self):
        print('ehooo you run')
        
def player_attack(char):
    char.attack()
    
class HybridBoard(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)



# wizard1 = Wizard('marolejn', 40, 'wizard@gmail.com')
# archer1 = Archer('iliana', 50, 'archer@gmail.com')
# user1 = User('user@gmail.com')
# print(wizard1.sign_in())
# print(user1.sign_in())
# player_attack(wizard1)
# player_attack(archer1)
# print(wizard1.attack())
# print(archer1.sign_in())
# print(archer1.attack())
# print(isinstance(wizard1, User))
# print(isinstance(wizard1, object))
# print(isinstance(wizard1, Wizard))
# print(isinstance(wizard1, Archer))


# print(wizard1.email)
# print(user1.email)
# print(archer1.email)
# print(dir(wizard1))

hb = HybridBoard('iliana', 30, 40)
print(hb.run())
print(hb.sign_in())