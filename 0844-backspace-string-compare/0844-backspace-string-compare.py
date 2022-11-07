class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        s_queue = self.make_queue_from_string(s)
        t_queue = self.make_queue_from_string(t)
        
        return s_queue == t_queue
    
    
    def make_queue_from_string(self, s: str) -> list:
        queue = []
        
        for char in s:
            if char == "#":
                if queue:
                    queue.pop()
            else:
                queue.append(char)
        
        return queue
        