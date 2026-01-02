def get_word_count(file):
    return len(file.split())

def get_num_char(file):
    counts = {}
    for c in file:
        if not c.isalpha(): 
            continue

        c = c.lower()
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    return counts

def get_sorted_dicts(file):
    sorted = []
    counts = get_num_char(file)
    for c in counts:
        tmp = {"char": c, "num": counts[c]}
        sorted.append(tmp)

    sorted.sort(key=lambda count: count["num"], reverse=True)

    return sorted