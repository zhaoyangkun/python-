def shell_sort(arr):
    """
    希尔排序
    :param arr: 列表
    """
    n = len(arr)  # 列表长度
    step = n // 2  # 步长，初始值为列表长度除 2 取整
    while step > 0:
        for j in range(step, n):  # 从下标 step 遍历到 n - 1
            while j - step >= 0 and arr[j] < arr[j - step]:  # 比较下标相差 step 的两个元素，若 j- step 比 j 对应元素大，将两者交换
                arr[j], arr[j - step] = arr[j - step], arr[j]
                j -= step
        step = step // 2  # 步长减半


if __name__ == '__main__':
    a = [2, 5, 4, 6, 3]
    shell_sort(a)
    print(a)
