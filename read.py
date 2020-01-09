data = []
count = 0 #透過記數來了解程式運算狀況的一種方法
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
#以上為一套把檔案載入的公式
		count += 1 # 也就是count = count + 1
		if count % 1000 == 0: # %是求餘數 也就是"如果count跟一千的餘數是0:"
			print(len(data))

print('檔案讀取完畢，共有', len(data), '資料')

sum_len = 0
for d in data: #每個D都是個字串
	sum_len = sum_len + len(d)
print('the average len of reviews is', sum_len/len(data))

#篩選

new = []
for each in data: # 把這個清單中的東西一個一個拿出來, each就是每個留言
	if len(each) < 100:
		new.append(d) # 如果你的長度小於100，我就把你裝進NEW這個清單內
 #要是放在for的框框內 那他就會一直印下去，只印一次就該跳出框框
print('the total is', len(new),'which is shorter than 100 words')
print(new[0])
