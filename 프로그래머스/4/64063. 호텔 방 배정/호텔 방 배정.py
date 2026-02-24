# def solution(k, room_number):
    
#     def find(x):
#         if x != parent[x]:
#             parent[x] = find(parent[x])
#         return parent[x]
    
#     def union(x,y):
#         a = find(x)
#         b = find(y)
#         if a != b:
#             parent[b] = a
            
#     parent = [i for i in range(k+2)]
#     answer = []
#     for i in room_number:
#         p = find(i)
#         if i == p:
#             answer.append(i)
#             union(i+1,i)
#         else:
#             answer.append(p)
#             union(p+1,p)
        
#     return answer
import sys

sys.setrecursionlimit(10**6)

def solution(k, room_number):
    parent = {}
    answer = []
    
    def find(x):
        if x not in parent:
            parent[x] = x + 1
            return x
        
        parent[x] = find(parent[x])
        return parent[x]
    
    for room in room_number:
        check = find(room)
        answer.append(check)
        
    return answer