from Numberful import vector

class Entity2D:
	def __init__(self):
		self._position = vector.Vec2(0,0)
		self._rotation = 0.0
		self._physics_body = None
		self._shape = None
		self._collider = None

	@property
	def position(self) -> tuple[float, float]:
		return self._position.value

	@position.setter
	def position(self, value: tuple[float, float]):
		if self._physics_body:
			self._physics_body.position = value

		self._position.value = value

	@property
	def rotation(self) -> float:
		return self._rotation

	@rotation.setter
	def rotation(self, value: float):
		if self._physics_body:
			self._physics_body.rotation = value
		
		self._rotation = value

	def update(self, delta_time):
		if self._physics_body:
			self._physics_body.update(delta_time)
			self._position = self._physics_body.position

		if self._shape:
			self._shape.pos = self._position.value

	def draw(self):
		if self._shape:
			self._shape.draw()