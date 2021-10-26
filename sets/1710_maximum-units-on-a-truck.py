'''
Q[1710]. Maximum Units on a Truck

n = len(boxTypes)
time : O(nlogn)
space : O(1)
'''


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        '''compute the maximum total number of units
        Args:
            boxTypes(List[List[int]]): the array[i] = [number of boxes, number of per boxes] (1 <= len(boxTypes) <= 1000)
            truckSize: the maximum number of boxes
        Returns:
            int: the maximum total number of units
        '''
        if not boxTypes:
            raise ValueError('boxTypes should be [1, 1000]')
        
        total_box_num = 0
        total_unit_num = 0
        boxTypes.sort(key=lambda x: x[1])
        
        for box in boxTypes[::-1]:
            total_box_num += box[0]

            if total_box_num > truckSize:
                total_box_num -= box[0]
                total_unit_num += ((truckSize - total_box_num)*box[1])
                return total_unit_num

            total_unit_num += (box[0] * box[1])
        return total_unit_num
