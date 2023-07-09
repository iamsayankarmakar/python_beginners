if __name__ == '__main__':
    d = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        d[name] = score
    print(d)
    v = d.values()
    sec_low_score = sorted(list(set(v)))[1]
    print(sec_low_score)
    sec_low_name = []
    for name, score in d.items():
        if score == sec_low_score:
            sec_low_name.append(name)
    sec_low_name.sort()
    for n in sec_low_name:
        print(n)