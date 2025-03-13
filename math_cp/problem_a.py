# TODO : MATH 
# https://codeforces.com/contest/2078/problem/A
# import sys
# def can_reduce_to_x(n, x, a):
#     avg = 0
#     for i in range(n):
#         avg += a[i]
#     return avg == n * x

# def main():
#     t = int(sys.stdin.readline().strip())
    
#     for _ in range(t):
#         n, x = map(int, sys.stdin.readline().split())
#         a = list(map(int, sys.stdin.readline().split()))
        
#         result = can_reduce_to_x(n, x, a)
#         print("YES" if result else "NO")

# if __name__ == "__main__":
#     main()