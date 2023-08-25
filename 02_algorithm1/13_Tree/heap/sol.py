N = 6
arr = [7, 2, 5, 3, 4, 6]

tree = [0] * (N+1)  # 0번은 안쓸거니까
last = 1

for i in range(N):
    if tree[i] == 0:
        tree[last] = arr[i]
    else:
        last += 1
        tree[last] = arr[i]
        child = last    # 자식의 위치
        # 완전 이진트리에서 부모의 위치는 자식의 위치를 2로 나눈 몫
        parent = child // 2

        # 만약에, 부모가 가진 값이 자식이 가진 값보다 크면
        # 최소힙을 만족할 수 없으니 두개 값을 swap해야한다.
        while parent >= 1 and tree[parent] > tree[child]:
            # 부모, 자식의 값 교환
            tree[parent], tree[child] = tree[child], tree[parent]
            # 자식의 위치가 swap한 부모의 위치가 되도록 설정
            child = parent
            # 부모의 값은?
            parent = child // 2

    print(tree)