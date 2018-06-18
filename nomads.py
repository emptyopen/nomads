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


class Game:

# ----------------------------------------------------------------------------------------------------------------------------------- PREP

    def __init__(self):

        # window
        self.caption = "The Nomads"
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1800, 717))  # (890, 503) , 214 vert for black, 20 margin
        self.background = pygame.image.load('pics/n-wall.png')
        self.one_off = True # toggler that ensures screen updates after state update?




# -------------------------------------------------------------------------------------------------------------------- EXECUTE

    def main(self):

        # setup
        pygame.init()
        pygame.display.set_caption(self.caption)
        self.map_components()
        self.place_components()
        if not DEBUG:
            self.create_basetime()

        while True: # main game loop

            self.update_state()

            # update state of game continuously
            for event in pygame.event.get():

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit

            self.update_display()


    def update_state(self):

        pass


# --------------------------------------------------------------------------------------------------------- DRAW

    def update_display(self):

        self.screen.blit(self.background, (self.p_offset[0], self.p_offset[1]))


    # blacksword.tff

    def draw_message(self, message, coord = (100, 100), preset = None, font = FONT, font_size = FONTSIZE, text_color = (160, 190, 255), background_color = None):
        if preset == 'help':
            background_color = (0, 0, 0)
            text_color = (255, 255, 255)
        if preset == 'bottom':
            background_color = None
        self.screen.blit(pygame.font.SysFont(font, font_size).render(message, True, text_color, background_color), coord)
