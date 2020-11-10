class Monster():

    def __init__(self, size, types, HP, MP):
        self.size = size
        self.types = types
        self.HP = HP
        self.MP = MP

    def attack(self, times):
        self.HP = times*(self.HP*0.2)
        return self.HP

    def sleep(self, time):
        self.HP = self.HP + time*20
        return self.HP

    def Form_second_stage(self, time):
        self.MP = self.MP - time*10000
        return self.MP
    

Werewolf = Monster(200, 'Canine', 1000,200000)
print('Werewolf size:', Werewolf.size)
print('Werewolf types:', Werewolf.types)
print('Werewolf HP:', Werewolf.HP)
print('Werewolf MP:', Werewolf.MP)

#Attack 10 times
print('The damage of the attacks:', Werewolf.attack(10))

#Sleep for 10 hours
print('HP after sleeping:', Werewolf.sleep(10))

#Transformed for 10 minutes
print('MP after transformed:', Werewolf.Form_second_stage(20))
