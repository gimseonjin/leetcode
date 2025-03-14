"""
1년 간 인사고과에 따라 인센트 지급

사원 마다 근무 태도 점수 / 동료 평가 점수

어떤 사람이 다른 임의의 사원보다 두 점수가 모두 낮은 경우가 한 번이라도 있으면 인센티브 받을 수 없다.

그렇지 않은 사원들에게는 두 점수의 합보다 높은 순으로 석차를 내어 석차에 따라 인센티브

두 점수의 합이 동일하면 동석차 / 동석차의 수 만큼 담 석차는 건너뛴다.

즉 1등이 두명이면 그 다음은 3등!

우선 근무 태도 중에서 두 점수 모두 낮으면, 받을 수 없다!!

즉 근무 태도 기준으로 정렬했을 때, 동료 평가가 가장 높은 것들만 카운팅 된다!! 라는 것이지

따라서 

근무 태도 & 동료 평가로 정렬하고, 

가장 높은 것들만 우선 뽑아오고,

총합 기준으로 정렬 한번 더하고,

거기서 원호가 몇번째 인덱스인지 찾고, 없으면 -1 반환!!!

"""
def solution(scores):
    wanho = scores[0]
    wanho_sum = sum(wanho)
    
    # 인센티브를 받을 수 있는 사원 목록 생성
    eligible_scores = []
    
    # 근무 태도 점수 기준 내림차순, 동료 평가 점수 기준 오름차순 정렬
    scores.sort(key=lambda s: (-s[0], s[1]))
    
    max_company = 0
    for s in scores:
        # 완호가 인센티브를 받을 수 없는 경우
        if wanho[0] < s[0] and wanho[1] < s[1]:
            return -1
        
        # 현재 사원이 인센티브를 받을 수 있는 경우
        if max_company <= s[1]:
            # 인센티브 자격 있는 사원의 점수와 완호 여부 저장
            eligible_scores.append((s[0] + s[1], s == wanho))
            max_company = s[1]
    
    # 점수 합 기준 내림차순 정렬
    eligible_scores.sort(key=lambda x: -x[0])
    
    # 동석차를 고려한 순위 계산
    rank = 1
    i = 0
    
    while i < len(eligible_scores):
        current_score = eligible_scores[i][0]
        same_rank_count = 0
        
        # 동일 점수 사원 수 계산
        while i + same_rank_count < len(eligible_scores) and eligible_scores[i + same_rank_count][0] == current_score:
            # 완호인 경우
            if eligible_scores[i + same_rank_count][1]:
                return rank
            same_rank_count += 1
        
        # 다음 순위로 건너뛰기 (동석차 수만큼)
        rank += same_rank_count
        i += same_rank_count
    
    # 여기까지 왔다면 오류 상황
    return -1