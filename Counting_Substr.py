def count_substring(string, sub_string):
    count = 0
    ind = 0
    for i in range(ind, len(string)):
        pos =string.find(sub_string, ind)
        if pos != -1:
            count += 1
            ind = pos + 1
    return count

s= count_substring("ABCDCDC", "CDC")
print(s)

