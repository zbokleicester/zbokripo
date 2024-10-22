# function.py


def several_zeros():

    

    return [0] * 10

def several_zeros_custom(nb_zeros):


    return [0] * nb_zeros

def matrix(rows = 3, cols = 3): 
    
    return [rows*[cols*[0]]]



if __name__ == '__main__':

    print(several_zeros())
    print(several_zeros_custom(30))
    result_matrix = matrix(0, 0)
    # print(result[2][3]) # error
    # print(result[1][2]) # 0
    # print(result[0]) # [0, 0, 0]
    # print(matrix(0,0))
    print(matrix())
    # print(result_matrix[1])

    # print(row[1])

    # for item in row1:
    #     print(item)
