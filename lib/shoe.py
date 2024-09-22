class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size
        self.condition = "new"  
    class Shoe:
        """
        A class representing a shoe with attributes like brand, size, and condition.
    
        Attributes
        ----------
        brand : str
            The brand of the shoe.
        _size : int
            The private size of the shoe.
        condition : str
            The condition of the shoe.
    
        Methods
        -------
        __init__(brand, size)
            Initializes a new Shoe object with the given brand and size.
    
        size: property
            A property that gets and sets the size of the shoe.
    
        cobble()
            Changeing the condition of the shoe to 'New' and prints a message.
        """
    
        def __init__(self, brand, size):
            """
            Initializes a new Shoe object with the given brand and size.
    
            Parameters
            ----------
            brand : str
                The brand of the shoe.
            size : int
                The size of the shoe.
            """
            self.brand = brand
            self._size = None
            self.size = size
            self.condition = "new"
    
        @property
        def size(self):
            """
            Returns the size of the shoe.
    
            Returns
            -------
            int
                The size of the shoe.
            """
            return self._size
    
        @size.setter
        def size(self, value):
            """
            Sets the size of the shoe.
    
            Parameters
            ----------
            value : int
                The new size of the shoe. If the value is not an integer, prints an error message.
            """
            if isinstance(value, int):
                self._size = value
            else:
                print("size must be an integer")
    
        def cobble(self):
            """
            Changes the condition of the shoe to 'New' and prints a message.
            """
            self.condition = "New"  
            print("Your shoe is as good as new!")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"  
        print("Your shoe is as good as new!")  
