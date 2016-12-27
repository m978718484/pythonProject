# -*- coding: utf-8 -*-
import sys

def add_songs_to_dict(key,content):
	if not songs.has_key(key):
		songs[key] = t
	else:
		songs[key].append(t)	

def split_song_content(song_content):
	temp = song_content.split('\t')
	t = [(temp[0],temp[2],temp[3],temp[4])]
	add_songs_to_dict(temp[1],t)

def load_songs():
	all_the_text = open('songs.txt').read()
	list_songs = all_the_text.split('\n')
	for song_content in list_songs:
		split_song_content(song_content)

def print_opt():
	print ('请选择数字操作：')
	print ('1.名字 2.专辑 3.类型 4.添加 5.删除 6.流行 7.最长')


songs = {}
if __name__ == '__main__':
	print_opt()
	while True:
		i = raw_input()
		if i == '1':
			singer = raw_input('請輸入藝人名：')
			if songs.has_key(singer):
				for song in song[singer]:
					print(song[0])    # 打印出輸入藝人的歌曲名
			else:
				print('not exists!')  # 如果輸入的藝人名不存在
		if i=='2':
			album = raw_input('請輸入專輯名：') # 獲取用戶輸入的專輯名
			for key in songs.keys():
				if songs[key][2] == album:
					print(song[0]) #打印輸入專輯所有的歌曲名
				
		if i=='3':
			style = raw_input('請輸入類型：')
			for key in songs.keys():
				if songs[key][3] == style:
					print(song[0]) #打印輸入類型所有的歌曲名				
		if i=='4':
			temp_song = raw_input('請依次按：歌曲名\t藝人名\t專輯名\t歌曲類型\t歌曲時長 格式輸入')
			split_song_content(temp_song) 



