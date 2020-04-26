def adjust(arr, parent, n):
    """
    调整二叉树
    :param arr: 列表
    :param parent: 父节点下标
    :param n: 列表长度
    """
    temp = arr[parent]  # 保存父结点的值
    child = 2 * parent + 1  # child 指向左孩子
    while child < n:
        if child + 1 < n and arr[child] < arr[child + 1]:  # 若右孩子存在且大于左孩子，将 child 指向右孩子
            child += 1
        if temp > arr[child]:  # 父结点已大于左右孩子，结束循环
            break
        arr[parent] = arr[child]  # 把孩子结点的值赋给父结点
        parent = child  # 选取孩子结点的左孩子，继续进行调整
        child = 2 * parent + 1
    arr[parent] = temp


def heap_sort(arr):
    """
    堆排序
    :param arr: 列表
    """
    length = len(arr)
    # 循环建立初始大顶堆
    for i in range((length - 1) // 2, -1, -1):
        adjust(arr, i, length)
    #  n - 1 次循环，完成堆排序
    for j in range(length - 1, 0, -1):
        arr[0], arr[j] = arr[j], arr[0]  # 交换第一个元素和最后一个元素
        adjust(arr, 0, j)  # 对剩余的 j - 1 个元素进行调整


if __name__ == '__main__':
    a = [1, 3, 4, 5, 2, 6, 9, 7, 8, 0]
    heap_sort(a)
    print(a)
