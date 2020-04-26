def insert_sort_directly(arr):
    """
    直接插入排序，不稳定，时间复杂度 o(n^2)
    :param arr: 列表
    :return: arr
    """
    n = len(arr)
    for i in range(1, n):  # 从第二个元素开始遍历
        temp = arr[i]  # 保存待插入元素
        j = i - 1  # 右边扫描开始下标
        while j >= 0 and temp < arr[j]:  # 从右向左扫描,直到找到比 temp 小的元素，将比 temp 大的元素依次右移一位
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp  # 找到插入位置，将 temp 插入
    return arr


if __name__ == '__main__':
    a = [2, 5, 4, 6, 3]
    result = insert_sort_directly(a)
    print(result)
