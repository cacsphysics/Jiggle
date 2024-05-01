from abc import ABC, abstractmethod

class AbstractWindow(ABC):
	def __init__(self, width: int, height: int, title: str):
		self._width = width
		self._height = height
		self._title = title
		self._window = None
  
	@abstractmethod
	def create(self):
		pass

	@abstractmethod
	def close(self):
		pass

	@abstractmethod
	def draw(self):
		pass

	@abstractmethod
	def update(self):
		pass

	@abstractmethod
	def run(self):
		pass

	@abstractmethod
	def on_draw(self):
		self.draw()
  
	@abstractmethod
	def on_update(self):
		self.update

	@abstractmethod
	def on_close(self):
		self.close()

	@property
	def width(self) -> int:
		return self._width

	@property
	def height(self) -> int:
		return self._height

	@property
	def size(self):
		return self._width, self._height

	@property
	def window(self):
		return self._window

	@property
	def event_manager(self):
		return self._event_manager