"""
즉 게임 난이도가, 내 레벨 보다 낮으면, time_cur 만큼 걸린다.
근데 게임 난이도가 내 레벨보다 높다, 그럼 (time_cur * (diff - level + 1)) + (pre_cur * (diff - level))
-> (time_cur + pre_cur) * (diff - level) + time_cur
"""
def calculate_clear_time(difficulty, level, current_time, previous_time):
    level_gap = difficulty - level
    if level_gap > 0:
        return (current_time + previous_time) * level_gap + current_time
    return current_time


def is_possible_to_clear_all(difficulties, times, time_limit, level):
    total_time = 0
    for i in range(len(difficulties)):
        current_time = times[i]
        previous_time = times[i - 1] if i > 0 else 0
        total_time += calculate_clear_time(difficulties[i], level, current_time, previous_time)
        if total_time > time_limit:
            return False
    return True


def solution(difficulties, times, time_limit):
    left, right = 1, max(difficulties) + 100  # upper bound은 넉넉히 잡기

    answer = right
    while left <= right:
        mid = (left + right) // 2
        if is_possible_to_clear_all(difficulties, times, time_limit, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer