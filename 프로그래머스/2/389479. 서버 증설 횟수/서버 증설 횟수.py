"""
나는 온라인 게임을 운영 중
게임을 이용하는 사람이 m명 늘어나면, 서버 한대 추가
m명 미만이면 증설 x

어느 시간대의 이용자 = k 가 n * m <= k < (n + 1) * m 최소 n대 서버 운영중

한번 증설한 서버는 k 시간 동안 운영, 그 이후에는 반납

ex n = 5 10시에 증설 -> 10 ~ 15시 / 모든 게임 이용자가 게임을 하기 위해선 몇 번 증설 해야 하는가?

제일 쉬워보이는 방법은, 24시간 짜리 배열 만들고, 게임 이용자 수를 받아와서 시간대 별로 충분한가? 계산하고, 증설이 필요하면 그때부터 K 시간 이후의 배열까지 + 1 하는 식으로 하면 될 듯??
"""
def calculate_server_for_serving(players, m):
    n = 0
    while True:
        if n * m <= players < (n + 1) * m:
            break
        n += 1
    return n

def solution(players, m, k):
    server_per_hour = [0] * 24
    added_server_count = 0
    
    for i, players_per_hour in enumerate(players):
        needed_server = calculate_server_for_serving(players_per_hour, m)
        added_server = server_per_hour[i]
        
        if needed_server > added_server:
            added_server_count += needed_server - added_server
            for j in range(i, min(i + k, len(server_per_hour))):
                server_per_hour[j] += needed_server - added_server
            
    return added_server_count