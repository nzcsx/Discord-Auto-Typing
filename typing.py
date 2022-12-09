from Xlib import display
from PIL import ImageGrab
from pynput.keyboard import Controller
import time
import datetime
import random

def get_cursor_pos():
    data = display.Display().screen().root.query_pointer()._data
    return data['root_x'], data['root_y']

def get_active_win():
    win_class = display.Display().get_input_focus().focus.get_wm_class()
    if win_class is None:
        return '',''
    else:
        return win_class[0], win_class[1]
    
def get_pixel_clr(x,y):
    pic = ImageGrab.grab().load()
    return pic[x,y]

def delay_and_type(keyboard, sleep_t, string):
    time.sleep(sleep_t)
    keyboard.type(string)


if __name__ == '__main__':
    
    time.sleep(3)
    keyboard = Controller()
    t_prev = time.time() - 3600
    
    while (True):
        t_now = time.time()
        
        '''
        time.sleep(5)
        x, y = get_cursor_pos()
        print(x, " ", y, " ", get_pixel_clr(x,y))
        '''
        
        if (t_now - t_prev >= 3600):
            
            '''get screen info'''
            #pixel_clr = get_pixel_clr(374, 107)
            win_name, win_title = get_active_win()
            
            '''type !work'''
            if (win_title == 'WebCord'): #and pixel_clr == (60, 132, 199)):
                delay_and_type(keyboard, random.uniform(2,3), '!work\n')
            
            '''update time'''
            t_prev = time.time()
            
            
            '''type !daily !coins !rank'''
            if (datetime.datetime.now().hour == 11 or datetime.datetime.now().hour == 12):
                delay_and_type(keyboard, random.uniform(2,4), '!daily\n')
                delay_and_type(keyboard, random.uniform(2,4), '!coins\n')
                delay_and_type(keyboard, random.uniform(2,4), '!rank\n')
            
        