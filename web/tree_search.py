# coding=utf-8


data = [
    ('None', 'A'),
    ('A', 'A1'),
    ('A', 'A1-1'),
    ('A1', 'A2'),
    ('A1-1', 'A2-3'),

]


def tree_search(d_dic, parent, son):
    for k, v_dic in d_dic.items():
        if k == parent:
            d_dic[k][son] = {}
            #print("Find parent of:", son)
            return
        else:
           # print("going to further layer")
            tree_search(d_dic[k], parent, son)


data_dic = {}



for item in data:
    print item

    parent, son = item
    if parent == 'None':
        data_dic[son] = {}
    else:
        tree_search(data_dic, parent, son)


for k, v in data_dic.items():
    print(k, v)

