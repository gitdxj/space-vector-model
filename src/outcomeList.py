import order
import index
import spaceVectorModel


def get_outcome_list(filename, query_content):
    inverted_index = index.get_index(filename)
    N = index.doc_num(filename)
    query_content_array_list = spaceVectorModel.get_query_content_array_list(query_content, inverted_index, N)
    doc_mat_list = spaceVectorModel.get_doc_mat_list(inverted_index, N)
    outcome = spaceVectorModel.array_times_mat_outcome(query_content_array_list, doc_mat_list)
    outcome_list = order.get_order_list(outcome)
    return outcome_list