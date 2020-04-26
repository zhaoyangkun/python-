def quick_sort(arr, left, right):
    """
    快速排序
    :param arr: 列表
    :param left: 开始下标
    :param right: 结束下标
    """
    i, j = left, right  # i 为左指针，j 为右指针
    if left < right:  # 递归出口条件
        base = arr[left]  # base 记录基准值
        while i < j:  # 对子列进行快排，当两个指针相遇时，结束循环
            while i < j and arr[j] >= base:  # 从右往左扫描，直到找到比 base 小的值
                j -= 1
            if i < j:  # 右指针在左指针右边，才能进行赋值操作（因为可能会出现未找到比基准元素小的情况，而此时 j <= i）
                arr[i] = arr[j]  # 把右指针对应的值赋给左指针
            while i < j and arr[i] <= base:  # 从左向右扫描，直到找到比 base 大的值
                i += 1
            if i < j:
                arr[j] = arr[i]  # 把左指针对应的值赋给右指针
        arr[i] = base  # 基准值插入到最终位置（此时左右指针相遇）
        quick_sort(arr, left, i - 1)  # 对左子列（基准值左边部分）进行快排
        quick_sort(arr, i + 1, right)  # 对右子列（基准值右边部分）进行快排


if __name__ == '__main__':
    a = [2, 5, 4, 6, 3, 1, 8, 9, 7, 10]
    quick_sort(a, 0, len(a) - 1)
    print(a)
