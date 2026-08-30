class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()

        output = 0
        l = 0
        r = len(people) - 1

        while l <= r:

            output += 1

            if l < r and people[l] <= limit - people[r]:
                l += 1
            r -= 1

        return output