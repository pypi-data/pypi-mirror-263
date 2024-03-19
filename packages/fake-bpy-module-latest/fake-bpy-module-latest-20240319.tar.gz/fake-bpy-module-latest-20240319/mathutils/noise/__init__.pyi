import typing
import mathutils

GenericType = typing.TypeVar("GenericType")

def cell(position: typing.Union["mathutils.Vector", typing.Sequence[float]]) -> float:
    """Returns cell noise value at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :rtype: float
    :return: The cell noise value.
    """

    ...

def cell_vector(
    position: typing.Union["mathutils.Vector", typing.Sequence[float]],
) -> "mathutils.Vector":
    """Returns cell noise vector at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :rtype: 'mathutils.Vector'
    :return: The cell noise vector.
    """

    ...

def fractal(
    position: typing.Union["mathutils.Vector", typing.Sequence[float]],
    H: float,
    lacunarity: float,
    octaves: int,
    noise_basis: str = "PERLIN_ORIGINAL",
) -> float:
    """Returns the fractal Brownian motion (fBm) noise value from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param H: The fractal increment factor.
    :type H: float
    :param lacunarity: The gap between successive frequencies.
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used.
    :type octaves: int
    :param noise_basis: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_basis: str
    :rtype: float
    :return: The fractal Brownian motion noise value.
    """

    ...

def hetero_terrain(
    position: typing.Union["mathutils.Vector", typing.Sequence[float]],
    H: float,
    lacunarity: float,
    octaves: int,
    offset: float,
    noise_basis: str = "PERLIN_ORIGINAL",
) -> float:
    """Returns the heterogeneous terrain value from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param H: The fractal dimension of the roughest areas.
    :type H: float
    :param lacunarity: The gap between successive frequencies.
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used.
    :type octaves: int
    :param offset: The height of the terrain above 'sea level'.
    :type offset: float
    :param noise_basis: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_basis: str
    :rtype: float
    :return: The heterogeneous terrain value.
    """

    ...

def hybrid_multi_fractal(
    position: typing.Union["mathutils.Vector", typing.Sequence[float]],
    H: float,
    lacunarity: float,
    octaves: int,
    offset: float,
    gain: float,
    noise_basis: str = "PERLIN_ORIGINAL",
) -> float:
    """Returns hybrid multifractal value from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param H: The fractal dimension of the roughest areas.
    :type H: float
    :param lacunarity: The gap between successive frequencies.
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used.
    :type octaves: int
    :param offset: The height of the terrain above 'sea level'.
    :type offset: float
    :param gain: Scaling applied to the values.
    :type gain: float
    :param noise_basis: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_basis: str
    :rtype: float
    :return: The hybrid multifractal value.
    """

    ...

def multi_fractal(
    position: typing.Union["mathutils.Vector", typing.Sequence[float]],
    H: float,
    lacunarity: float,
    octaves: int,
    noise_basis: str = "PERLIN_ORIGINAL",
) -> float:
    """Returns multifractal noise value from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param H: The fractal increment factor.
    :type H: float
    :param lacunarity: The gap between successive frequencies.
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used.
    :type octaves: int
    :param noise_basis: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_basis: str
    :rtype: float
    :return: The multifractal noise value.
    """

    ...

def noise(
    position: typing.Union["mathutils.Vector", typing.Sequence[float]],
    noise_basis: str = "PERLIN_ORIGINAL",
) -> float:
    """Returns noise value from the noise basis at the position specified.

    :param position: The position to evaluate the selected noise function.
    :type position: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param noise_basis: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_basis: str
    :rtype: float
    :return: The noise value.
    """

    ...

def noise_vector(
    position: typing.Union["mathutils.Vector", typing.Sequence[float]],
    noise_basis: str = "PERLIN_ORIGINAL",
) -> "mathutils.Vector":
    """Returns the noise vector from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param noise_basis: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_basis: str
    :rtype: 'mathutils.Vector'
    :return: The noise vector.
    """

    ...

def random() -> float:
    """Returns a random number in the range [0, 1).

    :rtype: float
    :return: The random number.
    """

    ...

def random_unit_vector(size: int = 3) -> "mathutils.Vector":
    """Returns a unit vector with random entries.

    :param size: The size of the vector to be produced, in the range [2, 4].
    :type size: int
    :rtype: 'mathutils.Vector'
    :return: The random unit vector.
    """

    ...

def random_vector(size: int = 3) -> "mathutils.Vector":
    """Returns a vector with random entries in the range (-1, 1).

    :param size: The size of the vector to be produced.
    :type size: int
    :rtype: 'mathutils.Vector'
    :return: The random vector.
    """

    ...

def ridged_multi_fractal(
    position: typing.Union["mathutils.Vector", typing.Sequence[float]],
    H: float,
    lacunarity: float,
    octaves: int,
    offset: float,
    gain: float,
    noise_basis: str = "PERLIN_ORIGINAL",
) -> float:
    """Returns ridged multifractal value from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param H: The fractal dimension of the roughest areas.
    :type H: float
    :param lacunarity: The gap between successive frequencies.
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used.
    :type octaves: int
    :param offset: The height of the terrain above 'sea level'.
    :type offset: float
    :param gain: Scaling applied to the values.
    :type gain: float
    :param noise_basis: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_basis: str
    :rtype: float
    :return: The ridged multifractal value.
    """

    ...

def seed_set(seed: int):
    """Sets the random seed used for random_unit_vector, and random.

        :param seed: Seed used for the random generator.
    When seed is zero, the current time will be used instead.
        :type seed: int
    """

    ...

def turbulence(
    position: typing.Union["mathutils.Vector", typing.Sequence[float]],
    octaves: int,
    hard: bool,
    noise_basis: str = "PERLIN_ORIGINAL",
    amplitude_scale: float = 0.5,
    frequency_scale: float = 2.0,
) -> float:
    """Returns the turbulence value from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param octaves: The number of different noise frequencies used.
    :type octaves: int
    :param hard: Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions).
    :type hard: bool
    :param noise_basis: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_basis: str
    :param amplitude_scale: The amplitude scaling factor.
    :type amplitude_scale: float
    :param frequency_scale: The frequency scaling factor
    :type frequency_scale: float
    :rtype: float
    :return: The turbulence value.
    """

    ...

def turbulence_vector(
    position: typing.Union["mathutils.Vector", typing.Sequence[float]],
    octaves: int,
    hard: bool,
    noise_basis: str = "PERLIN_ORIGINAL",
    amplitude_scale: float = 0.5,
    frequency_scale: float = 2.0,
) -> "mathutils.Vector":
    """Returns the turbulence vector from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param octaves: The number of different noise frequencies used.
    :type octaves: int
    :param hard: Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions).
    :type hard: bool
    :param noise_basis: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_basis: str
    :param amplitude_scale: The amplitude scaling factor.
    :type amplitude_scale: float
    :param frequency_scale: The frequency scaling factor
    :type frequency_scale: float
    :rtype: 'mathutils.Vector'
    :return: The turbulence vector.
    """

    ...

def variable_lacunarity(
    position: typing.Union["mathutils.Vector", typing.Sequence[float]],
    distortion: float,
    noise_type1: str = "PERLIN_ORIGINAL",
    noise_type2: str = "PERLIN_ORIGINAL",
) -> float:
    """Returns variable lacunarity noise value, a distorted variety of noise, from noise type 1 distorted by noise type 2 at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param distortion: The amount of distortion.
    :type distortion: float
    :param noise_type1: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_type1: str
    :param noise_type2: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_type2: str
    :rtype: float
    :return: The variable lacunarity noise value.
    """

    ...

def voronoi(
    position: typing.Union["mathutils.Vector", typing.Sequence[float]],
    distance_metric: str = "DISTANCE",
    exponent: float = 2.5,
) -> typing.List["mathutils.Vector"]:
    """Returns a list of distances to the four closest features and their locations.

    :param position: The position to evaluate the selected noise function.
    :type position: typing.Union['mathutils.Vector', typing.Sequence[float]]
    :param distance_metric: Enumerator in ['DISTANCE', 'DISTANCE_SQUARED', 'MANHATTAN', 'CHEBYCHEV', 'MINKOVSKY', 'MINKOVSKY_HALF', 'MINKOVSKY_FOUR'].
    :type distance_metric: str
    :param exponent: The exponent for Minkowski distance metric.
    :type exponent: float
    :rtype: typing.List['mathutils.Vector']
    :return: A list of distances to the four closest features and their locations.
    """

    ...
