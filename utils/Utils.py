"""
Utilities
Author: dentou
"""

from model.Point import Point
from pygame.math import Vector2
from math import sin, cos, pi


def rotate_point(point, pivot, angle):
	"""
	Return rotated point around pivot (the old point is not rotated)
	:param point: point to be rotated (won't be changed)
	:param pivot: pivot point
	:param angle: in degrees, positive means counter-clockwise rotation
	:return: rotated point
	"""

	vector = Vector2(point.x - pivot.x, point.y - pivot.y)
	rotated_vector = rotate_vector(vector, angle)

	px = rotated_vector.x + pivot.x
	py = rotated_vector.y + pivot.y

	return Point(px, py)


def rotate_vector(vector, angle):
	"""
	:param vector: vector to be rotated (won't be changed)
	:param angle: in degrees, positive means counter-clockwise rotation
	:return: rotated vector
	"""
	vx = vector.x
	vy = vector.y

	s = sin(angle * pi / 180)
	c = cos(angle * pi / 180)

	new_vy = vy * c - vx * s
	new_vx = vy * s + vx * c

	return Vector2(new_vx, new_vy)
