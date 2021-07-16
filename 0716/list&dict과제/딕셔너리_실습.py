#딕셔너리 실습1

# 1-1. 자신의 이름, 나이, 인사말로 구성된 my_info dictionary를 만들어보시오.

my_info_dictionary = {'이름' : '김동현', '나이' : 27 , '인사말' : '반가워요'}



# 1-2. my_info 딕셔너리에서 나이만 출력하시오.

print(my_info_dictionary['나이'])

#----------------------------------------------------
# 2.
coin = {
    'BTC': {
        'opening_price': '44405000',
        'closing_price': '38806000',
        'min_price': '36640000',
        'max_price': '44999000',
        'prev_closing_price': '44404000',
        'fluctate_24H': '-7463000',
        'fluctate_rate_24H': '-16.13',
    },
    'ETH': {
        'opening_price': '1458000',
        'closing_price': '1229000',
        'min_price': '1100000',
        'max_price': '1490000',
        'prev_closing_price': '1458000',
        'fluctate_24H': '-275000',
        'fluctate_rate_24H': '-18.28',
    },
    'XRP': {
        'opening_price': '364.5',
        'closing_price': '311.9',
        'min_price': '284.2',
        'max_price': '372.7',
        'prev_closing_price': '364.2',
        'fluctate_24H': '-90.6',
        'fluctate_rate_24H': '-22.51',
    },
}


# 2-1. 코인의 정보에서 BTC의 최대 가격을 출력하시오.

print(coin['BTC']['max_price'])

# 2-2. BTC의 시가와(opening price) XRP의 시가를 더한 결과를 출력하시오.

print(coin['BTC']['opening_price'] + coin['XRP']['opening_price'])