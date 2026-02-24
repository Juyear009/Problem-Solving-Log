class Node():
    def __init__(self):
        self.child = {}
        self.count = 0

def solution(words):
    answer = 0
    root = Node()
    for word in words:
        node = root
        for ch in word:
            if ch not in node.child:
                node.child[ch] = Node()
            node = node.child[ch]
            node.count += 1
            
    for word in words:
        node = root
        for ch in word:
            node = node.child[ch]
            answer += 1
            if node.count == 1:
                break
    
    return answer