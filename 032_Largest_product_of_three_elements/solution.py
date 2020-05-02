from itertools import combinations


def three_products(three_nums):
    res = 1
    for ele in three_nums:
        res *= ele

    return res


def maximum_product_of_three(lst):
    all_products = []
    for each in list(combinations(lst, 3)):
        all_products.append(three_products(each))

    return max(all_products) if all_products else 0


nums = [-4, -4, 2, 8]
print(maximum_product_of_three(nums))
# 128

nums = [4, 1, 3, 2, 6, 5]
print(maximum_product_of_three(nums))
# 120
