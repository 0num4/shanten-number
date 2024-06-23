import shanten_number

calc = shanten_number.Calsht()
init_calc = calc.initialize(".")

# 手牌の設定
hand = [
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,  # manzu
    0,
    1,
    0,
    1,
    1,
    0,
    2,
    0,
    1,  # pinzu
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,  # souzu
    1,
    0,
    1,
    0,
    3,
    0,
    0,  # jihai
]

# シャンテン数とモードを計算
sht, mode = calc(hand, 4, 7)

# 結果を表示
print(sht)
print(mode)
# result = calc(hand, m)  # hand_dataとmを適切に置き換えてください
# print(result)


def test_shanten_number():
    # 手牌の設定
    # 手牌の設定
    # orig_hand = [
    #     1, 1, 1, 0, 0, 0, 0, 0, 0,  # manzu
    #     1, 1, 0, 1, 1, 0, 2, 0, 1,  # pinzu
    #     0, 0, 0, 0, 0, 0, 0, 0, 0,  # souzu
    #     1, 0, 1, 0, 3, 0, 0         # jihai
    # ]
    # hand = [
    #     3, 0, 0, 0, 0, 0, 0, 0, 0,  # manzu
    #     3, 0, 0, 0, 0, 0, 0, 0, 0,  # pinzu
    #     3, 0, 0, 0, 0, 0, 0, 0, 3,  # souzu
    #     1, 1, 0, 0, 0, 0, 0         # jihai
    # ]
    # 牌は14枚or14枚+1。この例のhandは既に上がってる。0。
    sht, mode = calc(hand, 4, 7)
    # assert sht == 0
    # assert mode == 0
    print(sht, mode)
    print("test passed")


test_shanten_number()
