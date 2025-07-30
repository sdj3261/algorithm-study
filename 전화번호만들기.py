m = {
    '2': 'abc', '3': 'def', '4': 'ghi',
    '5': 'jkl', '6': 'mno', '7': 'pqr',
    '8': 'tuv', '9': 'wxyz'
}

ret = set()

def dfs(i, input_str, result):
    if i == len(input_str):
        ret.add(''.join(result))
        return

    for c in m.get(input_str[i], ''):
        result.append(c)
        dfs(i + 1, input_str, result)
        result.pop()

input_str = "23"
dfs(0, input_str, [])
print(ret)
