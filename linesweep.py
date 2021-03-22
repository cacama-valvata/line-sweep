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


def intersection_x (line1, line2):
	x_value = (line1.b - line2.b) / (line2.m - line1.m)
	return x_value


def within_bounds (intersection, line1, line2):
	# endpoint1 must be the lower bound
	if (intersection >= line1.endpoint1.x) and (intersection <= line1.endpoint2.x):
		if (intersection >= line2.endpoint1.x) and (intersection <= line2.endpoint2.x):
			return True
	return False


def close_line(i, open_lines):
	for j in open_lines:
		if i.line_no == j.line_no:
			open_lines.remove(j)
			return True
	return False


def mergesort (array):
	pass


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
	points = sorted(points, key=lambda Point: Point.x)

	#points = mergesort(points)
	#for i in points:
	#	print(i.x)


	''' Check intersections'''
	counter = 0
	open_lines = []

	for i in points:
		if close_line(i, open_lines):
			continue
		else:
			for j in open_lines:
				x_value = intersection_x(lines[i.line_no], lines[j.line_no])
				if within_bounds(x_value, lines[i.line_no], lines[j.line_no]):
					counter += 1
			open_lines.append(i)

	''' Write to file '''
	with open("output.txt", "w") as f:
		f.write(str(counter))


''' Start of execution '''
main()