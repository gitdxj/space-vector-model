import numpy
import math
# 把检索字段当作一个文档
# 计算其tf，df则是使用被检索的文档
# 得到被检索文档的权值向量


def tf_idf(tf, df, N):
    if tf == 0:
        return 0
    w = 1 + math.log10(tf)
    w = w * math.log10(N/df)
    return w


def get_query_content_array_list(query_content, inverted_index, N):
    query_word_list = query_content.split()
    query_content_array_list = []
    for term in inverted_index:
        term_tf = 0
        for word in query_word_list:
            if word == term:
                term_tf = term_tf + 1
        term_df = len(inverted_index[term])
        term_w = tf_idf(term_tf, term_df, N)
        query_content_array_list.append(term_w)  # 这里得到了查询语句的词频向量
    return query_content_array_list


# 获取某一词项的df
def get_df(term, inverted_index):
    doc_list = inverted_index[term]
    return len(doc_list)


# 现在我们要计算文档集的权重矩阵
# 权重矩阵的形式如下：
#       docID   1     2     3
# term
# Frank         5.52  3.18  0.0
# good          1.21  0.0   1.34
# ...           ...   ...   ...
# 我们根据倒排索引表来得到这样的矩阵
# 根据倒排索引表中的每一个词项可以很容易得到矩阵中的一个横行
# 最后再把他们连接起来即可
def get_term_array_list(term, inverted_index, N):
    term_df = get_df(term, inverted_index)
    postings = inverted_index[term]  # postings是一个字典，key值为docID，属性值是tf
    term_array_list = []  # 代表着权重矩阵中的一横行
    for i in range(1, N+1):
        if i in postings:
            term_tf = postings[i]
        else:
            term_tf = 0
        term_w = tf_idf(term_tf, term_df, N)
        term_array_list.append(term_w)
    return term_array_list


# 获取权值矩阵（以list的形式）
def get_doc_mat_list(inverted_index, N):
    doc_mat_list = []
    for term in inverted_index:
        term_array_list = get_term_array_list(term, inverted_index, N)
        doc_mat_list.append(term_array_list)
    return doc_mat_list


# 归一化的权值矩阵和查询向量相乘后的结果
def array_times_mat_outcome(query_content_array_list, doc_mat_list):
    query_content_array = numpy.array(query_content_array_list)
    query_content_array_length = numpy.linalg.norm(query_content_array)  # 向量欧几里得长度
    length_1_array = query_content_array / query_content_array_length  # 做了归一化后的向量
    doc_mat = numpy.mat(doc_mat_list)
    column_num = doc_mat.shape[1]  # 权值矩阵的列数
    outcome_list = []
    for column in range(column_num):
        column_array = doc_mat[:, column]
        column_array_length = numpy.linalg.norm(column_array)
        length_1_column_array = column_array / column_array_length
        outcome_list_term = length_1_array*length_1_column_array
        outcome_list_term = outcome_list_term.tolist()
        outcome_list_term = outcome_list_term[0][0]
        outcome_list.append(outcome_list_term)
    return outcome_list


if __name__ == '__main__':
    a = numpy.array([1, 3])
    b = numpy.mat([[3, 4], [5, 6]])
    b1column = b[:, 0]
    times = a * b1column

    print(type(times.tolist()[0][0]))
