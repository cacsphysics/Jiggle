from Jiggle.graphics.draw import Draw
from Jiggle.graphics.color import Color
from Numberful import geometry


class Point2D(geometry.Point2D):
	def __init__(self, pos: tuple[float, float], color: tuple[int, int, int]):
		super().__init__(pos)
		self._color = Color(*color)

	@property
	def color(self) -> Color:
		return self._color

	@color.setter
	def color(self, value: Color):
		self._color = value

	def draw(self):
		Draw.point(*self._pos.value, self._color.normal)


class Line2D(geometry.Line2D):
	def __init__(self, start: tuple[float, float], end: tuple[float,float], color: tuple[int,int,int]):
		super().__init__(start, end)
		self._color = Color(*color)

	@property
	def color(self) -> Color:
		return self._color

	@color.setter
	def color(self, value: Color):
		self._color = value
	
	def draw(self):
		Draw.line(*self._start.value, *self._end.value, self._color.normal)


class Rectangle(geometry.Rectangle):
	def __init__(self, pos: tuple[float,float], width: float, height: float, rotation:float, color: tuple[int,int,int]):
		super().__init__(pos, width, height, rotation)
		self._color = Color(*color)

	@property
	def color(self) -> Color:
		return self._color

	@color.setter
	def color(self, value: Color):
		self._color = value
 
	def draw(self):
		Draw.rectangle(*self._pos.value, *self.size, self._rotation.value, self._color.normal)


class Polygon(geometry.Polygon):
	def __init__(self, pos: tuple[float, float], verts: tuple[tuple[float, float], ...], rotation: float, color: tuple[int,int,int]):
		super().__init__(pos, verts, rotation)
		self._color = Color(*color)

	@property
	def color(self) -> Color:
		return self._color

	@color.setter
	def color(self, value: Color):
		self._color = value

	def draw(self):
		Draw.polygon(*self._pos.value, self._verts, self._rotation.value, self._color.normal)


class Circle(geometry.Circle):
	def __init__(self, pos: tuple[float, float], radius: float,rotation: float, color: tuple[int,int,int]):
		super().__init__(pos, radius, rotation)
		self._color = Color(*color)

	def draw(self):
		Draw.circle(*self._pos.value, self._radius, self._rotation.value, self._color.normal)