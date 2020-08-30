import heapq
from typing import *
from dataclasses import dataclass
from sortedcontainers import SortedList



def _get_skyline_using_sorted_container(buildings: List[List[int]]) -> List[List[int]]:
    
    @dataclass
    class BuildingPoint:
        x: int
        y: int
        is_start: bool
        
    
    skylines = []
    points = []
    for xi, xj, h in buildings:
        points.append(BuildingPoint(xi, h, True))
        points.append(BuildingPoint(xj, h, False))
    
    points = sorted(points, key=lambda p: p.x)
    i = 0
    last_x = None
    last_y = None
    hts = SortedList()
    while i < len(points):
        point = points[i]
        if (last_x is not None) and (last_x != point.x):
            # add skyline point
            max_ht = hts[-1] if hts else 0
            if max_ht != last_y:
                skylines.append((last_x, max_ht))
                last_y = max_ht
        
        if point.is_start:
            hts.add(point.y)
        else:
            hts.remove(point.y)
        
        last_x = point.x
        i += 1
    
    skylines.append((last_x, 0))
    return skylines
    

def _get_skyline_using_heap(buildings: List[List[int]]) -> List[List[int]]:
    
    @dataclass
    class BuildingPoint:
        x: int
        y: int
        end_x: Optional[int]
    
        @property
        def is_start(self):
            return self.end_x is not None
    
    skylines = []
    points = []
    for xi, xj, h in buildings:
        points.append(BuildingPoint(xi, h, xj))
        points.append(BuildingPoint(xj, h, None))
    
    points = sorted(points, key=lambda p: p.x)
    i = 0
    last_x = None
    last_y = None
    hts = []
    while i < len(points):
        point = points[i]
        if (last_x is not None) and (last_x != point.x):
            # add skyline point
            max_ht = max(hts, key=lambda entry: entry[1])[1] if hts else 0
            if max_ht != last_y:
                skylines.append((last_x, max_ht))
                last_y = max_ht
        
        if point.is_start:
            heapq.heappush(hts, (point.end_x, point.y))
        else:
            heapq.heappop(hts)
        
        last_x = point.x
        i += 1
    
    skylines.append((last_x, 0))
    return skylines
                

def _get_skyline_using_map(buildings: List[List[int]]) -> List[List[int]]:
    output = {}
    for l, r, h in buildings:
        for i in range(l, r):
            if i not in output:
                output[i] = h
            elif output[i] < h:
                output[i] = h

    min_x = min(output.keys())
    max_x = max(output.keys())

    i = min_x
    last_ht = output[min_x]
    skyline = [(i, last_ht)]

    for i in range(min_x+1, max_x+1):
        if i not in output:
            ht = 0
        else:
            ht = output[i]

        if ht != last_ht:
            skyline.append((i, ht))
            last_ht = ht

    skyline.append((max_x+1, 0))
    return skyline




class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # return _get_skyline_using_map(buildings)
        # return _get_skyline_using_heap(buildings)
        return _get_skyline_using_sorted_container(buildings)


def main():
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    skyline = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    assert Solution().getSkyline(buildings) == skyline


if __name__ == "__main__":
    main()
