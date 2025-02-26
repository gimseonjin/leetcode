"""
1~n 까지 번호가 있는 상자,
왼쪽에서 오른쪽으로 가면서 w 개까지 놓고 위로 올라감

num 번호를 가진 상자를 꺼내기 위해선 그 위의 상자들을 다 꺼내야한다.
이때 상자의 총 개수를 구하라!

가장 쉬운 방법은 2차 배열로 주루루룩 만든 다음에 위치 찾아서 계산하는 거다.

13
12 11 10
 7  8  9
 6  5  4
 1  2  3
"""
import math

def init_grid(n, w) : 
    rows = math.ceil(n / w)
    grid = [[0] * w for _ in range(rows)]
    
    row = 0
    col = 0
    direction = "LEFT"
    for i in range(1, n + 1):
        if col >= w:
            row += 1
            col = 0
            direction = "RIGHT" if direction == "LEFT" else "LEFT"
        
        if direction == "LEFT":
            grid[row][col] = i
        else:
            grid[row][w - col - 1] = i
            
        col += 1
    
    return grid

def count_box_to_move(grid, num):
    count = 0
    col = 0
    count_start = False
    for row in grid:
        if num in row:
            count_start = True
            col = row.index(num)
        if count_start and row[col] != 0:
            count += 1
            
    return count
        

def solution(n, w, num):
    grid = init_grid(n,w)
    
    answer = count_box_to_move(grid, num)
    
    return answer;