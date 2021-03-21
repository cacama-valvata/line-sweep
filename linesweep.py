'''
Line Sweep Algorithm in Python
Casey Colley
'''

class Point:
	def __init__(self, x, y, line_no):
		self.x = x
		self.y = y
		self.line_no = line_no

class Line:
	def __init__(self, endpoint1, endpoint2):
		self.endpoint1 = endpoint1
		self.endpoint2 = endpoint2
		self.m = (endpoint1.y - endpoint2.y) / (endpoint1.x - endpoint2.x)
		self.b = endpoint1.y - (self.m * endpoint1.x)


def intersection_x (line1_m, line1_b, line2_m, line2_b):
	pass


def within_bounds (intersection, line1_e1, line1_e2, line2_e1, line2_e2):
	pass


def mergesort (array)


def main ():
	''' Reading of file '''
	points = []
	lines = []

	with open("input1.txt", "r") as f:
		input_line = f.readlines()
	for i in input_line:
		coords = i.split("\t")
		n = input_line.index(i)

		e1 = Point(int(coords[0]), int(coords[1]), n)
		e2 = Point(int(coords[2]), int(coords[3]), n)
		li = Line(e1, e2)

		points.append(e1)
		points.append(e2)
		lines.append(li)

	''' Sort points '''
	points = mergesort(points)

	''' Check intersections'''
	counter = 0

	''' Write to file '''
	with open("output.txt", "w") as f:
		f.write(str(counter))


''' Start of execution '''
main()