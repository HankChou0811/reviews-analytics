import time
import progressbar


data = []
count = 0 #透過記數來了解程式運算狀況的一種方法
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
#以上為一套把檔案載入的公式
		count += 1 # 也就是count = count + 1
		bar.update(count)
		# if count % 1000 == 0: # %是求餘數 也就是"如果count跟一千的餘數是0:"
		# 	print(len(data))

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
print(new[1])

good = []
for each in data:
	if 'good' in each:
		good.append(each)#如果留言裡有GOOD，那就從EACH裝進去GOOD的清單
print('the total amount of "good" reviews is', len(good))
print(good[10])


#文字記數

wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增第一次讀取到的字就是等於1


for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word]) 

print(len(wc))
print(wc['Allen'])

while True:
	word = input('please enter the word u want to search:')
	if word == 'q':
		break
	print(word, 'appearing', wc[word], 'times')

print('ty')


#以下為快寫法
good = [each for each in data if 'good' in each]
#課程第4節第57站有講到
#第一個each就是如果公式成立，要把什麼"東西"裝進good清單當中
good = [each + 10 for each in data if 'bad' in each]
