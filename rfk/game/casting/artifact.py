from game.casting.actor import Actor
# from game.shared.color import Color
# from game.shared.point import Point

class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        # """Constructs a new Actor."""
        # self._text = ""
        # self._font_size = 15
        # self._color = Color(255, 255, 255)
        # self._position = Point(0, 0)
        self._message = ""

    # def get_color(self):
    #     """Gets the actor's color as a tuple of three ints (r, g, b).
        
    #     Returns:
    #         Color: The actor's text color.
    #     """
    #     return self._color

    # def get_font_size(self):
    #     """Gets the actor's font size.
        
    #     Returns:
    #         Point: The actor's font size.
    #     """
    #     return self._font_size

    # def get_position(self):
    #     """Gets the actor's position in 2d space.
        
    #     Returns:
    #         Point: The actor's position in 2d space.
    #     """
    #     return self._position
    
    # def get_text(self):
    #     """Gets the actor's textual representation.
        
    #     Returns:
    #         string: The actor's textual representation.
    #     """
    #     return self._text

    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    # def set_color(self, color):
    #     """Updates the color to the given one.
        
    #     Args:
    #         color (Color): The given color.
    #     """
    #     self._color = color

    # def set_position(self, position):
    #     """Updates the position to the given one.
        
    #     Args:
    #         position (Point): The given position.
    #     """
    #     self._position = position
    
    # def set_font_size(self, font_size):
    #     """Updates the font size to the given one.
        
    #     Args:
    #         font_size (int): The given font size.
    #     """
    #     self._font_size = font_size
    
    # def set_text(self, text):
    #     """Updates the text to the given value.
        
    #     Args:
    #         text (string): The given value.
    #     """
    #     self._text = text

    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message 