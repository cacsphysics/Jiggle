import Jiggle

class Application(Jiggle.Window.ApplicationWindow):
	def __init__(self, window_size: tuple):
		super().__init__(*window_size)
		
  		#Example properties
		self._polygon_verts = ((50,50), (0,100), (-50, 50), (-50, -50), (50, -50))
		self._shape_rotation = 0

	def update(self):
  		#Delta time for physics updates
		self._shape_rotation -= 90 * self._clock.delta_time

	def draw(self):
		#Jiggle.Graphics.Draw.line(-400,0,400,0,(255,255,255))
		#Jiggle.Graphics.Draw.line(0,-300,0,300,(255,255,255))
		
		Jiggle.Graphics.Draw.circle(100, 100, 100, self._shape_rotation, (0,1,0))
		Jiggle.Graphics.Draw.rectangle(-100, -100, 125, 125, self._shape_rotation, (1,0,0))
		Jiggle.Graphics.geometry.Circle((-200,50), 50, self._shape_rotation, (0,0,255)).draw()
		Jiggle.Graphics.geometry.Polygon((100, -150), self._polygon_verts, self._shape_rotation, (255,255,0)).draw()

app = Application((800,600))
app.run()