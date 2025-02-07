import csv
import sys

# def ():
#     pass

def main():
    print(sys.argv[1])
    as_dict = {}
    with open(file, 'r') as file:
        for row in file:
            prod, cage, sku, unkown = row.strip('"').split(',')
            as_dict['product_info':prod, 'cage':cage, 'sku':sku,'unkown0':unkown]
    return(print(as_dict))


def csv_to_df():
    pass

def join_dfs():
    pass


if __name__ =='__main__':
    main