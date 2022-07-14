n_stop = int(input()) # n個車站
available_sits = int(input()) # 為了下面算法，我將題目給定的最大乘客數K，轉成閒置座位數，直接以該變數進行後續運算

for i in range(n_stop):
    i_stop_passengers = int(input())  # 讀入第i站有多少乘客
    
    # 先檢查公車行駛至該站時車上是否為滿載狀態      
    if available_sits == 0:
        full_stop = i + 1  # 在第i站遇到滿員狀況 (為了輸出結果所以+1)
        overload = i_stop_passengers  # 該站無法上車之乘客數即為該站人數
    
    # 若上述狀況沒發生，繼續檢查公車是否能夠載完第i站的乘客
    available_sits -= i_stop_passengers        
    if available_sits < 0:
        full_stop = i + 1
        overload = -(available_sits)  # 將負數的座位取正數即為該站無法上車之乘客數
        print(full_stop, overload, sep=',')  # 輸出結果
        break  # 跳出迴圈
    
if available_sits >= 0:
    print(0)