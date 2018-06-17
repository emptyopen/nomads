'''
everyone is a pixel, fighting against bosses. as more people play, pixels get smaller

You can be: Warrior (tanky), Hunter (ranged, pet), Mage (ranged, magic), Farmer, Medic

Stats/inventory are displayed on takaomatt.com

starts with 10x10 grid?
'''

class Player(object):

    def __init__(self):

        self.profession = 'Warrior'
        self.inventory = []
        self.equipped = {'head':None, 'chest':None, 'arms':None, 'legs':None, 'misc1':None, 'misc2':None}
        self.level = 1

    def reset_character():
        pass

    def change_character():
        pass
