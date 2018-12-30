# 把一个list进行排序，返回一个列表，其中依次为从大到小的项的角标
def get_order_list(lis):
    order_list = []
    while len(lis) != len(order_list):
        for i in range(len(lis)):
            if i in order_list:
                continue
            else:
                sub = i
                for k in range(len(lis)):
                    if k in order_list:
                        continue
                    elif lis[k] > lis[sub]:
                        sub = k
                    else:
                        continue
                order_list.append(sub)
    for i in range(len(order_list)):  # 对于每一个元素都加1，因为docID是从1开始的
        order_list[i] += 1
    return order_list


if __name__ == '__main__':
    lista = [3, 5, 2, 7, 13, 11]
    print(get_order_list(lista))