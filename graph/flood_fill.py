def floodFill(image, sr, sc, color):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type color: int
    :rtype: List[List[int]]
    """
    fill_color(image, sr, sc, image[sr][sc], color)


def fill_color(image, r, c, start_color, color):
    image[r][c] = color
    neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    for (neighbor_r, neighbor_c) in neighbors:
        if neighbor_r in range(len(image)) and neighbor_c in range(len(image[0])) and image[neighbor_r][
            neighbor_c] == start_color:
            fill_color(image, neighbor_r, neighbor_c, start_color, color)


image = [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]
sr = 1
sc = 1
color = 2
floodFill(image, sr, sc, color)
print(image)
