'''
Q[973]. K Closest Points to Origin
'''

# n = len(points)
# time : O(nlogn)
# space : O(n)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''find k th closest point
        Args:
            points(List[List[int]]) : points on the X-Y plane
            k(int) : integer (1 <= k <= len(points) <= 10**4)
        Returns:
            List[List[int]] : k th closest point
        '''
        if not points:
            raise ValueError('points length should be [1, 10**4]')

        point_distances = []
        for i in range(len(points)):
            point_distances.append([i, points[i][0]**2 + points[i][1]**2])

        distance_sort = sorted(point_distances, key=lambda x:x[1])
        k_closest_points = []
        for i in range(len(points)):
            if i == k - 1:
                k_closest_points.append(points[distance_sort[i][0]])

        return k_closest_points

# time : O(nlogk)
# space : O(k)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, key=lambda x:x[0]**2 + x[1]**2)
