def simple_choose_sort(arr):
    """
    简单选择排序
    :param arr: 列表
    """
    n = len(arr)
    for i in range(n - 1):  # 经过 n - 1 次遍历后，已经全部有序
        index = i  # 保存最小值下标
        for j in range(i + 1, n):
            if arr[j] < arr[index]:  # 若找到比当前最小值 arr[index] 还要小的元素，更新最小值下标
                index = j
        arr[i], arr[index] = arr[index], arr[i]  # 将最小值和待排序列第一个元素交换


if __name__ == '__main__':
    a = [2, 5, 1, 4, 3, 6]
    simple_choose_sort(a)
    print(a)
