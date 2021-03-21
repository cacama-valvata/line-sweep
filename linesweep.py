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


def intersection_y (line, x):
	y_value = (line.m * x) + line.b
	return y_value


def within_bounds (intersection, mode, line1, line2):
	if mode == "x":
		# endpoint1 must be the lower bound
		if (intersection >= line1.endpoint1.x) and (intersection <= line1.endpoint2.x):
			if (intersection >= line2.endpoint1.x) and (intersection <= line2.endpoint2.x):
				return True
		return False

	elif mode == "y":
		# endpoint1 or 2 may be the lower bound
		if (intersection >= line1.endpoint1.y) and (intersection <= line1.endpoint2.y):
			if (intersection >= line2.endpoint1.y) and (intersection <= line2.endpoint2.y):
				return True
		if (intersection >= line1.endpoint2.y) and (intersection <= line1.endpoint1.y):
			if (intersection >= line2.endpoint2.y) and (intersection <= line2.endpoint1.y):
				return True
		return False
	else:
		print("???")


def close_line(i, open_lines):
	for j in open_lines:
		if i.line_no == j.line_no:
			open_lines.remove(j)
			return True
	return False

'''
def mergesort (array):
	if len(array) == 2:
		if array[0].x > array[1].x:
			temp = array[0]
			array[0] = array[1]
			array[1] = temp
		return array
'''

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
	#points = mergesort(points)
	#for i in points:
	#	print(i.x)

	points = sorted(points, key=lambda Point: Point.x)

	''' Check intersections'''
	counter = 0
	open_lines = []

	for i in points:
		if close_line(i, open_lines):
			continue
		else:
			for j in open_lines:
				x_value = intersection_x(i, j)
				y_value = intersection_y(i, x_value)
				if within_bounds(x_value, "x", i, j) and within_bounds(y_value, "y", i, j):
					counter += 1
			open_lines.append(i)

	''' Write to file '''
	with open("output.txt", "w") as f:
		f.write(str(counter))


''' Start of execution '''
main()