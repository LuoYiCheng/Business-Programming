input_str1 = input()
input_list = input_str1.split()
for i in range(len(input_list)):  #  先取list的長度，再用range()創造一個iterable Object
    input_list[i] = int(input_list[i])
n_town = input_list[0]

all_info_towns = []  #  建立一個即將包含所有城鎮資訊的 Nest List ， All_info_towns[i] 表示第i個城鎮， 
                     #  All_info_town[i][j] 表示第i個城鎮的資訊，由小至大分別是：x座標、y座標、城鎮人口數

# Input策略：在外層迴圈中先依照題目給定的城鎮數設定為總次數，因此我們需要input n次，馬上使用split()將字串轉成清單，接著再利用第二層迴圈將清單內的字串轉成整數
for town in range(n_town):
    info_town_str = input()
    info_town_list = info_town_str.split()
    for info in range(len(info_town_list)):  #  先取list的長度，再用range()創造一個iterable Object
        info_town_list[info] = int(info_town_list[info])
    all_info_towns.append(info_town_list)  #  將每次外層迴圈的結果append到Nest List



# 分別建立座標清單和人口清單
coordinate_list = [all_info_towns[i][0:2] for i in range(len(all_info_towns))]
pop_list = [all_info_towns[i][2] for i in range(len(all_info_towns))]
# print('coordinate_list: ', coordinate_list)
# print('pop_list: ', pop_list)

# 建立距離清單，dist_list[i][j]表示第i個城鎮到第j個城鎮的幾何距離
import math
dist_list = []
for i in range(n_town):
    sub_dist_list = []
    for j in range(n_town):
        # sub_dist_list[j] = ((coordinate_list[i][0] - coordinate_list[j][0])**2 + (coordinate_list[i][1] - coordinate_list[j][1])**2)**0.5  
        # PS.因為不能修改list中不存在的index值，所以上行的程式會導致Index Error
        dist = ((coordinate_list[i][0] - coordinate_list[j][0])**2 + (coordinate_list[i][1] - coordinate_list[j][1])**2)**0.5
        sub_dist_list.append(round(dist, 2))
    dist_list.append(sub_dist_list)
# print('dist_list: ', dist_list)

# 演算法
n_base_station = input_list[1]
cover_radius = input_list[2]
station_list = []
total_cover_pop = 0
for p in range(n_base_station):  #  最外層loop將選出p個基地台
    max_cover_pop = 0  # 本次迴圈中，最多可覆蓋的人數
    whole_cover_list = []

    for i in range(n_town):
        i_cover_list = []  #  作為我們提取pop_list的index

        for j in range(n_town):
            if dist_list[i][j] <= cover_radius:  # 如果兩個城鎮之間的幾何距離小於等於半徑，則該城鎮將被append到i_cover_list中
                i_cover_list.append(j)
        i_cover_pop = sum([pop_list[covered] for covered in i_cover_list])
        # print('第' + str(i) + '個城鎮覆蓋城鎮人數: ', i_cover_pop)
        whole_cover_list.append(i_cover_list)

        # 如果當前覆蓋城鎮人數大於最多可覆蓋人數，我們就暫定選該城鎮，直到找出最佳的城鎮
        if i_cover_pop > max_cover_pop:  # 不使用>=是因為我們要選編號較小的那一個
            max_cover_pop = i_cover_pop
            build_station = i

    station_list.append(build_station)  # 將選定的town加入基地台list
    total_cover_pop += max_cover_pop

    for town in whole_cover_list[build_station]:  # 將已被基地台涵蓋的城鎮人口數歸0
        pop_list[town] = 0 

    
    # print('我們蓋在第',build_station, '+1個城鎮')
    # print('本輪各個城鎮Cover的城鎮:', whole_cover_list)
    # print('目前未被基地台涵蓋的人數:', pop_list)
    # print('已經蓋基地台的城鎮:', station_list)
    # print('目前基地台總Cover人數:', total_cover_pop)

#輸出最後結果
for i in range(n_base_station):
    print(station_list[i] + 1, end=' ')
print(total_cover_pop)

# 運算時間0.011315584182739258

""" 
Debug 2022/2/26
一開始我選擇建立了一個un_build_list去存放還沒建造基地台的城鎮，這樣在跑i層迴圈的時候就可以只針對那些還沒被建造的城鎮運算就好，希望能夠提高運算效率
不過遇到了一個問題是，隨著un_build_list的數量越來越少，導致line64的
    for town in whole_cover_list[build_station]:
        pop_list[town] = 0 
發生了index error，原因是whole_cover_list也越來越短，當whole_cover_list需要索引到編號更大的i時，已經超出了list的長度，針對該問題我尚未想到解決方案
但是我想到如果直接捨棄建立un_build_list的方法，也能達到我們想要的結果，因為我們會隨著每次迴圈把每個城鎮未涵蓋的人數減掉，只是比較麻煩的是每次都要針對
全部的城鎮重算一次，如果我有想出解決上述的方法再來比較運算速率唄
"""
