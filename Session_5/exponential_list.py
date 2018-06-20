def exponential():

    index_number = []
    for i in range(11):
        index_number.append(i)

    exponential_list = []
    
    for j in range(len(index_number)):
        exponential_list.append(2 ** index_number[j])

    return exponential_list
