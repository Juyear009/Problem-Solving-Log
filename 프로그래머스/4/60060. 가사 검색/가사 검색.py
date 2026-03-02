# def solution(words, queries):
#     answer = []
#     class Node:
#         def __init__(self):
#             self.child = {}
#             self.count = 0
    
#     root = Node()
#     for word in words:
#         node = root
#         for char in word:
#             if char not in node.child:
#                 node.child[char] = Node()
#                 node.count += 1
#             if "?" not in node.child:
#                 node.child["?"] = Node()
#                 node.child["?"].count += 1
#             node = node.child[char]
            
#     for word in words:
#         node = root.child["?"]
#         for char in word[1:]:
#             if char not in node.child:
#                 node.child[char] = Node()
#                 node.count += 1

#     for query in queries:
#         node = root
#         for q in query:
#             node = node.child[q]
            
            
#     return answer

from collections import defaultdict

def solution(words, queries):
    answer = []

    class Node:
        def __init__(self):
            self.child = {}
            self.count = 0

    # 길이별 트라이
    trie = defaultdict(Node)
    reverse_trie = defaultdict(Node)

    # 1️⃣ 단어 삽입
    for word in words:
        length = len(word)

        # 정방향
        node = trie[length]
        for char in word:
            node.count += 1
            if char not in node.child:
                node.child[char] = Node()
            node = node.child[char]
        node.count += 1

        # 역방향
        node = reverse_trie[length]
        for char in word[::-1]:
            node.count += 1
            if char not in node.child:
                node.child[char] = Node()
            node = node.child[char]
        node.count += 1

    # 2️⃣ 쿼리 처리
    for query in queries:
        length = len(query)

        # 길이 다른 건 0
        if length not in trie:
            answer.append(0)
            continue

        # 앞에 ? 있는 경우
        if query[0] == '?':
            node = reverse_trie[length]
            query = query[::-1]
        else:
            node = trie[length]

        for char in query:
            if char == '?':
                answer.append(node.count)
                break
            if char not in node.child:
                answer.append(0)
                break
            node = node.child[char]
        else:
            answer.append(node.count)

    return answer