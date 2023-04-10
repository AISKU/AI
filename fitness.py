def fitness(path, map):
    total_distance = 0
    check_list = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 
                  'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0,
                  'X': 0, 'Y': 0, 'Z': 0 } # 0 : 아직 방문하지 않은 도시, 1 : 방문한 도시
    for i in range(len(path) -1):
        # 현재 도시 위치에서 다음 도시의 방문 여부를 판단
        # 만약, 이동할 다음 위치가 0(방문안함)이라면, map의 distance를 가져와서 total_distance에 대입
        if check_list[path[i+1]] == 0:
            temp = map.distance.get(path[i], path[i+1])
            total_distance += temp
            check_list[path[i+1]] = 1
        # 만약, 이동할 다음 위치가 방문한 곳이라면, total_distance에 무한 숫자를 대입
        else: 
            total_distance = float('inf')
    
    # 처음 도시로 돌아와야 하므로 마지막 도시에서 처음 도시로의 경로를 더해줌
    total_distance += map.distance.get((path[-1], path[0]))

    return 1/total_distance
