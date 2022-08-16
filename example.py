class PlayerCharacter():
    membership = True
    def __init__(self, name, age):
        self._name = name
        self._age = age

    
    def run(self):
        print('ehoooo run')
        return 'done'
        
    @classmethod
    def add_things(cls, num1, num2):
        return cls('Hola', num1 + num2)
    
    @staticmethod
    def adding_num(num1, num2):
        return num1 + num2

player = PlayerCharacter('iliana', 10)
player1 = PlayerCharacter.add_things(1, 2)
player1.name = 'dadada'
# print(player.name)
# print(player.age)
# print(player.run())
# print(player1.name)
print(PlayerCharacter.adding_num(2,3))
print(player1.name )