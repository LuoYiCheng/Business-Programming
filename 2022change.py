import os
path = r'C:\Users\Yicheng\Desktop\NTU\110-2\bussiness programming\homework\week_homework' # 這就是欲進行檔名更改的檔案路徑
files = os.listdir(path)
print(files) # 印出讀取到的檔名稱，用來確認自己是不是真的有讀到

os.chdir(path)
for i in range(len(files)): # 因為資料夾裡面的檔案都要重新更換名稱
	oldname = files[i] # 指出檔案現在的路徑名稱，[n]表示第n個檔案
	newname = str(i) + '_' + oldname # 在本案例中的命名規則為：年份+ - + 次序
	os.rename(oldname, newname)
	print(oldname+'>>>'+newname) # 印出原名與更名後的新名，可以進一步的確認每個檔案的新舊對應
