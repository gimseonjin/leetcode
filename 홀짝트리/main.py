"""
루트 노드가 설정되어 있지않은 1개 이상의 트리가 있다.

모든 노드는 각자 번호가 있고, 각 노드는 4개 중 하나다

홀수 : 번호 홀수 & 자식 개수 홀수
짝수 : 번호 짝수 & 자식 개수 짝수
역홀수 : 번호 홀수 & 자식 개수 짝수
역짝수 : 번호 짝수 & 자식 개수 홀수

여기서 트리가 홀짝 트리 || 역홀짝 트리 개수 카운팅

홀짝 트리 : 홀수 & 짝수
역홀짝 트리 : 역홀수 & 역짝수

즉, 트리는 어떤 노드를 루트 노드로 설정하냐에 따라 홀짝 트리 혹은 역홀짝 트리가 될 수 있습니다. 경우에 따라 하나의 트리가 홀짝 트리와 역홀짝 트리 두 가지 모두 될 수 있거나 두 가지 모두 될 수 없을 수도 있습니다.

포레스트에 존재하는 노드들의 번호를 담은 1차원 정수 배열 nodes, 포레스트에 존재하는 간선들의 정보를 담은 2차원 정수 배열 edges가 매개변수로 주어집니다. 이때, 홀짝 트리가 될 수 있는 트리의 개수와 역홀짝 트리가 될 수 있는 트리의 개수를 1차원 정수 배열에 순서대로 담아 return 하도록 solution 함수를 완성해 주세요.
"""
"""
from collections import deque, defaultdict
import sys
sys.setrecursionlimit(2_000_000)

def is_odd_node(parent, children, visited):
    valid_children = [child for child in children if child not in visited]
    return parent % 2 == 1 and len(valid_children) % 2 == 1

def is_even_node(parent, children, visited):
    valid_children = [child for child in children if child not in visited]
    return parent % 2 == 0 and len(valid_children) % 2 == 0

def is_reverse_odd_node(parent, children, visited):
    valid_children = [child for child in children if child not in visited]
    return parent % 2 == 1 and len(valid_children) % 2 == 0

def is_reverse_even_node(parent, children, visited):
    valid_children = [child for child in children if child not in visited]
    return parent % 2 == 0 and len(valid_children) % 2 == 1

def bfs(start, tree):
    visited = set()
    queue = deque([start])
    result = []
    
    odd_and_even_trees = []
    revers_odd_and_even_trees = []

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        result.append(node)
        
        is_odd_and_even_tree = is_odd_node(node, tree[node], visited) or is_even_node(node, tree[node], visited)
        is_revers_odd_and_even_tree = is_reverse_odd_node(node, tree[node], visited) or is_reverse_even_node(node, tree[node], visited)
        
        odd_and_even_trees.append(is_odd_and_even_tree)
        revers_odd_and_even_trees.append(is_revers_odd_and_even_tree)
        
        for neighbor in tree[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    result_value = (all(odd_and_even_trees), all(revers_odd_and_even_trees))
    return result_value

def solution(nodes, edges):
    tree = defaultdict(list)
    for edge in edges:
        first, second = edge
        tree[first].append(second)
        tree[second].append(first)
    
    total_odd_and_even_tree_count = 0
    total_revers_odd_and_even_tree_count = 0
    for node in nodes:
        odd_and_even_tree_count, revers_odd_and_even_tree_count = bfs(node, tree)
        total_odd_and_even_tree_count += odd_and_even_tree_count
        total_revers_odd_and_even_tree_count += revers_odd_and_even_tree_count
        
    return [total_odd_and_even_tree_count, total_revers_odd_and_even_tree_count]
"""
from collections import defaultdict

def find(node, parent):
    if parent[node] != node:
        parent[node] = find(parent[node], parent)
    return parent[node]

def merge(a, b, parent):
    root_a = find(a, parent)
    root_b = find(b, parent)
    if root_a != root_b:
        parent[root_b] = root_a

def solution(nodes, edges):
    in_degree = defaultdict(int)
    parent = {node: node for node in nodes}
    
    # 간선 정보로 부모 관계 설정 및 진입 차수 계산
    for a, b in edges:
        in_degree[a] += 1
        in_degree[b] += 1
        merge(a, b, parent)
    
    tree_info_map = defaultdict(lambda: {"odd_type": 0, "even_type": 0, "reverse_odd_type": 0, "reverse_even_type": 0})
    
    for node in nodes:
        root = find(node, parent)
        if node % 2 == 0 and in_degree[node] % 2 == 0:
            tree_info_map[root]["even_type"] += 1
        elif node % 2 == 1 and in_degree[node] % 2 == 1:
            tree_info_map[root]["odd_type"] += 1
        elif node % 2 == 0 and in_degree[node] % 2 == 1:
            tree_info_map[root]["reverse_even_type"] += 1
        elif node % 2 == 1 and in_degree[node] % 2 == 0:
            tree_info_map[root]["reverse_odd_type"] += 1
    
    odd_even_tree_count = 0
    reverse_odd_even_tree_count = 0
    
    for tree_info in tree_info_map.values():
        if (tree_info["odd_type"] == 1 and tree_info["even_type"] == 0) or (tree_info["odd_type"] == 0 and tree_info["even_type"] == 1):
            odd_even_tree_count += 1
        
        if (tree_info["reverse_odd_type"] == 1 and tree_info["reverse_even_type"] == 0) or (tree_info["reverse_odd_type"] == 0 and tree_info["reverse_even_type"] == 1):
            reverse_odd_even_tree_count += 1
    
    return [odd_even_tree_count, reverse_odd_even_tree_count]
