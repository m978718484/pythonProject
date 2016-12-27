# -*- coding: utf-8 -*-
import sys

def add_songs_to_dict(key,content):
	if key not in songs:
		songs[key] = [content]
	else:
		songs[key].append(content)	

def split_song_content(song_content):
	temp = song_content.replace('\n','').split('\t')
	t = (temp[0],temp[1],temp[3],temp[4])
	add_songs_to_dict(temp[2],t)

def load_songs():
	f = open('itunes.txt','r')
	all_text_lines =f.readlines()
	f.close()
	for song_content in all_text_lines:
		split_song_content(song_content)

def print_opt():
	print ('请选择数字操作：')
	print ('1.名字 2.专辑 3.类型 4.添加 5.删除 6.流行 7.最长')


songs = {}
if __name__ == '__main__':
	load_songs()
	print(songs)
	while True:
		print_opt()
		i = input()
		if i == '1':
			singer = input('請輸入藝人名：')
			if singer in songs:
				for song in songs[singer]:
					print(song[0])    # 打印出輸入藝人的歌曲名
			else:
				print('not exists!')  # 如果輸入的藝人名不存在
		if i=='2':
			album = input('請輸入專輯名：') # 獲取用戶輸入的專輯名
			for key in songs.keys():
				for song in songs[key]:
					if song[2] == album:
						print(song[0]) #打印輸入專輯所有的歌曲名
				
		if i=='3':
			style = input('請輸入類型：')
			for key in songs.keys():
				for song in songs[key]:
					if song[3] == style:
						print(song[0]) #打印輸入類型所有的歌曲名				
		if i=='4':
			print('請依次輸入：歌名\t時長\t演唱家\t專輯\t類型 ')
			temp_song = input()
			split_song_content(temp_song)
			input_name = temp_song.split('\t')
			print(songs[input_name[2]])
		if i=='5':
			song_name = input("請輸入要刪除的樂曲名：")
			for key in songs.keys():
				for song in songs[key]:
					if song[0] == song_name:
						songs[key].remove(song)
					print(songs)
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

