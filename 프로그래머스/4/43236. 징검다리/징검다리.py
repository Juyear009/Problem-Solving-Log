def solution(distance, rocks, n):
    def check(mid):
        remove = 0
        prev = 0
        for i in range(len(rocks)):
            if rocks[i] - prev < mid:
                remove += 1
            else:
                prev = rocks[i]
        if distance - prev < mid:
            remove += 1
        
        if remove <= n:
            return True
        return False
            
    answer = 0
    rocks.sort()
    left = 1
    right = distance
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    answer = right
    return answer