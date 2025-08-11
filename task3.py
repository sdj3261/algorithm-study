from collections import defaultdict

def solution(S, A):
    n = len(S)
    tree = defaultdict(list)
    root = -1

    # 트리 만들기
    for child in range(n):
        parent = S[child]
        if parent == -1:
            root = child
        else:
            tree[parent].append(child)

    def dfs(node):
        valid_lengths = []

        for child in tree[node]:
            child_len = dfs(child)
            # 부모-자식 문자가 다르면 연결 가능
            if A[child] != A[node]:
                valid_lengths.append(child_len)

        if not valid_lengths:
            return 1  # 자기 자신만 있는 경로 길이

        # 가장 긴 경로로만 이어감
        return max(valid_lengths) + 1

    return dfs(-1)

# 테스트
print(solution([-1,0], "ab"))  # 예상: 3
