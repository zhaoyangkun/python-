def bubble_sort(arr):
    """
    冒泡排序（起泡排序）
    :param arr: 列表
    :return: arr
    """
    n = len(arr)
    for i in range(n - 1, 0, -1):  # 反向遍历下标从 n - 1 到 1 的元素
        flag = 0  # 标记是否发生元素交换
        for j in range(0, i):  # 遍历下标 0 ～ i - 1 的元素
            if arr[j] > arr[j + 1]:  # 若当前元素大于下一个元素，将两者交换
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1  # 标记已发生交换
        if flag == 0:  # 未发生交换，结束排序
            return arr


if __name__ == '__main__':
    a = [2, 5, 4, 6, 3]
    bubble_sort(a)
    print(a)
