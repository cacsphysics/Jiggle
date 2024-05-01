# graphics/color.py
class Color():
	def __init__(self, red: int, green: int, blue: int):
		self._red = red
		self._green = green
		self._blue = blue
		self._normal = self.normalized(self)
 
	@property
	def value(self) -> tuple[int,int,int]:
		return (self._red, self._green, self._blue)
	
	@value.setter
	def value(self, value: tuple[int,int,int]):
		self._red = value[0]
		self._green = value[1]
		self._blue = value[2]
		self._normal = self.normalized(self)
  
	@property
	def normal(self):
		return self._normal
  
	@staticmethod
	def normalized(color):
		val = color.value
		n_color = tuple(channel / 255 for channel in val)
		return n_color

#PREDEFINED COLORS
color_predef = {'white' : Color(255,255,255),
        'black'  : Color(000,000,000), 
        'red'    : Color(255,000,000),
        'green'  : Color(000,255,000),
        'blue'   : Color(000,000,255)}