import pygame

class BGM():
    """A class for all the background sounds."""
    
    def __init__(self):
        """Initialize sound effects."""
        self.bullets_sound=pygame.mixer.Sound(r'F:\SFX\bow_release _edited.wav')
        self.game_over= pygame.mixer.Sound(r'F:\SFX\failure-1-89170.mp3')
    
    def shoot(self):
        """Play sound effect of bullet."""
        self.bullets_sound.play()   
    
    def crash(self):
        """Play sound effect of game over."""
        self.game_over.play()