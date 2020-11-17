class Monster():

    def __init__(self, size, types, HP, MP, gender):
        self.size = size
        self.types = types
        self.HP = HP
        self.MP = MP
        self.gender = gender
        

    def attack(self, times):
        self.HP = times*(self.HP*0.2)
        return self.HP

    def sleep(self, time):
        self.HP = self.HP + time*20
        self.MP = self.MP + time*2000
        return self.HP

    def Form_second_stage(self, time):
        self.MP = self.MP - time*10000
        self.HP = self.HP - time*10
        return self.MP

class Beast(Monster):
    def __init__(self, size, types, HP, MP, gender):
        super().__init__(size, types, HP, MP, gender)

    def eat(self, time):
        self.size = self.size + time*1
        return self.size
    

Werewolf = Monster(200, 'Canine', 1000,200000, 'Male')
Whitewolf = Beast(350, 'Canine', 10000, 300000, 'Male')
print('Werewolf size:', Werewolf.size)
print('Werewolf types:', Werewolf.types)
print('Werewolf HP:', Werewolf.HP)
print('Werewolf MP:', Werewolf.MP)
print('Werewolf gender:', Whitewolf.gender)
print('Whitewolf size:', Whitewolf.size)
print('Whitewolf types:', Whitewolf.types)
print('Whitewolf HP:', Whitewolf.HP)
print('Whitewolf MP:', Whitewolf.MP)
print('Whitewolf gender:', Whitewolf.gender)

#Attack 10 times
print('The damage of the attacks:', Werewolf.attack(10))

#Sleep for 10 hours
print('HP after sleeping:', Werewolf.sleep(10))

#Transformed for 10 minutes
print('MP after transformed:', Werewolf.Form_second_stage(20))

#Attack 10 times
print('The damage of the attacks:', Whitewolf.attack(10))

#Sleep for 10 hours
print('HP after sleeping:', Whitewolf.sleep(10))

#Transformed for 10 minutes
print('MP after transformed:', Whitewolf.Form_second_stage(20))

#Eat for 10 minutes
print('Size of Whitewolf after eating:', Whitewolf.eat(10))
