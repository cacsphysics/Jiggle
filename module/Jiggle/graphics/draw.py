from OpenGL.GL import *
from math import cos, sin, pi

class Draw():
	@staticmethod
	def point(x: float, y: float, color: tuple[float,float,float]):
		glColor3f(*color)
		glBegin(GL_POINTS)
		glVertex2f(x, y)
		glEnd()

	@staticmethod
	def line(x1: float, y1:float, x2:float, y2:float, color: tuple[float,float,float]):
		glColor3f(*color)
		glBegin(GL_LINES)
		glVertex2f(x1, y1)
		glVertex2f(x2, y2)
		glEnd()

	@staticmethod
	def rectangle(x: float, y: float , width: float, height: float, rotation:float, color: tuple[float,float,float]):
		glPushMatrix()
		glTranslatef(x, y, 0)
		glRotatef(-rotation, 0, 0, 1)

		glColor3f(*color)
		w_center = width/2
		h_center = height/2
		
		glBegin(GL_QUADS)
		glVertex2f(-w_center, -h_center)
		glVertex2f(w_center, -h_center)
		glVertex2f(w_center, h_center)
		glVertex2f(-w_center, h_center)
		
		glEnd()
		glPopMatrix()

	@staticmethod
	def polygon(x:float, y:float, vertices: tuple[tuple[float,float],...], rotation: float, color: tuple[float,float,float]):
		glPushMatrix()
		glTranslatef(x, y, 0)
		glRotate(-rotation, 0 ,0 ,1)
		glColor3f(*color)
		
		glBegin(GL_POLYGON)
		for vertex in vertices:
			glVertex2f(vertex.x, vertex.y)
		
		glEnd()
		glPopMatrix()

	@staticmethod
	def circle(x: float, y: float, radius: float, rotation: float, color: tuple[float, float, float], num_segments=12):
		glPushMatrix()
		glTranslatef(x, y, 0)
		glRotatef(-rotation, 0, 0, 1)
		glColor3f(*color)
		
		glBegin(GL_TRIANGLE_FAN)
		glVertex2f(0, 0)
		for i in range(num_segments + 1):
			angle = 2.0 * pi * i / num_segments
			vertex_x = radius * cos(angle)
			vertex_y = radius * sin(angle)
			glVertex2f(vertex_x, vertex_y)
		
		glEnd()
		glPopMatrix()
