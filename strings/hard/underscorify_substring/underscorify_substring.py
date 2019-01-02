# O(n*m) time | O(n) space
def underscorify_substring(string, substring):
    locations = collapse(get_locations(string, substring))
    return underscorify(string, locations)

def get_locations(string, substring):
    locs = []
    start_idx = 0
    while start_idx < len(string):
        next_idx = string.find(substring, start_idx)
        if next_idx != -1:
            locs.append([next_idx, next_idx + len(substring)])
            start_idx = next_idx + 1
        else:
            break
    return locs

def collapse(locs):
    if not len(locs):
        return locs
    new_locs = [locs[0]]
    prev = new_locs[0]
    for i in range(1, len(locs)):
        curr = locs[i]
        if curr[0] <= prev[1]:
            prev[1] = curr[1]
        else:
            new_locs.append(curr)
            prev = curr
    return new_locs

def underscorify(string, locs):
    locs_idx = 0
    str_idx = 0
    in_between_underscores = False
    final_chars = []
    i = 0
    while str_idx < len(string) and locs_idx < len(locs):
        if str_idx == locs[locs_idx][i]:
            final_chars.append('_')
            in_between_underscores = not in_between_underscores
            if not in_between_underscores:
                locs_idx += 1
            i = 0 if i == 1 else 1
        final_chars.append(string[str_idx])
        str_idx += 1
    if locs_idx < len(locs):
        final_chars.append('_')
    elif str_idx < len(string):
        final_chars.append(string[str_idx])
    return "".join(final_chars)
