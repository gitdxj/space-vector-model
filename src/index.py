import csv
import os
import split


# 创建倒排索引
# 在向量空间模型当中，每一个位置的权重值依赖于文档频率df和文档中词项的频率tf
# 我们要在倒排索引表中记录某一词在某一文档中出现的频率tf
# 最初的思路是把倒排表中的每一项设置为一个二元的tuple
# 然而在python中tuple是immutable的
# 于是我打算把倒排表由list变成一个dictionary，key值为docID，属性值为该term在docID文档中出现的频率tf
def create_index(file_name):
    csv_file = open(file_name, 'r')
    csv_reader = csv.reader(csv_file)
    docID = 0
    inverted_index = {}
    for row in csv_reader:
        docID = docID + 1
        for string in row:
            if ' ' in string:
                word_list = split.split_word(string)  # 进行分词
                for word in word_list:
                    if word not in inverted_index:  # 若该词在倒排索引表中不存在
                        inverted_index[word] = {docID: 1}  # 在倒排索引表中添加该单词
                    elif docID not in inverted_index[word]:  # 若该词在倒排索引表中存在但该文档不在倒排表字典中
                        inverted_index[word][docID] = 1  # 在该词对应的倒排表字典中添加此文档的docID，并把tf设置为1
                    else:                                # 若该词在倒排索引表中存在且该文档在倒排表字典中就把tf+1
                        inverted_index[word][docID] += 1
            else:
                if string not in inverted_index:
                    inverted_index[string] = {docID: 1}
                elif docID not in inverted_index[string]:
                    inverted_index[string][docID] = 1
                else:
                    inverted_index[string][docID] += 1
    return inverted_index


# 获取csv表格的行数，即总文档个数N
def doc_num(file_name):
    csv_file = open(file_name, 'r')
    lines = csv_file.readlines()
    return len(lines)


def rename(file_name):
    pre_name = ''
    for letter in file_name:
        if letter != '.':
            pre_name += letter
        else:
            break
    return pre_name + '_index.txt'


# 创建倒排索引文件
def create_index_txt(file_name):
    index = create_index(file_name)
    new_name = rename(file_name)
    index_file = open(new_name, 'w')
    index_file.write(str(index))


# 读取倒排索引文件
def read_index_txt(file_name):
    new_name = rename(file_name)
    index_file = open(new_name, 'r')
    inverted_index = eval(index_file.read())
    return inverted_index


def get_index(filename):
    new_file_name = rename(filename)
    if os.path.isfile(new_file_name):  # 若已经有倒排索引表了
        fr = open(new_file_name, 'r')  # 读取倒排索引表
        inverted_index = eval(fr.read())
        fr.close()
    else:                                                  # 若还没有倒排索引表
        inverted_index = create_index(filename)       # 创建新的倒排索引表
        fw = open(new_file_name, 'w')                      # 写入和要查找的文件相同的目录下
        fw.write(str(inverted_index))
        fw.close()
    return inverted_index


