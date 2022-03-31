class Color:
    """
    The responsibility of Color is to hold and provide information about itself. Color has a few 
    convenience methods for comparing them and converting to a tuple.
    """
    
    def __init__(self, red, green, blue, alpha = 255):
        """Constructs a new Color using the specified red, green, blue and alpha values. The alpha 
        value is the color's opacity.
        """
        self._red = red
        self._green = green
        self._blue = blue 
        self._alpha = alpha

    def to_tuple(self):
        #Gets the color as a tuple of four values (red, green, blue, alpha).
        return (self._red, self._green, self._blue, self._alpha)   

    