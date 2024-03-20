import typing
import mathutils

GenericType = typing.TypeVar("GenericType")

def area_tri(
    v1: typing.Union["mathutils.Vector", typing.Sequence[float]],
    v2: typing.Union["mathutils.Vector", typing.Sequence[float]],
    v3: typing.Union["mathutils.Vector", typing.Sequence[float]],
) -> float:
    """Returns the area size of the 2D or 3D triangle defined.

    :param v1: Point1
    :type v1: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param v2: Point2
    :type v2: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param v3: Point3
    :type v3: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :rtype: float
    """

    ...

def barycentric_transform(
    point: typing.Union["mathutils.Vector", typing.Sequence[float]],
    tri_a1: typing.Union["mathutils.Vector", typing.Sequence[float]],
    tri_a2: typing.Union["mathutils.Vector", typing.Sequence[float]],
    tri_a3: typing.Union["mathutils.Vector", typing.Sequence[float]],
    tri_b1: typing.Union["mathutils.Vector", typing.Sequence[float]],
    tri_b2: typing.Union["mathutils.Vector", typing.Sequence[float]],
    tri_b3: typing.Union["mathutils.Vector", typing.Sequence[float]],
) -> typing.Any:
    """Return a transformed point, the transformation is defined by 2 triangles.

    :param point: The point to transform.
    :type point: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param tri_a1: source triangle vertex.
    :type tri_a1: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param tri_a2: source triangle vertex.
    :type tri_a2: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param tri_a3: source triangle vertex.
    :type tri_a3: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param tri_b1: target triangle vertex.
    :type tri_b1: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param tri_b2: target triangle vertex.
    :type tri_b2: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param tri_b3: target triangle vertex.
    :type tri_b3: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :rtype: typing.Any
    :return: The transformed point
    """

    ...

def box_fit_2d(points: typing.List) -> float:
    """Returns an angle that best fits the points to an axis aligned rectangle

    :param points: list of 2d points.
    :type points: typing.List
    :rtype: float
    :return: angle
    """

    ...

def box_pack_2d(boxes: typing.List) -> typing.Tuple:
    """Returns a tuple with the width and height of the packed bounding box.

    :param boxes: list of boxes, each box is a list where the first 4 items are [x, y, width, height, ...] other items are ignored.
    :type boxes: typing.List
    :rtype: typing.Tuple
    :return: the width and height of the packed bounding box
    """

    ...

def closest_point_on_tri(
    pt: typing.Union["mathutils.Vector", typing.Sequence[float]],
    tri_p1: typing.Union["mathutils.Vector", typing.Sequence[float]],
    tri_p2: typing.Union["mathutils.Vector", typing.Sequence[float]],
    tri_p3: typing.Union["mathutils.Vector", typing.Sequence[float]],
) -> "mathutils.Vector":
    """Takes 4 vectors: one is the point and the next 3 define the triangle.

    :param pt: Point
    :type pt: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param tri_p1: First point of the triangle
    :type tri_p1: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param tri_p2: Second point of the triangle
    :type tri_p2: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param tri_p3: Third point of the triangle
    :type tri_p3: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :rtype: 'mathutils.Vector'
    :return: The closest point of the triangle.
    """

    ...

def convex_hull_2d(points: typing.List) -> typing.List[int]:
    """Returns a list of indices into the list given

    :param points: list of 2d points.
    :type points: typing.List
    :rtype: typing.List[int]
    :return: a list of indices
    """

    ...

def delaunay_2d_cdt(vert_coords, edges, faces, output_type, epsilon, need_ids=True):
    """Computes the Constrained Delaunay Triangulation of a set of vertices,
    with edges and faces that must appear in the triangulation.
    Some triangles may be eaten away, or combined with other triangles,
    according to output type.
    The returned verts may be in a different order from input verts, may be moved
    slightly, and may be merged with other nearby verts.
    The three returned orig lists give, for each of verts, edges, and faces, the list of
    input element indices corresponding to the positionally same output element.
    For edges, the orig indices start with the input edges and then continue
    with the edges implied by each of the faces (n of them for an n-gon).
    If the need_ids argument is supplied, and False, then the code skips the preparation
    of the orig arrays, which may save some time.
    :arg vert_coords: Vertex coordinates (2d)
    :type vert_coords: list of `mathutils.Vector`
    :arg edges: Edges, as pairs of indices in vert_coords
    :type edges: list of (int, int)
    :arg faces: Faces, each sublist is a face, as indices in vert_coords (CCW oriented)
    :type faces: list of list of int
    :arg output_type: What output looks like. 0 => triangles with convex hull. 1 => triangles inside constraints. 2 => the input constraints, intersected. 3 => like 2 but detect holes and omit them from output. 4 => like 2 but with extra edges to make valid BMesh faces. 5 => like 4 but detect holes and omit them from output.
    :type output_type: intn   :arg epsilon: For nearness tests; should not be zero
    :type epsilon: float
    :arg need_ids: are the orig output arrays needed?
    :type need_args: bool
    :return: Output tuple, (vert_coords, edges, faces, orig_verts, orig_edges, orig_faces)
    :rtype: (list of mathutils.Vector, list of (int, int), list of list of int, list of list of int, list of list of int, list of list of int)

    """

    ...

def distance_point_to_plane(
    pt: typing.Union["mathutils.Vector", typing.Sequence[float]],
    plane_co: typing.Union["mathutils.Vector", typing.Sequence[float]],
    plane_no: typing.Union["mathutils.Vector", typing.Sequence[float]],
) -> float:
    """Returns the signed distance between a point and a plane    (negative when below the normal).

    :param pt: Point
    :type pt: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param plane_co: A point on the plane
    :type plane_co: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param plane_no: The direction the plane is facing
    :type plane_no: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :rtype: float
    """

    ...

def interpolate_bezier(
    knot1: typing.Union["mathutils.Vector", typing.Sequence[float]],
    handle1: typing.Union["mathutils.Vector", typing.Sequence[float]],
    handle2: typing.Union["mathutils.Vector", typing.Sequence[float]],
    knot2: typing.Union["mathutils.Vector", typing.Sequence[float]],
    resolution: int,
) -> typing.List:
    """Interpolate a bezier spline segment.

    :param knot1: First bezier spline point.
    :type knot1: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param handle1: First bezier spline handle.
    :type handle1: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param handle2: Second bezier spline handle.
    :type handle2: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param knot2: Second bezier spline point.
    :type knot2: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param resolution: Number of points to return.
    :type resolution: int
    :rtype: typing.List
    :return: The interpolated points
    """

    ...

def intersect_line_line(
    v1: typing.Union["mathutils.Vector", typing.Sequence[float]],
    v2: typing.Union["mathutils.Vector", typing.Sequence[float]],
    v3: typing.Union["mathutils.Vector", typing.Sequence[float]],
    v4: typing.Union["mathutils.Vector", typing.Sequence[float]],
) -> typing.Tuple["mathutils.Vector"]:
    """Returns a tuple with the points on each line respectively closest to the other.

    :param v1: First point of the first line
    :type v1: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param v2: Second point of the first line
    :type v2: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param v3: First point of the second line
    :type v3: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param v4: Second point of the second line
    :type v4: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :rtype: typing.Tuple['mathutils.Vector']
    """

    ...

def intersect_line_line_2d(
    lineA_p1: typing.Union["mathutils.Vector", typing.Sequence[float]],
    lineA_p2: typing.Union["mathutils.Vector", typing.Sequence[float]],
    lineB_p1: typing.Union["mathutils.Vector", typing.Sequence[float]],
    lineB_p2: typing.Union["mathutils.Vector", typing.Sequence[float]],
) -> "mathutils.Vector":
    """Takes 2 segments (defined by 4 vectors) and returns a vector for their point of intersection or None.

    :param lineA_p1: First point of the first line
    :type lineA_p1: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param lineA_p2: Second point of the first line
    :type lineA_p2: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param lineB_p1: First point of the second line
    :type lineB_p1: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param lineB_p2: Second point of the second line
    :type lineB_p2: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :rtype: 'mathutils.Vector'
    :return: The point of intersection or None when not found
    """

    ...

def intersect_line_plane(
    line_a: typing.Union["mathutils.Vector", typing.Sequence[float]],
    line_b: typing.Union["mathutils.Vector", typing.Sequence[float]],
    plane_co: typing.Union["mathutils.Vector", typing.Sequence[float]],
    plane_no: typing.Union["mathutils.Vector", typing.Sequence[float]],
    no_flip=False,
) -> "mathutils.Vector":
    """Calculate the intersection between a line (as 2 vectors) and a plane.
    Returns a vector for the intersection or None.

        :param line_a: First point of the first line
        :type line_a: typing.Union['mathutils.Vector', typing.Sequence[float]]
        :param line_b: Second point of the first line
        :type line_b: typing.Union['mathutils.Vector', typing.Sequence[float]]
        :param plane_co: A point on the plane
        :type plane_co: typing.Union['mathutils.Vector', typing.Sequence[float]]
        :param plane_no: The direction the plane is facing
        :type plane_no: typing.Union['mathutils.Vector', typing.Sequence[float]]
        :rtype: 'mathutils.Vector'
        :return: The point of intersection or None when not found
    """

    ...

def intersect_line_sphere(
    line_a: typing.Union["mathutils.Vector", typing.Sequence[float]],
    line_b: typing.Union["mathutils.Vector", typing.Sequence[float]],
    sphere_co: typing.Union["mathutils.Vector", typing.Sequence[float]],
    sphere_radius: typing.Any,
    clip=True,
) -> typing.Tuple:
    """Takes a line (as 2 points) and a sphere (as a point and a radius) and
    returns the intersection

        :param line_a: First point of the line
        :type line_a: typing.Union['mathutils.Vector', typing.Sequence[float]]
        :param line_b: Second point of the line
        :type line_b: typing.Union['mathutils.Vector', typing.Sequence[float]]
        :param sphere_co: The center of the sphere
        :type sphere_co: typing.Union['mathutils.Vector', typing.Sequence[float]]
        :param sphere_radius: Radius of the sphere
        :type sphere_radius: typing.Any
        :rtype: typing.Tuple
        :return: The intersection points as a pair of vectors or None when there is no intersection
    """

    ...

def intersect_line_sphere_2d(
    line_a: typing.Union["mathutils.Vector", typing.Sequence[float]],
    line_b: typing.Union["mathutils.Vector", typing.Sequence[float]],
    sphere_co: typing.Union["mathutils.Vector", typing.Sequence[float]],
    sphere_radius: typing.Any,
    clip=True,
) -> typing.Tuple:
    """Takes a line (as 2 points) and a sphere (as a point and a radius) and
    returns the intersection

        :param line_a: First point of the line
        :type line_a: typing.Union['mathutils.Vector', typing.Sequence[float]]
        :param line_b: Second point of the line
        :type line_b: typing.Union['mathutils.Vector', typing.Sequence[float]]
        :param sphere_co: The center of the sphere
        :type sphere_co: typing.Union['mathutils.Vector', typing.Sequence[float]]
        :param sphere_radius: Radius of the sphere
        :type sphere_radius: typing.Any
        :rtype: typing.Tuple
        :return: The intersection points as a pair of vectors or None when there is no intersection
    """

    ...

def intersect_plane_plane(
    plane_a_co: typing.Union["mathutils.Vector", typing.Sequence[float]],
    plane_a_no: typing.Union["mathutils.Vector", typing.Sequence[float]],
    plane_b_co: typing.Union["mathutils.Vector", typing.Sequence[float]],
    plane_b_no: typing.Union["mathutils.Vector", typing.Sequence[float]],
) -> typing.Tuple:
    """Return the intersection between two planes

    :param plane_a_co: Point on the first plane
    :type plane_a_co: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param plane_a_no: Normal of the first plane
    :type plane_a_no: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param plane_b_co: Point on the second plane
    :type plane_b_co: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param plane_b_no: Normal of the second plane
    :type plane_b_no: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :rtype: typing.Tuple
    :return: The line of the intersection represented as a point and a vector
    """

    ...

def intersect_point_line(
    pt: typing.Union["mathutils.Vector", typing.Sequence[float]],
    line_p1: typing.Union["mathutils.Vector", typing.Sequence[float]],
    line_p2,
) -> typing.Union["mathutils.Vector", float]:
    """Takes a point and a line and returns a tuple with the closest point on the line and its distance from the first point of the line as a percentage of the length of the line.

    :param pt: Point
    :type pt: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param line_p1: First point of the lineSecond point of the line
    :type line_p1: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :rtype: typing.Union['mathutils.Vector', float]
    """

    ...

def intersect_point_quad_2d(
    pt: typing.Union["mathutils.Vector", typing.Sequence[float]],
    quad_p1: typing.Union["mathutils.Vector", typing.Sequence[float]],
    quad_p2: typing.Union["mathutils.Vector", typing.Sequence[float]],
    quad_p3: typing.Union["mathutils.Vector", typing.Sequence[float]],
    quad_p4: typing.Union["mathutils.Vector", typing.Sequence[float]],
) -> int:
    """Takes 5 vectors (using only the x and y coordinates): one is the point and the next 4 define the quad,
    only the x and y are used from the vectors. Returns 1 if the point is within the quad, otherwise 0.
    Works only with convex quads without singular edges.

        :param pt: Point
        :type pt: typing.Union['mathutils.Vector', typing.Sequence[float]]
        :param quad_p1: First point of the quad
        :type quad_p1: typing.Union['mathutils.Vector', typing.Sequence[float]]
        :param quad_p2: Second point of the quad
        :type quad_p2: typing.Union['mathutils.Vector', typing.Sequence[float]]
        :param quad_p3: Third point of the quad
        :type quad_p3: typing.Union['mathutils.Vector', typing.Sequence[float]]
        :param quad_p4: Fourth point of the quad
        :type quad_p4: typing.Union['mathutils.Vector', typing.Sequence[float]]
        :rtype: int
    """

    ...

def intersect_point_tri(
    pt: typing.Union["mathutils.Vector", typing.Sequence[float]],
    tri_p1: typing.Union["mathutils.Vector", typing.Sequence[float]],
    tri_p2: typing.Union["mathutils.Vector", typing.Sequence[float]],
    tri_p3: typing.Union["mathutils.Vector", typing.Sequence[float]],
) -> "mathutils.Vector":
    """Takes 4 vectors: one is the point and the next 3 define the triangle. Projects the point onto the triangle plane and checks if it is within the triangle.

    :param pt: Point
    :type pt: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param tri_p1: First point of the triangle
    :type tri_p1: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param tri_p2: Second point of the triangle
    :type tri_p2: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param tri_p3: Third point of the triangle
    :type tri_p3: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :rtype: 'mathutils.Vector'
    :return: Point on the triangles plane or None if its outside the triangle
    """

    ...

def intersect_point_tri_2d(
    pt: typing.Union["mathutils.Vector", typing.Sequence[float]],
    tri_p1: typing.Union["mathutils.Vector", typing.Sequence[float]],
    tri_p2: typing.Union["mathutils.Vector", typing.Sequence[float]],
    tri_p3: typing.Union["mathutils.Vector", typing.Sequence[float]],
) -> int:
    """Takes 4 vectors (using only the x and y coordinates): one is the point and the next 3 define the triangle. Returns 1 if the point is within the triangle, otherwise 0.

    :param pt: Point
    :type pt: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param tri_p1: First point of the triangle
    :type tri_p1: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param tri_p2: Second point of the triangle
    :type tri_p2: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param tri_p3: Third point of the triangle
    :type tri_p3: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :rtype: int
    """

    ...

def intersect_ray_tri(
    v1: typing.Union["mathutils.Vector", typing.Sequence[float]],
    v2: typing.Union["mathutils.Vector", typing.Sequence[float]],
    v3: typing.Union["mathutils.Vector", typing.Sequence[float]],
    ray: typing.Union["mathutils.Vector", typing.Sequence[float]],
    orig: typing.Union["mathutils.Vector", typing.Sequence[float]],
    clip: bool = True,
) -> "mathutils.Vector":
    """Returns the intersection between a ray and a triangle, if possible, returns None otherwise.

    :param v1: Point1
    :type v1: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param v2: Point2
    :type v2: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param v3: Point3
    :type v3: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param ray: Direction of the projection
    :type ray: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param orig: Origin
    :type orig: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param clip: When False, don't restrict the intersection to the area of the triangle, use the infinite plane defined by the triangle.
    :type clip: bool
    :rtype: 'mathutils.Vector'
    :return: The point of intersection or None if no intersection is found
    """

    ...

def intersect_sphere_sphere_2d(
    p_a: typing.Union["mathutils.Vector", typing.Sequence[float]],
    radius_a: float,
    p_b: typing.Union["mathutils.Vector", typing.Sequence[float]],
    radius_b: float,
) -> typing.Tuple["mathutils.Vector"]:
    """Returns 2 points on between intersecting circles.

    :param p_a: Center of the first circle
    :type p_a: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param radius_a: Radius of the first circle
    :type radius_a: float
    :param p_b: Center of the second circle
    :type p_b: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param radius_b: Radius of the second circle
    :type radius_b: float
    :rtype: typing.Tuple['mathutils.Vector']
    """

    ...

def intersect_tri_tri_2d(tri_a1, tri_a2, tri_a3, tri_b1, tri_b2, tri_b3) -> bool:
    """Check if two 2D triangles intersect.

    :rtype: bool
    """

    ...

def normal(vectors: typing.List) -> "mathutils.Vector":
    """Returns the normal of a 3D polygon.

    :param vectors: Vectors to calculate normals with
    :type vectors: typing.List
    :rtype: 'mathutils.Vector'
    """

    ...

def points_in_planes(planes: typing.List["mathutils.Vector"]) -> typing.Any:
    """Returns a list of points inside all planes given and a list of index values for the planes used.

    :param planes: List of planes (4D vectors).
    :type planes: typing.List['mathutils.Vector']
    :rtype: typing.Any
    :return: two lists, once containing the vertices inside the planes, another containing the plane indices used
    """

    ...

def tessellate_polygon(veclist_list) -> typing.List:
    """Takes a list of polylines (each point a pair or triplet of numbers) and returns the point indices for a polyline filled with triangles. Does not handle degenerate geometry (such as zero-length lines due to consecutive identical points).

    :param veclist_list: list of polylines
    :rtype: typing.List
    """

    ...

def volume_tetrahedron(
    v1: typing.Union["mathutils.Vector", typing.Sequence[float]],
    v2: typing.Union["mathutils.Vector", typing.Sequence[float]],
    v3: typing.Union["mathutils.Vector", typing.Sequence[float]],
    v4: typing.Union["mathutils.Vector", typing.Sequence[float]],
) -> float:
    """Return the volume formed by a tetrahedron (points can be in any order).

    :param v1: Point1
    :type v1: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param v2: Point2
    :type v2: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param v3: Point3
    :type v3: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param v4: Point4
    :type v4: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :rtype: float
    """

    ...
