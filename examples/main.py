import Jiggle

win = Jiggle.Window.ApplicationWindow(800,600,"Jiggle Window")

#Variables for Testing
polygon_verts = ((50,50), (0,100), (-50, 50), (-50, -50), (50, -50))
global_rotation = 0

def update_fn():
	global global_rotation
	global_rotation -= 1

def draw_fn():
	Jiggle.Graphics.Draw.line(-400,0,400,0,(255,255,255))
	Jiggle.Graphics.Draw.line(0,-300,0,300,(255,255,255))
	
	Jiggle.Graphics.Draw.circle(100, 100, 100, global_rotation, (0,1,0))
	Jiggle.Graphics.Draw.rectangle(-100, -100, 125, 125, global_rotation, (1,0,0))
	Jiggle.Graphics.geometry.Circle((-200,50), 50, global_rotation, (0,0,255)).draw()
	Jiggle.Graphics.geometry.Polygon((100, -150), polygon_verts, global_rotation, (255,255,0)).draw()

win.draw = draw_fn
win.update = update_fn
win.run()
