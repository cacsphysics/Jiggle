import glfw
import imgui
from imgui.integrations.glfw import GlfwRenderer
from OpenGL.GL import *
from .window_abstraction import AbstractWindow
from SpringBox.Time.clock import Clock

class ApplicationWindow(AbstractWindow):
	def __init__(self, width: int, height: int, title = "Jiggle Application Window"):
		super().__init__(width, height, title)
		self._clock = Clock()
		self._window_init()
		self._gui_renderer = self._gui_init()
		self._gui_elements = []

	def _window_init(self):
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

	def _gui_init(self):
		# Initialize ImGui
		imgui.create_context()
		imgui.get_io().fonts.add_font_default()
		return GlfwRenderer(self._window)

	@property
	def clock(self) -> Clock:
		return self._clock

	@property
	def gui_renderer(self) -> GlfwRenderer:
		return self._gui_renderer

	def clear_screen(self):
		glClear(GL_COLOR_BUFFER_BIT)

	def poll_events(self):
		glfw.poll_events()

	def flip(self):
		glfw.swap_buffers(self._window)

	def run(self):
		while not glfw.window_should_close(self._window):
			self.poll_events()
			self.on_update()
			self.clear_screen()
			self.on_draw()
			self.flip()
			self._clock.tick()

	def draw(self):
		pass

	def _gui_draw(self):
		imgui.render()
		self._gui_renderer.render(imgui.get_draw_data())

	def update(self):
		pass

	def _gui_update(self):
		self._gui_renderer.process_inputs()
		imgui.new_frame()
		for element in self._gui_elements:
			element()

	def close(self):
		pass

	def on_draw(self):
		self.draw()
		self._gui_draw()

	def on_update(self):
		self.update()
		self._gui_update()

	def on_close(self):
		self._gui_renderer.shutdown()
		glfw.terminate()
		self.close()
