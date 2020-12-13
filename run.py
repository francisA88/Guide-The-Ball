import sys
try:
	from main import run
	run()
except ImportError:
	'''Means I forgot something or you have not yet run build.py'''
	from main import MainActivity
	MainActivity().run()
#import kivy