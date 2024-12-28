def prime(arr_name,arr_score):
    ar = []
    for i in arr_score:
        if arr_score.count(i) >= 2:
            for _ in range(arr_score.count(i)):
                name = arr_name[arr_score.index(i)]
                ar.append(name)
                arr_score.remove(i)
                arr_name.remove(name)
    return sorted(ar)

if __name__ == '__main__':
    arr_name = []
    arr_score = []
    arr = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr_name.append(name)
        arr_score.append(score)
    for a in prime(arr_name,arr_score):
        print(a)
