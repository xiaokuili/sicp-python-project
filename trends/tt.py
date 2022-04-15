from shapely.geometry import Polygon


coords = ((1., 2.), (3., 4.), (5., 0.), (1., 2.))
some_poly = Polygon(coords)
p = some_poly.centroid
print(p.x, p.y)