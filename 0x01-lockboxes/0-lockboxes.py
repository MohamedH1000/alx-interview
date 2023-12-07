#!/usr/bin/python3
"""
check if a all the list of boxes can be opened
"""


def canUnlockAll(boxes):
    """
    This function takes a list of lists and returns a boolean indicating
        whether all boxes in the list can be opened.
    """
    num = len(boxes)
    boxes_seen = set([0])
    boxes_unseen = set(boxes[0]).difference(set([0]))
    while len(boxes_unseen) > 0:
        id_box = boxes_unseen.pop()
        if not id_box or id_box >= num or id_box < 0:
            continue
        if id_box not in boxes_seen:
            boxes_unseen = boxes_unseen.union(boxes[id_box])
            boxes_seen.add(id_box)
    return num == len(boxes_seen)
