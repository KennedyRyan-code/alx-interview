#!/usr/bin/python3
"""A python module that determines if all boxes can be opened
   from a list of lists
"""


def canUnlockAll(boxes):
    """A function that returns True if all box in
    boxes can be opend
    """
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
