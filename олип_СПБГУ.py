import math

def solve():
    t = int(input())
    for _ in range(t):
        w = int(input())
        xA, yA = map(int, input().split())
        xB, yB = map(int, input().split())
        
        def dist(x1, y1, x2, y2):
            return math.hypot(x1 - x2, y1 - y2)
        
        
        def total_time(xP, xQ):
            if xQ <= xP:
                return float('inf')
            yP = xP
            yQ = w
            
            time_AP = dist(xA, yA, xP, yP)
            time_QB = dist(xB, yB, xQ, yQ)
            
            dx = xQ - xP
            dy = yQ - yP
            time_river = (dx * dx + dy * dy) / (2 * dx)
            
            return time_AP + time_river + time_QB
        
        
        def optimize():
            best = float('inf')
            left_P = 0.0
            right_P = w
            
            for _ in range(60):
                mid1_P = left_P + (right_P - left_P) / 3
                mid2_P = right_P - (right_P - left_P) / 3
                
                left_Q1 = mid1_P
                right_Q1 = w
                best_Q1 = float('inf')
                for __ in range(60):
                    mid1_Q = left_Q1 + (right_Q1 - left_Q1) / 3
                    mid2_Q = right_Q1 - (right_Q1 - left_Q1) / 3
                    t1 = total_time(mid1_P, mid1_Q)
                    t2 = total_time(mid1_P, mid2_Q)
                    if t1 < t2:
                        right_Q1 = mid2_Q
                    else:
                        left_Q1 = mid1_Q
                    best_Q1 = min(best_Q1, t1, t2)
                
                left_Q2 = mid2_P
                right_Q2 = w
                best_Q2 = float('inf')
                for __ in range(60):
                    mid1_Q = left_Q2 + (right_Q2 - left_Q2) / 3
                    mid2_Q = right_Q2 - (right_Q2 - left_Q2) / 3
                    t1 = total_time(mid2_P, mid1_Q)
                    t2 = total_time(mid2_P, mid2_Q)
                    if t1 < t2:
                        right_Q2 = mid2_Q
                    else:
                        left_Q2 = mid1_Q
                    best_Q2 = min(best_Q2, t1, t2)
                
                if best_Q1 < best_Q2:
                    right_P = mid2_P
                else:
                    left_P = mid1_P
                best = min(best, best_Q1, best_Q2)
            
            return best
        
        result = optimize()
        print(f"{result:.15f}")

if __name__ == "__main__":
    solve()