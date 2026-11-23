class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Approach: Stack with unique sorted posiitons (O(n) because pos are unique, then 2nd O(n) through that array to cluster, calc the remaining time to target for each, if tehy are the same, form a car fleet)
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in cars:
            # Calculate time to reach the target for each car
            time = (target - pos) / spd
            # Only add to stack if this car cant catch up to the fleet
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)

        