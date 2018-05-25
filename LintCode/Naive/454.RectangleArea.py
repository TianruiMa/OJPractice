class Rectangle:
    """
     * Define a constructor which expects two parameters width and height here.
    """

    # write your code here
    def __init__(self, w, h):
        self.width = w
        self.height = h

    '''
     * Define a public method `getArea` which can calculate the area of the
     * rectangle and return.
    '''

    # write your code here
    def getArea(self):
        return self.width * self.height
