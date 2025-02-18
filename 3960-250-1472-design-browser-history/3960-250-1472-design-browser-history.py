"""
이건 단순한 구현 문제!
여기서 queue를 쓰면 적절할 거 같지만 굳이 쓸 필요는 없을 거 같구
list랑 cursor로 구현하는게 더 편할 거 같다
"""

class BrowserHistory:
    def __init__(self, homepage: str):
        self.current_index = 0         # 현재 페이지의 인덱스
        self.visited_pages = [homepage]  # 방문한 페이지 목록

    def visit(self, url: str) -> None:
        self.current_index += 1
        # 앞으로의 페이지 기록을 제거한 후 새 페이지 추가
        self.visited_pages = self.visited_pages[:self.current_index]
        self.visited_pages.append(url)

    def back(self, steps: int) -> str:
        # 인덱스가 0 미만이 되지 않도록 조정
        self.current_index = max(0, self.current_index - steps)
        return self.get_current_page()

    def forward(self, steps: int) -> str:
        # 인덱스가 방문한 페이지의 마지막을 넘지 않도록 조정
        self.current_index = min(len(self.visited_pages) - 1, self.current_index + steps)
        return self.get_current_page()

    def get_current_page(self) -> str:
        """현재 페이지를 반환하는 함수"""
        return self.visited_pages[self.current_index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)