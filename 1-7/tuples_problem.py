def hash_of_tuple(int_list):
    tupla = tuple(int_list)
    return hash(tupla)

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash_of_tuple(integer_list))