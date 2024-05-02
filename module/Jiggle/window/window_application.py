import glfw
from OpenGL.GL import *
from .window_abstraction import AbstractWindow

class ApplicationWindow(AbstractWindow):
	def __init__(self, width: int, height: int, title = "Jiggle Application"):
		super().__init__(width, height, title)
		self.create()

	def create(self):
		# Initialize GLFW
		if not glfw.init():
			print("Failed to initialize GLFW")
			return

		# Create a windowed mode window and its OpenGL context
		self._window = glfw.create_window(self._width, self._height, self._title, None, None)
		if not self._window:
			glfw.terminate()
			print("Failed to create GLFW window")
			return

		# Make the window's context current
		glfw.make_context_current(self._window)

		# Set up the orthographic projection with (0, 0) at the center of the screen
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glOrtho(-self._width / 2, self._width / 2, -self._height / 2, self._height / 2, -1, 1)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

	def close(self):
		pass

	def draw(self):
		pass

	def update(self):
		pass

	def run(self):
		while not glfw.window_should_close(self._window):
			glClear(GL_COLOR_BUFFER_BIT)
			glfw.poll_events()
			self.on_update()
			self.on_draw()
			glfw.swap_buffers(self._window)
			

	def on_draw(self):
		self.draw()

	def on_update(self):
		self.update()

	def on_close(self):
		self.close()
