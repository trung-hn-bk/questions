
"""
Question:

Given the initial position of a knight on the board (5, 4)
and a sequence of legal moves A, B, C, D, E, F, G, H
return the final position of the knight after moving

Follow up question:
Check if "moves" is the shortest path
"""

def final_pos(pos=(5, 4), moves="AGG"):
    delta = {"A": (-1, 2), "B": (-2, 1), "C": (-2, -1), "D": (-1, -2),
             "E": (1, -2), "F": (2, -1), "G": (2, 1), "H": (1, 2)}
    x, y = pos
    for move in moves:
        dx, dy = delta[move]
        x += dx
        y += dy
    return x, y


def shortest_path(pos=(5, 4), moves="AGG"):
    """Follow up question"""
    delta = {"A": (-1, 2), "B": (-2, 1), "C": (-2, -1), "D": (-1, -2),
             "E": (1, -2), "F": (2, -1), "G": (2, 1), "H": (1, 2)}
    x0, y0 = pos
    x1, y1 = final_pos(pos, moves)
    queue = [[x0, y0, 0]]
    for x, y, depth in queue:
        if x == x1 and y == y1:
            return depth == len(moves)
        for dx, dy in delta.values():
            queue.append([x + dx, y + dy, depth + 1])
    return False

print(final_pos((5, 4), "AGG"))  # (8, 8)
print(final_pos((5, 4), "AHCDEFACD"))  # (1, 1)

print(shortest_path((5, 4), "AGG"))  # True
print(shortest_path((5, 4), "AHCDEFACD"))  # False