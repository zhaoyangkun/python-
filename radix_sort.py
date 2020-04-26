def radix_sort(arr):
    """
    基数排序
    :param arr: 列表
    """
    curr_digit = 0  # 记录当前位数是第几位，0 表示个位，1表示十位，依次类推
    max_val = max(arr)  # 获取列表中的最大值
    max_digit = len(str(max_val))  # 记录最大值的位数总数
    while curr_digit < max_digit:  # 注意循环条件：最大位数是 max_digit - 1
        bucket_list = [[] for _ in range(10)]  # 建立二维空数组，用于保存数据
        for i in arr:
            digit = (i // (10 ** curr_digit)) % 10  # 计算当前位数上的数字
            bucket_list[digit].append(i)  # 将当前元素写入二维数组中
        del arr[:]  # 清空列表
        for j in bucket_list:  # 将排序好的元素写入原列表 arr
            for k in j:
                arr.append(k)
        curr_digit += 1  # 位数 + 1


if __name__ == '__main__':
    a = [2, 5, 1, 4, 3, 6]
    radix_sort(a)
    print(a)
