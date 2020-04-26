def merge(left_arr, right_arr):
    """
    合并两个列表（非递减）
    :param left_arr: 左列表
    :param right_arr:右列表
    :return: 合并后的列表
    """
    result = []
    i, j = 0, 0
    while i < len(left_arr) and j < len(right_arr):  # 双指针遍历两个列表，将两个列表合并
        if left_arr[i] < right_arr[j]:  # 若 i 指向元素小于 j 指向元素，将 left_arr[i] 插入 result 中
            result.append(left_arr[i])
            i += 1  # i 向右移动一位
        else:
            result.append(right_arr[j])
            j += 1
    while i < len(left_arr):  # 将剩余元素依次写入 result 中
        result.append(left_arr[i])
        i += 1
    while j < len(right_arr):
        result.append(right_arr[j])
        j += 1
    return result


def merge_sort(arr):
    """
    归并排序
    :param arr: 列表
    :return:列表
    """
    n = len(arr)
    if n <= 1:  # 若长度小于等于 1，结束排序（递归出口）
        return arr
    mid = n // 2
    left_arr = merge_sort(arr[:mid])  # 对左列表进行归并排序
    right_arr = merge_sort(arr[mid:])  # 对右列表进行归并排序
    return merge(left_arr, right_arr)  # 合并左右两个列表


if __name__ == '__main__':
    a = [2, 5, 1, 4, 3, 6]
    result = merge_sort(a)
    print(result)
