class Solution:
    def trap(self, heights: list[int]) -> int:
        i, j = 0, 0
        total_volume = 0

        if len(heights) < 2:
            return 0

        while j < len(heights):
            # Find first left height where height > 0
            left_height = heights[i]
            if left_height <= 0:
                i += 1
                continue

            # Find the j
            j_height = 0
            for h in range(i + 1, len(heights)):
                height = heights[h]
                if height >= left_height:
                    j_height = height
                    j = h
                    break
                else:
                    if height > j_height:
                        j_height = height
                        j = h

            # Handle the no suitable height for j
            if j_height == 0:
                break

            volume = self.get_volume(heights[i : j + 1])
            total_volume += volume

            i = j
            j += 1

        return total_volume

    def get_volume(self, list_data: list[int]) -> int:
        water_height = min(list_data[0], list_data[-1])
        container_bottom_area = len(list_data) - 2
        sum_of_all_obstacles = sum(list_data[1:-1])
        water_volume = water_height * container_bottom_area - sum_of_all_obstacles
        return water_volume