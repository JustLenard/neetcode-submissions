from dataclasses import dataclass

@dataclass
class CarFleet:
    postition: int
    speed: int


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        carfleets: list[CarFleet] = []

        carfleets_reachet_target = 0

        for i, p in enumerate(position):
            new_carFleet = CarFleet(postition=p, speed=speed[i])
            carfleets.append(new_carFleet)

        carfleets = sorted(carfleets, key=lambda key: key.postition)

        while carfleets:
            for i in range(len(carfleets) - 1, -1, -1):
                curr_carfleet = carfleets[i]

                carfleet_in_front = None if i == len(carfleets) - 1 else carfleets[i + 1]

                # Drive
                curr_carfleet.postition = curr_carfleet.postition + curr_carfleet.speed

                # if we reached the carfleet in front:
                if carfleet_in_front and curr_carfleet.postition >= carfleet_in_front.postition:
                    # Positions at the start of this hour
                    curr_start = curr_carfleet.postition - curr_carfleet.speed
                    front_start = carfleet_in_front.postition - carfleet_in_front.speed

                    # The catch-up happened mid-hour; it only counts if it was at or before the target.
                    # catch_point = curr_start + curr_speed * gap / speed_diff, cross-multiplied to stay in integers
                    gap = front_start - curr_start
                    speed_diff = curr_carfleet.speed - carfleet_in_front.speed
                    if curr_start * speed_diff + curr_carfleet.speed * gap <= target * speed_diff:
                        del carfleets[i]

            # Check if reached target (several fleets can arrive in the same hour)
            while carfleets and carfleets[-1].postition >= target:
                carfleets.pop()
                carfleets_reachet_target += 1

        return carfleets_reachet_target