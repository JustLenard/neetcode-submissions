class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Cars travel toward target on a single lane at their own fixed speed and can
        never pass one another; a faster car behind a slower one bunches up with it
        and they continue together as one fleet at the slower speed. Return the
        number of distinct fleets that arrive at target.

        Example:
            target = 12, position = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]
            -> 3   (cars at 10 and 8 merge into one fleet; 5 and 3 each form their own)
        """


        cars_info = [(pos, speed[i], (target - pos) / speed[i]) for i, pos in enumerate(position)]

        cars_info = sorted(cars_info, key=lambda x: x[0], reverse=True)

        prev_carfleet_time = cars_info[0][2]
        res = 1

        for _, _, time in cars_info[1:]:
            if prev_carfleet_time < time:
                prev_carfleet_time = time
                res += 1
  

        return res