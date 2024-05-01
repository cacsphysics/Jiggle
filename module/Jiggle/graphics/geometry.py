import Jiggle.logging.error
from Jiggle.graphics.draw import Draw
from Jiggle.graphics.color import Color
from Numberful.vector import Vector, Vec2, Vec3

class Calculate():
	@staticmethod
	def polygon_centroid(vertices) -> tuple[float,float]:
		avg_x = sum(vertex[0] for vertex in vertices) / len(vertices)
		avg_y = sum(vertex[1] for vertex in vertices) / len(vertices)
		
		return (avg_x, avg_y)
	
	@staticmethod
	def polyhedron_centroid(vertices) -> tuple[float,float,float]:
		# Number of vertices
		n = len(vertices)
		
		# Initialize variables for centroid coordinates and total area
		cx = cy = area = 0
		
		# Iterate over each vertex
		for i in range(n):
			# Get current and next vertex
			current_vertex = vertices[i]
			next_vertex = vertices[(i + 1) % n]  # Wrap around to the first vertex for the last iteration
			
			# Compute the cross product to get the signed area of the triangle formed by the origin and the current and next vertices
			cross_product = (current_vertex[0] * next_vertex[1]) - (next_vertex[0] * current_vertex[1])
			
			# Update the total area
			area += cross_product
			
			# Update the centroid coordinates (weighted by the area)
			cx += (current_vertex[0] + next_vertex[0]) * cross_product
			cy += (current_vertex[1] + next_vertex[1]) * cross_product
		
		# Divide the centroid coordinates by 3 times the total area
		cx /= (3 * area)
		cy /= (3 * area)
		
		return (cx, cy)

class Angle():
	def __init__(self, value: float):
		self._value = value % 360
		
	@property
	def value(self) -> float:
		return self._value

	@value.setter
	def value(self, value: float):
		self._value = value

	def __add__(self, other):
		if type(other) == Angle:
			return Angle(self.value + other.value)
		else:
			raise TypeError(error.Message.operator_overload(self,other, "+"))
	
	def __sub__(self, other):
		if type(other) == Angle:
			return Angle(self.value - other.value)
		else:
			raise TypeError(error.Message.operator_overload(self,other, "-"))
	
	def __mul__(self, other):
		if type(other) == Angle:
			return Angle(self.value * other.value)
		else:
			raise TypeError(error.Message.operator_overload(self,other, "*"))

	def __truediv__(self, other):
		if type(other) == Angle:
			return Angle(self.value / other.value)
		else:
			raise TypeError(error.Message.operator_overload(self,other, "/"))

class Point2D():
	def __init__(self, pos: tuple[float, float], color: tuple[int, int, int]):
		self._pos = Vec2(*pos)
		self._color = Color(*color)

	@property
	def pos(self) -> tuple[float, float]:
		return self._pos.value
	
	@pos.setter
	def pos(self, value: tuple[float, float]):
		pos.value = value

	@property
	def color(self) -> Color:
		return self._color

	@color.setter
	def color(self, value: Color):
		self._color = value

	def draw(self):
		Draw.point(*self._pos.value, self._color.normal)

class Line2D():
	def __init__(self, start: tuple[float, float], end: tuple[float,float], color: tuple[int,int,int]):
		self._color = Color(*color)
		self._start = Vec2(*start)
		self._end = Vec2(*end)
	
	@property
	def start(self) -> Vec2:
		return self._start.value
	
	@start.setter
	def start(self, value: tuple[float, float]):
		self._start.value = value

	@property
	def end(self) -> Vec2:
		return self._end
	
	@end.setter
	def end(self, value: tuple[float, float]):
		self._end.value = value

	@property
	def points(self) -> tuple[Vec2, Vec2]:
		return (self._start, self._end)

	@property
	def color(self) -> Color:
		return self._color

	@color.setter
	def color(self, value: Color):
		self._color = value
	
	def draw(self):
		Draw.line(*self._start.value, *self._end.value, self._color.normal)

#--- SHAPE CLASSES ---#
class Shape:
	def __init__(self, pos: tuple[float, float], rotation: float, color: tuple[int,int,int]):
		self._pos = Vec2(*pos)
		self._rotation = Angle(rotation)
		self._color = Color(*color)

	@property
	def pos(self) -> Vec2:
		return self._pos
	
	@pos.setter
	def pos(self, value: tuple[float, float]):
		self._pos.value = value

	@property
	def rotation(self) -> float:
		return self._rotation.value

	@rotation.setter
	def rotation(self, value):
		self._rotatation.value = value

	@property
	def color(self) -> Color:
		return self._color

	@color.setter
	def color(self, value: Color):
		self._color = value

class Rectangle(Shape):
	def __init__(self, pos: tuple[float,float], width: float, height: float, rotation:float, color: tuple[int,int,int]):
		super().__init__(pos, rotation, color)
		self._width = width
		self._height = height

	@property
	def width(self) -> float:
		return self._width

	@width.setter
	def width(self, value: float):
		self._width = value

	@property
	def height(self) -> float:
		return self._height

	@height.setter
	def height(self, value: float):
		self._height = value

	@property
	def size(self):
		return (self._width, self._height)

	def draw(self):
		Draw.rectangle(*self._pos.value, *self.size, self._rotation.value, self._color.normal)

class Polygon(Shape):
	def __init__(self, pos: tuple[float, float], verts: tuple[tuple[float, float], ...], rotation: float, color: tuple[int,int,int]):
		super().__init__(pos, rotation, color)
		self._verts = Vector.vectorize(Vec2, verts)

	def draw(self):
		Draw.polygon(*self._pos.value, self._verts, self._rotation.value, self._color.normal)

class Circle(Shape):
	def __init__(self, pos: tuple[float, float], radius: float,rotation: float, color: tuple[int,int,int]):
		super().__init__(pos, rotation, color)
		self._radius = radius

	@property
	def radius(self) -> float:
		return self._radius

	@radius.setter
	def radius(self, value: float):
		self._radius = value

	def draw(self):
		Draw.circle(*self._pos.value, self._radius, self._rotation.value, self._color.normal)