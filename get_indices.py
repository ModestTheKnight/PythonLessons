def get_indices(sourcelist, s_elem):
    indexlist=[]
    for s in range(len(sourcelist)):
        if sourcelist[s]==s_elem:
            indexlist.append(s)
    return(indexlist)
lst_test=[["a", "a", "b", "a", "b", "a"],[1, 5, 5, 2, 7],[1, 5, 5, 2, 7],[1, 5, 5, 2, 7]]
elem_test=["a",7,5,8]
for k in range(len(elem_test)):
    print(get_indices(lst_test[k],elem_test[k]))
