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
    if r - 1 >= 0 and image[r - 1][c] == start_color:
        fill_color(image, r - 1, c, start_color, color)
    if r + 1 < len(image) and image[r + 1][c] == start_color:
        fill_color(image, r + 1, c, start_color, color)
    if c - 1 >= 0 and image[r][c - 1] == start_color:
        fill_color(image, r, c - 1, start_color, color)
    if c + 1 < len(image[0]) and image[r][c + 1] == start_color:
        fill_color(image, r, c + 1, start_color, color)

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
floodFill(image,sr,sc,color)
print(image)