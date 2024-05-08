class Solution:
    def knightDialer(self, n: int) -> int:
        # A-type:{0} -> 2B, B-type:{4,6} -> A+2C
        # C-type:{1,3,7,9} -> B+D, D-type:{2,8} -> 2C
        mod = 10**9+7
        movement = [1, 2, 4, 2, 1]  # {0}, {4, 6}, {1, 3, 7, 9}, {2, 8}, {5}
        for _ in range(n-1):
            A = movement[1]
            B = (movement[0]*2 + movement[2]) % mod
            C = (movement[1]*2 + movement[3]*2) % mod
            D = movement[2]
            movement = [A, B, C, D]
        return sum(movement) % mod
