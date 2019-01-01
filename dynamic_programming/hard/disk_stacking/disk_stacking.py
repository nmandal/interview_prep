# O(n^2) time | O(n) space - where n is the number of disks
def disk_stacking(disks):
    disks.sort(key=lambda disk: disk[2])
    heights = [disk[2] for disk in disks]
    seqs = [None for disk in disks]
    max_height_idx = 0
    for i in range(1, len(disks)):
        curr = disks[i]
        for j in range(0, i):
            other_disk = disks[j]
            if is_valid_dimensions(curr, other):
                if heights[i] <= curr[2] + heights[j]:
                    heights[i] = curr[2] + heights[j]
                    seqs[i] = j
        if heights[i] >= heights[max_height_idx]:
            max_height_idx = i
    return build_seq(disks, seqs, max_height_idx)
        
def is_valid_dimensions(bottom, top):
    return bottom[0] > top[0] and bottom[1] > top[1] and bottom[2] > top[2]
    
def build_seq(disks, seqs, max_height_idx):
    seq = []
    while curr_idx is not None:
        seq.append(arr[curr_idx])
        curr_idx = seqs[curr_idx]
    return list(reversed(seq))
