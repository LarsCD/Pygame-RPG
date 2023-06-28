import pygame
import logging
from item_display_screen import Item_Display_Screen

from assets.custom_pygame_assets import Label
from dev.dev_logger import DevLogger
from dev.dev_screen import DevScreen

class Player_Inventory:
    def __init__(self, ROOT):
        self.ROOT = ROOT
        self.run_display = True

        # SCENE COLORS
        self.default_bg_color = self.ROOT.default_bg_color
        self.bg_color = self.ROOT.bg_color
        self.BLACK = (0, 0, 0)
        self.highlight_color = (38, 162, 140)

        # SCENE LABELS
        self.static_text_lables = []
        self.dynamic_category_lables = []
        self.dynamic_item_labels = []

        self.title = 'PLAYER INVENTORY'
        self.display_start_x_pos = 128
        self.display_start_y_pos = 120
        self.display_sep_space = 300
        self.text_size = 15
        self.name_pos_x = 135
        self.background = pygame.image.load("assets/images/inventory_background_1.png")

        # PLAYER
        self.player_object = None

        # INVENTORY
        self.cat_text_size = 20
        self.current_inventory_category = 'weapon'
        self.cat_positions = {
            'weapon': (109, 70),
            'potion': (282, 70),
            'armor': (456, 70),
            'helmet': (645, 70),
            'shield': (826, 70),
            'key_item': (1023, 70),
        }

        self.item_text_size = 20
        self.item_begin_pos_x = 100
        self.item_begin_pos_y = 200

        # ICON DATA
        self.default_icon_size = (64, 64)
        self.tier_frame_pos = (128, 40)
        self.icon_pos = (130, 42)
        self.default_frame_size = (60, 60)
        self.tier_name_pos_y = 80

        # MODULES
        self.log = DevLogger(Player_Inventory).log
        self.DevScreen = DevScreen(self.ROOT)
        self.Item_Display_Screen = Item_Display_Screen


    def main_loop(self, player_object):
        self.player_object = player_object
        self.run_display = True

        back_label = Label('BACK', 25, 'white', 'gray', (153, 0, 28),
                           (1090, 620), is_clickable=True, bold_text=True)

        self.dynamic_category_lables = []
        self.build_categories()

        self.build_items()

        while self.run_display:
            # self.log(logging.DEBUG, f'self.current_inventory_category: {self.current_inventory_category}')

            self.check_quit_event()

            self.build_static_text_lables()

            # display background
            self.ROOT.window.blit(pygame.transform.scale(self.background, self.ROOT.RESOLUTION), (0, 0))

            self.draw_static_text_labels()
            self.draw_dynamic_category_labels()
            self.draw_dynamic_item_labels()

            if back_label.draw_text(self.ROOT.window):
                # quit out of view
                self.run_display = False

            # dev
            self.DevScreen.main()

            pygame.display.update()
            self.ROOT.clock.tick(self.ROOT.fps)

    def check_if_current_cat(self, category):
        if category == self.current_inventory_category:
            return 1
        else:
            return 0

    def change_current_cat(self, category):
        self.current_inventory_category = category

    def update_category_labels(self):
        cat_lookup_table = {
            'Weapons': 'weapon',
            'Potions': 'potion',
            'Armor': 'armor',
            'Helmet': 'helmet',
            'Shield': 'shield',
            'Keys': 'key_item',
        }

        for i, _ in enumerate(self.dynamic_category_lables):
            LABEL = self.dynamic_category_lables[i]
            cat_index = cat_lookup_table[LABEL.text]
            if self.check_if_current_cat(cat_index):
                LABEL.def_color = self.highlight_color
            else:
                LABEL.def_color = 'white'

    def build_categories(self):
        for category in self.player_object.inventory_cat_names:

            # set text color
            main_text_color = 'white'
            if self.check_if_current_cat(category):
                main_text_color = self.highlight_color

            # get category name
            cat_name = self.player_object.inventory_cat_names[category]

            category_label = Label(f'{cat_name}', self.cat_text_size, main_text_color, 'white', 'gray',
                                   (self.cat_positions[category]), bold_text=True, is_clickable=True,
                                   class_method=self.change_current_cat, method_args=(category))

            self.dynamic_category_lables.append(category_label)


    def build_items(self):
        item_offset_y = 5
        quantity_offset_x = 300
        column_offset_x = 333
        column_counter = 1
        max_column_items = 17
        column_item_counter = 0


        for index, item in enumerate(self.player_object.inventory[self.current_inventory_category]):
            column_item_counter += 1

            if column_item_counter >= 17:
                column_item_counter = 0
                column_counter = 1

            pos_x = self.item_begin_pos_x+(column_offset_x*column_counter)
            pos_y = self.item_begin_pos_y+((self.item_text_size+item_offset_y)*column_item_counter)

            # get current item object
            item_object = self.player_object.inventory[self.current_inventory_category.lower()][index]

            # get item quantity
            quantity = self.player_object.get_item_quantity(item.tag, item.item_type)

            # bake labels
            item_label = Label(f'{item.name}', self.item_text_size, item.tier_color, 'white', 'gray',
                               ((pos_x), (pos_y)), bold_text=True, is_clickable=True,
                               class_method=self.Item_Display_Screen(self.ROOT).main_loop, method_args=(item_object))

            quantity_label = Label(f'x{quantity}', self.item_text_size, 'white', 'black', 'black',
                                   ((pos_x+quantity_offset_x), (pos_y)), bold_text=True, is_clickable=False)

            # save labels
            self.dynamic_item_labels.append(item_label)
            self.dynamic_item_labels.append(quantity_label)



    def set_background_color(self):
        if self.bg_color != None:
            self.ROOT.window.fill(self.bg_color)
        else:
            self.ROOT.window.fill(self.default_bg_color)


    def build_static_text_lables(self):
        def_color = self.ROOT.lable_hover_col
        black = (0, 0, 0)
        # build static labels
        title_label = Label(self.title, self.text_size, self.ROOT.lable_col, self.ROOT.lable_click_col,
                            self.ROOT.lable_hover_col, (5, 5),
                            is_clickable=False)
        self.static_text_lables.append(title_label)


    def draw_static_text_labels(self):
        for label in self.static_text_lables:
            label.draw_text(self.ROOT.window)
        self.static_text_lables = []


    def draw_dynamic_category_labels(self):
        self.update_category_labels()
        for label in self.dynamic_category_lables:
            label.draw_text(self.ROOT.window)

    def draw_dynamic_item_labels(self):
        for label in self.dynamic_item_labels:
            label.draw_text(self.ROOT.window)


    def check_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
