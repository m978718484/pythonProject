user_mail = {}
last_content = ''
last_user = ''
with open('data.txt') as f:
	for line in f:
		line = line.replace('\n','')
		if '@' in line:
			last_user = line
		else:
			last_content = line

		if user_mail.has_key(last_user):
			user_mail[last_user].append(last_content)
		else:
			user_mail[line] = [last_content]
		last_content = ''
print user_mail['zhangsan@163.com']