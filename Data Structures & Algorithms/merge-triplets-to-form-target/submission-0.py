class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        output = [0, 0, 0]

        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                for i in range(3):
                    output[i] = max(output[i], triplet[i])

                if output == target:
                    return True

        return False