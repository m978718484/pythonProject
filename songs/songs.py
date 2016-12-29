
# 将歌曲存入字典
def add_songs_to_dict(key,content):
	if key not in songs:
		songs[key] = [content]
	else:
		songs[key].append(content)	

# 将歌曲拆分并存放到字典中
def split_song_content(song_content):
	temp = song_content.replace('\n','').split('\t')
	t = (temp[0],temp[1],temp[3],temp[4])
	add_songs_to_dict(temp[2],t)

# 读取歌曲列表
def load_songs():
	f = open('itunes.txt','r')
	all_text_lines =f.readlines()
	f.close()
	for song_content in all_text_lines:
		split_song_content(song_content)
# 打印操作选项
def print_opt():
	print ('请选择数字操作：')
	print ('1.名字 2.专辑 3.类型 4.添加 5.删除 6.流行 7.最长')

#  用于存放歌曲元数据的字典
songs = {}
if __name__ == '__main__':
	load_songs()
	# print(songs)
	while True:
		print_opt()
		i = input()
		if i == '1':
			singer = input('请输入艺人名：')
			if singer in songs:
				for song in songs[singer]:
					print(song[0])    # 打印出输入艺人的歌曲名
			else:
				print('not exists!')  # 如果输入的艺人名不存在
		if i=='2':
			album = input('请输入专辑名：') # 获取用户输入的专辑名
			for key in songs.keys():
				for song in songs[key]:
					if song[2] == album:
						print(song[0]) #打印输入专辑所有的歌曲名
				
		if i=='3':
			style = input('请输入类型：')
			for key in songs.keys():
				for song in songs[key]:
					if song[3] == style:
						print(song[0]) #打印输入类型所有的歌曲名				
		if i=='4':
			print('请依次输入：歌名\t时长\t演唱家\t专辑\t类型 ')
			temp_song = input()
			split_song_content(temp_song)
			input_name = temp_song.split('\t')
			print(songs[input_name[2]])
		if i=='5':
			song_name = input("请输入要删除的乐曲名：")
			for key in songs.keys():
				for song in songs[key]:
					if song[0] == song_name:
						print(song)
						songs[key].remove(song)
		if i=='6':
			max_songs = 0
			max_key = ''
			for key in songs.keys():
				if len(songs[key]) >= max_songs:
					max_songs = len(songs[key])
					max_key = key
			print(max_key,max_songs)

		if i=='7':
			max_time = 0
			max_time_key = ''
			for key in songs.keys():
				for song in songs[key]:
					temp_time = int(song[1].replace(':',''))
					if temp_time >= max_time:
						max_time = temp_time
						max_time_key = key
			print(songs[max_time_key])
		if i=='0':
			break

