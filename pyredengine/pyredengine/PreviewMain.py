# Main project file
import pygame, sys, os


class MainGame:
    def __init__(self) -> None:
        pygame.init()

        self._init_display()
        self.clock = pygame.time.Clock()
        self.run = True
        
        self.mouse_pos = (0,0) 

        
    def _init_display(self, resolution = [1280, 720], caption = "Pygame Window"): # Don't touch 
        """Initialises the display to be rendered within the viewport window of the engine"""
        self._hwnd = None
        if len(sys.argv) > 1:
            self._hwnd = int(sys.argv[1])
            os.environ['SDL_WINDOWID'] = str(self._hwnd)
        
        self.display_width = resolution[0]
        self.display_height = resolution[1]
        
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (-1000, -1000)
        self.display = pygame.display.set_mode((self.display_width, self.display_height), pygame.NOFRAME)
        pygame.display.set_caption(caption)
        
    def _send_event(self, type, key = None, mouse = None):
        """Manages event handling between viewport window and the game
           Mouse = x, y, button_down(type)
        
        """
    
        if type == 1: # Keyboard press
            event = pygame.event.Event(pygame.KEYDOWN, {'key': key})
            pygame.event.post(event)
            
        elif type == 2: # Mouse Movement
            mouse_x, mouse_y, mouse_down = mouse
            self.mouse_rel = mouse_x - self.mouse_pos[0], mouse_y - self.mouse_pos[1]
                                  
            event = pygame.event.Event(pygame.MOUSEMOTION, {'pos': (mouse_x, mouse_y), 'rel': (self.mouse_rel[0], self.mouse_rel[1]) , 'buttons': pygame.mouse.get_pressed()})
            pygame.event.post(event)
            
            self.mouse_pos = mouse_x, mouse_y   
            
        elif type == 3: # Mouse Press
            mouse_x, mouse_y, mouse_down = mouse
            self.mouse_rel = mouse_x - self.mouse_pos[0], mouse_y - self.mouse_pos[1]
                   
            event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"button": mouse_down, "pos": (mouse_x, mouse_y)})
            pygame.event.post(event)
            
            self.mouse_pos = mouse_x, mouse_y   

        elif type == 4: # Mouse Release
            mouse_x, mouse_y, mouse_up = mouse
            self.mouse_rel = mouse_x - self.mouse_pos[0], mouse_y - self.mouse_pos[1]
                       
            event = pygame.event.Event(pygame.MOUSEBUTTONUP, {"button": mouse_up, "pos": (mouse_x, mouse_y)})
            pygame.event.post(event)
            
            self.mouse_pos = mouse_x, mouse_y   



    def handle_events(self):
        """Handles custom user events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            
    def update(self):
        """Put all your custom logic here"""
        pass
    
    def draw(self):
        """Custom drawing logic here"""
        pygame.display.flip()
    
    def on_reload(self):
        pass
        
        
    def on_save(self):
        pass
    
    
    def run_game(self):
        """Handles the running of the game"""
        
        while self.run: # Don't touch
            self.clock.tick()
            self.handle_events()
            self.update()
            self.draw()
            
            yield self.display

        pygame.quit()
        sys.exit()
        
    def close_game(self):
        self.run = False
        pygame.quit()
    
