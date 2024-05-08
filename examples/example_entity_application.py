import Jiggle
import SpringBox

entity = Jiggle.entities.entity.Entity2D()
entity._shape = Jiggle.Graphics.Circle((0,0),10,0,(255,255,0))
entity._physics_body = SpringBox.Body.PhysBody2D()
entity.position = (0, 300)

class Application(Jiggle.Window.ApplicationWindow):
	def __init__(self, window_size: tuple):
		super().__init__(*window_size)
		self._entity = entity

	def update(self):
		self._entity.update(self.clock.delta_time)

	def draw(self):
		self._entity.draw()

app = Application((800,600))
app.run()