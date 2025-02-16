from typing import List


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    water_flow_pacific_atlantic = [[0] * len(heights[0]) for r in range(len(heights))]

    num_r = len(heights)
    num_c = len(heights[0])
    filled = [[False] * num_c] * num_r

    # for i in range(num_r):
    #     water_flow_pacific_atlantic[i][0] += 1
    #     filled[i][0] = True
    # for i in range(num_c):
    #     water_flow_pacific_atlantic[0][i] += 1
    #     filled[0][i] = True

    def flood_fill_water_flow_pacific_atlantic(r, c: int):
        if r == 0 or r == num_r - 1 or c == 0 or c == num_c - 1:
            water_flow_pacific_atlantic[r][c] += 1
            filled[r][c] = True

        if r + 1 < num_r and not filled[r + 1][c] and heights[r][c] <= heights[r + 1][c]:
            water_flow_pacific_atlantic[r + 1][c] += 1
            filled[r + 1][c] = True
            flood_fill_water_flow_pacific_atlantic(r + 1, c)
        if r - 1 >= 0 and not filled[r - 1][c] and heights[r][c] <= heights[r - 1][c]:
            water_flow_pacific_atlantic[r - 1][c] += 1
            filled[r - 1][c] = True
            flood_fill_water_flow_pacific_atlantic(r - 1, c)
        if c + 1 < num_c and not filled[r][c + 1] and heights[r][c] <= heights[r][c + 1]:
            water_flow_pacific_atlantic[r][c + 1] += 1
            filled[r][c + 1] = True
            flood_fill_water_flow_pacific_atlantic(r, c + 1)
        if c - 1 >= 0 and not filled[r][c - 1] and heights[r][c] <= heights[r][c - 1]:
            water_flow_pacific_atlantic[r][c - 1] += 1
            filled[r][c - 1] = True
            flood_fill_water_flow_pacific_atlantic(r, c - 1)

    for i in range(num_r):
        flood_fill_water_flow_pacific_atlantic(i, 0)
    for i in range(num_c):
        flood_fill_water_flow_pacific_atlantic(0, i)

    print(water_flow_pacific_atlantic)
    filled = [[False] * num_c] * num_r
    # for i in range(num_r):
    #     water_flow_pacific_atlantic[i][num_c - 1] += 1
    #     filled[i][num_c - 1] = True
    # for i in range(num_c):
    #     water_flow_pacific_atlantic[num_r - 1][i] += 1
    #     filled[num_r - 1][i] = True

    for i in range(num_r):
        flood_fill_water_flow_pacific_atlantic(i, num_c - 1)
    for i in range(num_c):
        flood_fill_water_flow_pacific_atlantic(num_r - 1, i)

    result = []
    for r in range(num_r):
        for c in range(num_c):
            if water_flow_pacific_atlantic[r][c] == 2:
                result.append([r, c])

    return result


print(pacificAtlantic([
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]]))
