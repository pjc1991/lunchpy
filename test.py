
def get_discount_rate(original_price, result_price):
    percent = (1 - result_price / original_price) * 100
    if percent % 1 == 0:
        print("found it!")
    return percent

if __name__ =='__main__':
    # result price should be 369000
    # original price is about 599000

    # original price from 650000 to 500000
    # for loop

    for i in range(999999, 369000, -1):
        result = get_discount_rate(i, 369000)
        if result % 1 == 0:
            print(i, result)

    # result
    # 650000 599000.0

    
    
