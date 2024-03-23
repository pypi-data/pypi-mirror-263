import cv2
import numpy as np
import numpy.typing as npt
from pycvutils import padding


def flood_fill_binary(binary: npt.NDArray[np.uint8], x_y: tuple[int, int]) -> npt.NDArray[np.uint8]:
    """
    cv2.floodFill wrapper only for binary images.
    Fill value is calculating automatically
    """
    if ((binary > 0) & (binary < 255)).any():
        raise ValueError("You passed non binary image")
    x, y = x_y
    try:
        if int(binary[y, x]) == 0:
            fill_value = 255
        else:
            fill_value = 0
    except IndexError:
        return binary

    flags = 4 | (fill_value << 8) | cv2.FLOODFILL_FIXED_RANGE
    binary = cv2.floodFill(
        binary,
        mask=None,
        seedPoint=(x, y),
        newVal=fill_value,
        loDiff=0,
        upDiff=0,
        flags=flags,
    )[1]
    return binary


def darken_areas_near_borders(binary: npt.NDArray[np.uint8 | np.bool_]) -> npt.NDArray[np.uint8]:
    """Removes white blobs touching image borders"""
    binary = binary.astype(np.uint8)

    binary = padding.equal(binary, size=1, value=255)
    binary = flood_fill_binary(binary, (0, 0))
    binary = binary[1:-1, 1:-1]

    return binary


def brighten_areas_near_borders(binary: npt.NDArray[np.uint8 | np.bool_]) -> npt.NDArray[np.uint8]:
    """Removes black blobs touching image borders"""
    binary = binary.astype(np.uint8)

    binary = padding.equal(binary, size=1, value=0)
    binary = flood_fill_binary(binary, (0, 0))
    binary = binary[1:-1, 1:-1]

    return binary
