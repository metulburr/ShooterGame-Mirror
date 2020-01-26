from . import tools
import pygame as pg

class MenuManager:
    def __init__(self):
        self.selected_index = 0
        self.last_option = None
        self.button_volume = .2
        self.button_hover_volume = .1
        self.button_sound = tools.Sound('button.wav')
        self.button_sound.sound.set_volume(self.button_volume)
        self.button_hover = tools.Sound('button_hover.wav')
        self.button_hover.sound.set_volume(self.button_hover_volume)
        
    def mouse_hover_sound(self):
        '''play sound when selected option changes'''
        for i,opt in enumerate(self.rendered["des"]):
            if opt[1].collidepoint(pg.mouse.get_pos()):
                if self.last_option != opt:
                    self.button_hover.sound.play()
                    self.last_option = opt
    def mouse_menu_click(self, event):
        '''select menu option '''
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            for i,opt in enumerate(self.rendered["des"]):
                if opt[1].collidepoint(pg.mouse.get_pos()):
                    self.selected_index = i
                    self.select_option(i)
                    break
    def pre_render_options(self):
        '''render menu options based on selected or deselected'''
        font_deselect = tools.Font.load('impact.ttf', 50)
        font_selected = tools.Font.load('impact.ttf', 75)

        rendered_msg = {"des":[],"sel":[]}
        for option in self.options:
            d_rend = font_deselect.render(option, 1, (255,255,255))
            d_rect = d_rend.get_rect()
            s_rend = font_selected.render(option, 1, (255,255,0))
            s_rect = s_rend.get_rect()
            rendered_msg["des"].append((d_rend,d_rect))
            rendered_msg["sel"].append((s_rend,s_rect))
        self.rendered = rendered_msg

    def select_option(self, i):
        '''select menu option via keys or mouse'''
        if i == len(self.next_list):
            self.quit = True
        else:
            self.button_sound.sound.play()
            self.next = self.next_list[i]
            self.done = True
            self.selected_index = 0

    def change_selected_option(self, op=0):
        '''change highlighted menu option'''
        for i,opt in enumerate(self.rendered["des"]):
            if opt[1].collidepoint(pg.mouse.get_pos()):
                self.selected_index = i
        if op:
            self.button_hover.sound.play()
            self.selected_index += op
            max_ind = len(self.rendered['des'])-1
            if self.selected_index < 0:
                self.selected_index = max_ind
            elif self.selected_index > max_ind:
                self.selected_index = 0
