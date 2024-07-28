class Rectangle:
    __width,__height

    def init(self,width,height):
        self.width=width
        self.height=height

    def get_width(self):
        return self.__width
    
    def set_width(self,width):
        if(width>0):
            self._width=width
        else:
            print("Invalid Width")

    