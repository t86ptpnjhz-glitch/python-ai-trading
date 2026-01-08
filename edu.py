from collections import deque

# =======================
# Соседи в сетке 10x10
# =======================
def neighbors(pos):
    r, c = divmod(pos, 10)
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 10 and 0 <= nc < 10:
            yield nr * 10 + nc

# =======================
# Прямые пути между двумя клетками
# =======================
def straight_path(start, end):
    r1, c1 = divmod(start, 10)
    r2, c2 = divmod(end, 10)
    
    # Вертикально → горизонтально
    path1 = []
    step_r = 1 if r2 > r1 else -1
    for r in range(r1, r2 + step_r, step_r):
        path1.append(r * 10 + c1)
    step_c = 1 if c2 > c1 else -1
    for c in range(c1 + step_c, c2 + step_c, step_c):
        path1.append(r2 * 10 + c)
    
    # Горизонтально → вертикально
    path2 = []
    step_c = 1 if c2 > c1 else -1
    for c in range(c1, c2 + step_c, step_c):
        path2.append(r1 * 10 + c)
    step_r = 1 if r2 > r1 else -1
    for r in range(r1 + step_r, r2 + step_r, step_r):
        path2.append(r * 10 + c2)
    
    return [path1, path2]

# =======================
# BFS для кратчайших путей без повторений
# =======================
def all_shortest_paths(start, end, blocked=set()):
    queue = deque([[start]])
    visited = {start: 0}
    paths = []
    shortest = None

    while queue:
        path = queue.popleft()
        cur = path[-1]

        if shortest is not None and len(path) > shortest:
            continue

        if cur == end:
            shortest = len(path)
            paths.append(path)
            continue

        for nxt in neighbors(cur):
            if nxt in blocked or nxt in path:
                continue
            dist = len(path)
            if nxt not in visited or visited[nxt] >= dist:
                visited[nxt] = dist
                queue.append(path + [nxt])

    return paths

# =======================
# Генерация сегментов с приоритетом прямых маршрутов
# =======================
def generate_segments(stations):
    segments = []
    for i in range(len(stations)-1):
        direct_paths = straight_path(stations[i], stations[i+1])
        valid_directs = []
        for p in direct_paths:
            if len(set(p)) == len(p):
                valid_directs.append(p)
        if valid_directs:
            segments.append(valid_directs)
        else:
            bfs_paths = all_shortest_paths(stations[i], stations[i+1])
            if bfs_paths:
                segments.append(bfs_paths)
            else:
                segments.append([])  # сегмент без допустимого пути
    return segments

# =======================
# Рекурсивная сборка пути без повторений
# =======================
def assemble_optimal_path(segments, i=0, current_path=None, used=None):
    if current_path is None:
        if not segments or not segments[0]:
            return None
        current_path = [segments[0][0][0]]
    if used is None:
        used = set(current_path)
    
    if i == len(segments):
        return current_path
    
    if not segments[i]:
        return None  # если сегмент невозможен
    
    min_path = None
    for p in segments[i]:
        overlap = set(p[1:]) & used
        if overlap:
            continue
        new_used = used | set(p[1:])
        candidate = assemble_optimal_path(segments, i+1, current_path + p[1:], new_used)
        if candidate is not None:
            if min_path is None or len(candidate) < len(min_path):
                min_path = candidate
    return min_path

# =======================
# BFS по всем станциям сразу без повторений
# =======================
def bfs_full_route(stations):
    full_path = [stations[0]]
    used = set(full_path)

    for i in range(len(stations)-1):
        start, end = full_path[-1], stations[i+1]
        queue = deque([[start]])
        found = None

        while queue and found is None:
            path = queue.popleft()
            cur = path[-1]
            if cur == end:
                found = path
                break
            for nxt in neighbors(cur):
                if nxt not in used and nxt not in path:
                    queue.append(path + [nxt])
        if found is None:
            return None  # путь между станциями невозможен
        full_path.extend(found[1:])
        used.update(found[1:])
    return full_path

# =======================
# Основная функция с fallback
# =======================
def four_pass(stations):
    segments = generate_segments(stations)
    path = assemble_optimal_path(segments)
    if path is not None:
        return path

    # fallback BFS по всему маршруту без повторений
    return bfs_full_route(stations)


tester = [37,61,92,36]

result = four_pass(tester)
print(result)









