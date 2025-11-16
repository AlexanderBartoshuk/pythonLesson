def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = data[1:1+n]
    
    first_occurrence = {}
    last_occurrence = {}
    
    for i, sticker in enumerate(arr):
        if sticker not in first_occurrence:
            first_occurrence[sticker] = i
        last_occurrence[sticker] = i
    
    # precompute next_diff
    next_diff = [n] * n
    for i in range(n-2, -1, -1):
        if arr[i] != arr[i+1]:
            next_diff[i] = i+1
        else:
            next_diff[i] = next_diff[i+1]
    
    super_rare = []
    for sticker in first_occurrence:
        first = first_occurrence[sticker]
        last = last_occurrence[sticker]
        if next_diff[first] >= last:
            super_rare.append(sticker)
    
    if not super_rare:
        print("NO")
    else:
        super_rare.sort()
        print("\n".join(super_rare))

if __name__ == "__main__":
    solve()