a, b, c = map(int, input().split())


def find_answer(ret, b):  #a^8 = a^4 * a^2 핵심개념 :  a^b= a^(b/2)^2
    if b == 1:
        return ret % c
    ret = find_answer(ret, b // 2)
    ret = (ret * ret) % c
    if b % 2 == 1:
        ret = (ret * a) % c
    return ret


print(find_answer(a, b))
