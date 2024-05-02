from setuptools import setup, find_packages

setup(
	name='Jiggle',
	version='0.0.3',
	packages=find_packages(),
	install_requires=[
		'PyOpenGL>=3.1.7',
		'glfw>=2.7.0',
		'Numberful>=0.0.1',
		'SpringBox>=0.0.1'
  		],
	
	author='Kevin Ferry Jr.',
	author_email='kevinferrydesign@gmail.com',
	description='A simple game engine toolkit module for python!',
	url='https://github.com/KevinFerryJr/JiggleEngine',
)