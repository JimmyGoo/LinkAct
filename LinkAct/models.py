from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from TermProject import settings
import ast
import json
import types
import string

# Create your models here.
#show what front page need

	
class MyUser(models.Model):
	#与其关联的默认User
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	#昵称
	nickname = models.CharField(max_length = 20, default = '')
	#生日
	birthday = models.DateField(default = date.today)
	#好友
	friends = models.CharField(max_length = 300, default = '[]')
	#主页地址
	website = models.URLField()
	#所在城市
	city = models.CharField(max_length = 20, default = '')
	#头像
	head = models.IntegerField(default = -1)
	#已完成活动：参与&发起
	participate_terminative_acts = models.CharField(max_length = 300, default = '[]')
	create_terminative_acts = models.CharField(max_length = 300, default = '[]')
	#进行中活动：参与&发起
	participate_ongoing_acts = models.CharField(max_length = 300, default = '[]')
	create_ongoing_acts = models.CharField(max_length = 300, default = '[]')
	#评论过的活动
	commented_acts = models.CharField(max_length = 300, default = '[]')
	#性别
	gender = models.CharField(max_length = 20, default = '')
	#兴趣
	interests = models.CharField(max_length = 300, default = '[]')
	#电话号码
	phone_number = models.CharField(max_length = 20, default = '')
	#待处理好友请求         #new_pos
	waiting_deal_friends = models.CharField(max_length = 300, default = '[]')
	 #好友列表

	friends = models.CharField(max_length = 300, default = '[]')
	friend_movement_id = models.CharField(max_length = 300, default = '[]')
	friend_movement = models.CharField(max_length = 300, default = '[]')
	movement_name = models.CharField(max_length = 300, default = '[]')
	movement_link = models.CharField(max_length = 300, default = '[]')

	#get attribute
	def get_friend_movement_id(self):
		if isinstance(self.friend_movement_id, str):
			return json.loads(self.friend_movement_id)
		return self.friend_movement_id
	def get_friend_movement(self):
		if isinstance(self.friend_movement, str):
			return json.loads(self.friend_movement)
		return self.friend_movement
	def get_movement_name(self):
		if isinstance(self.movement_name, str):
			return json.loads(self.movement_name)
		return self.movement_name
	def get_movement_link(self):
		if isinstance(self.movement_link, str):
			return json.loads(self.movement_link)
		return self.movement_link
	def get_username(self):
		return self.user.get_username()
	def get_nickname(self):
		return self.nickname
	def get_id(self):
		return self.user.id
	def get_birthday(self):
		return self.birthday
	def get_friends(self):
		if isinstance(self.friends, str):
			return json.loads(self.friends)
		return self.friends
	# def get_website(self):
	# 	return self.website
	def get_email(self):
		return self.user.email
	def get_city(self):
		return self.city
	def get_participate_terminative_acts(self):
		if isinstance(self.participate_terminative_acts, str):
			return json.loads(self.participate_terminative_acts)
		return self.participate_terminative_acts
	def get_create_terminative_acts(self):
		if isinstance(self.create_terminative_acts, str):
			return json.loads(self.create_terminative_acts)
		return self.create_terminative_acts
	def get_participate_ongoing_acts(self):
		if isinstance(self.participate_ongoing_acts, str):
			return json.loads(self.participate_ongoing_acts)
		return self.participate_ongoing_acts
	def get_create_ongoing_acts(self):
		if isinstance(self.create_ongoing_acts, str):
			return json.loads(self.create_ongoing_acts)
		return self.create_ongoing_acts
	def get_commented_acts(self):
		if isinstance(self.commented_acts, str):
			return json.loads(self.commented_acts)
		return self.commented_acts
	def get_gender(self):
		return self.gender
	def get_interests(self):
		if isinstance(self.interests, str):
			return json.loads(self.interests)
		return self.interests
	def get_head(self):
		return self.head
	def get_waiting(self):
		if isinstance(self.waiting_deal_friends, str):
			return json.loads(self.waiting_deal_friends)
		return self.waiting_deal_friends


	#set attribute

	def set_friend_movement_id(self, friend_movement_id):
		if isinstance(friend_movement_id, str):
			self.friend_movement_id = friend_movement_id
		else:
			self.friend_movement_id = json.dumps(friend_movement_id)
		self.save()
	def append_friend_movement_id(self, friend_movement_id):
		f = self.get_friend_movement_id()

		f.append(friend_movement_id)
		self.friend_movement_id = json.dumps(f)
		self.save()
	def clear_friend_movement_id(self):
		temp = []
		self.set_friend_movement_id(temp)
	def remove_friend_movement(self, friend_movement):
		f = self.get_friend_movement_id()
		if friend_movement_id in f:
			f.remove(friend_movement_id)
			self.friend_movement_id = json.dumps(f)
			self.save()
			return True
		self.friend_movement_id = json.dumps(f)
		self.save()
		return False


	def set_friend_movement(self, friend_movement):
		if isinstance(friend_movement, str):
			self.friend_movement = friend_movement
		else:
			self.friend_movement = json.dumps(friend_movement)
		self.save()
	def append_friend_movement(self, friend_movement):
		f = self.get_friend_movement()
		f.append(friend_movement)
		self.friend_movement = json.dumps(f)
		self.save()
	def remove_friend_movement(self, friend_movement):
		f = self.get_friend_movement()
		if friend_movement in f:
			f.remove(friend_movement)
			self.friend_movement = json.dumps(f)
			self.save()
			return True
		self.friend_movement = json.dumps(f)
		self.save()
		return False
	def clear_friend_movement(self):
		temp = []
		self.set_friend_movement(temp)
	def set_movement_name(self, movement_name):
		if isinstance(movement_name, str):
			self.movement_name = movement_name
		else:
			self.movement_name = json.dumps(movement_name)
		self.save()
	def append_movement_name(self, movement_name):
		f = self.get_movement_name()
		f.append(movement_name)
		self.movement_name = json.dumps(f)
		self.save()
	def remove_movement_name(self, movement_name):
		f = self.get_movement_name()
		if movement_name in f:
			f.remove(movement_name)
			self.movement_name = json.dumps(f)
			self.save()
			return True
		self.movement_name = json.dumps(f)
		self.save()
		return False
	def clear_movement_name(self):
		temp = []
		self.set_movement_name(temp)
	def set_movement_link(self, movement_link):
		if isinstance(movement_link, str):
			self.movement_link = movement_link
		else:
			self.movement_link = json.dumps(movement_link)
		self.save()
	def append_movement_link(self, movement_link):
		f = self.get_movement_link()
		f.append(movement_link)
		self.movement_link = json.dumps(f)
		self.save()
	def remove_movement_link(self, movement_link):
		f = self.get_movement_link()
		if movement_link in f:
			f.remove(movement_link)
			self.movement_link = json.dumps(f)
			self.save()
			return True
		self.movement_link = json.dumps(f)
		self.save()
		return False
	def clear_movement_link(self):
		temp = []
		self.set_movement_link(temp)
	def set_username(self, username):
		self.user.username = username
		self.user.save()
		self.save()
	def set_nickname(self, nickname):
		self.nickname = nickname
		self.save()
	def set_birthday(self, birthday):
		self.birthday = birthday
		self.save()
	def set_friends(self, friends):
		if isinstance(friends, str):
			self.friends = friends
		else:
			self.friends = json.dumps(friends)
		self.save()
	def append_friends(self, friend_id):
		f = self.get_friends()
		if friend_id not in f:
			f.append(friend_id)
			self.friends = json.dumps(f)
			self.save()
			return True
		self.friends = json.dumps(f)
		self.save()
		return False
	def remove_friends(self, friend_id):
		f = self.get_friends()
		if friend_id in f:
			f.remove(friend_id)
			self.friends = json.dumps(f)
			self.save()
			return True
		self.friends = json.dumps(f)
		self.save()
		return False
	# def set_website(self, website):
	# 	self.website = website
	# 	self.save()
	def set_email(self, email):
		self.user.email = email
		self.user.save()
		self.save()
	def set_city(self, city):
		self.city = city
		self.save()
	def set_participate_terminative_acts(self, participate_terminative_acts):
		if isinstance(participate_terminative_acts, str):
			self.participate_terminative_acts = participate_terminative_acts
		else:
			self.participate_terminative_acts = json.dumps(participate_terminative_acts)
		self.save()
	def append_participate_terminative_acts(self, act_id):
		pta = self.get_participate_terminative_acts()
		if act_id not in pta:
			pta.append(act_id)
			self.participate_terminative_acts = json.dumps(pta)
			self.save()
			return True
		self.participate_terminative_acts = json.dumps(pta)
		self.save()
		return False
	def remove_participate_terminative_acts(self, act_id):
		pta = self.get_participate_terminative_acts()
		if act_id in pta:
			pta.remove(act_id)
			self.participate_terminative_acts = json.dumps(pta)
			self.save()
			return True
		self.participate_terminative_acts = json.dumps(pta)
		self.save()
		return False
	def set_create_terminative_acts(self, create_terminative_acts):
		if isinstance(create_terminative_acts, str):
			self.create_terminative_acts = create_terminative_acts
		else:
			self.create_terminative_acts = json.dumps(create_terminative_acts)
		self.save()
	def append_create_terminative_acts(self, act_id):
		cta = self.get_create_terminative_acts()
		if act_id not in cta:
			cta.append(act_id)
			self.create_terminative_acts = json.dumps(cta)
			self.save()
			return True
		self.create_terminative_acts = json.dumps(cta)
		self.save()
		return False
	def remove_create_terminative_acts(self, act_id):
		cta = self.get_create_terminative_acts()
		if act_id in cta:
			cta.remove(act_id)
			self.create_terminative_acts = json.dumps(cta)
			self.save()
			return True
		self.create_terminative_acts = json.dumps(cta)
		self.save()
		return False
	def set_participate_ongoing_acts(self, participate_ongoing_acts):
		if isinstance(participate_ongoing_acts, str):
			self.participate_ongoing_acts = participate_ongoing_acts
		else:
			self.participate_ongoing_acts = json.dumps(participate_ongoing_acts)
		self.save()
	def append_participate_ongoing_acts(self, act_id):
		poa = self.get_participate_ongoing_acts()
		if act_id not in poa:
			poa.append(act_id)
			self.participate_ongoing_acts = json.dumps(poa)
			self.save()
			return True
		self.participate_ongoing_acts = json.dumps(poa)
		self.save()
		return False
	def remove_participate_ongoing_acts(self, act_id):
		poa = self.get_participate_ongoing_acts()
		if act_id in poa:
			poa.remove(act_id)
			self.participate_ongoing_acts = json.dumps(poa)
			self.save()
			return True
		self.participate_ongoing_acts = json.dumps(poa)
		self.save()
		return False
	def set_create_ongoing_acts(self, create_ongoing_acts):
		if isinstance(create_ongoing_acts, str):
			self.create_ongoing_acts = create_ongoing_acts
		else:
			self.create_ongoing_acts = json.dumps(create_ongoing_acts)
		self.save()
	def append_create_ongoing_acts(self, act_id):
		coa = self.get_create_ongoing_acts()
		if act_id not in coa:
			coa.append(act_id)
			self.create_ongoing_acts = json.dumps(coa)
			self.save()
			return True
		self.create_ongoing_acts = json.dumps(coa)
		self.save()
		return False
	def remove_create_ongoing_acts(self, act_id):
		coa = self.get_create_ongoing_acts()
		if act_id in coa:
			coa.remove(act_id)
			self.create_ongoing_acts = json.dumps(coa)
			self.save()
			return True
		self.create_ongoing_acts = json.dumps(coa)
		self.save()
		return False
	def set_commented_acts(self, commented_acts):
		if isinstance(commented_acts, str):
			self.commented_acts = commented_acts
		else:
			self.commented_acts = json.dumps(commented_acts)
		self.save()
	def append_commented_acts(self, act_id):
		ca = self.get_commented_acts()
		if act_id not in ca:
			ca.append(act_id)
			self.commented_acts = json.dumps(ca)
			self.save()
			return True
		self.commented_acts = json.dumps(ca)
		self.save()
		return False
	def remove_commented_acts(self, act_id):
		ca = self.get_commented_acts()
		if act_id in ca:
			ca.remove(act_id)
			self.commented_acts = json.dumps(ca)
			self.save()
			return True
		self.commented_acts = json.dumps(ca)
		self.save()
		return False
	def set_gender(self, gender):
		self.gender = gender
		self.save()
	def set_interests(self, interests):
		if isinstance(interests, str):
			self.interests = interests
		else:
			self.interests = json.dumps(interests)
		self.save()
	def append_interests(self, interest_id):
		ite = self.get_interests()
		if interest_id not in ite:
			ite.append(interest_id)
			self.interests = json.dumps(ite)
			self.save()
			return True
		self.interests = json.dumps(ite)
		self.save()
		return False
	def remove_interests(self, interest_id):
		ite = self.get_interests()
		if interest_id in ite:
			ite.remove(interest_id)
			self.interests = json.dumps(ite)
			self.save()
			return True
		self.interests = json.dumps(ite)
		self.save()
		return False
	def set_password(self, raw_password):
		self.user.set_password(raw_password)
		self.user.save()
		self.save()
	def set_gender(self, gender):
		
		self.gender = gender
		self.save()
			
	def set_head(self, head):
		self.head = head
		self.save()
	def append_waiting(self, requester_id):
		ite = self.get_waiting()
		if requester_id not in ite:
			ite.append(requester_id)
			self.waiting_deal_friends = json.dumps(ite)
			self.save()
			return True
		self.waiting_deal_friends = json.dumps(ite)
		self.save()
		return False
	def del_waiting_friends(self, requester_id):
		ite = self.get_waiting()
		if requester_id in ite:
			ite.remove(requester_id)
			self.waiting_deal_friends = json.dumps(ite)
			self.save()
			return True
		self.waiting_deal_friends = json.dumps(ite)
		self.save()
		return False

	def set_phonenumber(self, phone_number):
		self.phone_number = phone_number
		self.save()

	#tools
	def check_password(self, raw_password):
		return self.user.check_password(raw_password)
	def email_user(self, subject, message, from_email = None, **kwargs):
		self.user.email_user(subject, message, from_email, kwargs)

	def create_user(self, usernames, passwords, email, nickname):
				flag = True
				temp = User.objects.all()
				for item in temp:
						if item.username == usernames:
								flag = False
								break
				if flag:
						u = User.objects.create_user(username=usernames, password=passwords, email = email)
						u.save()
						self.user = u
						self.nickname = nickname
						self.birthday = date(1970, 1, 1)
						self.city = ''
						self.interests = '[]'
						self.save()
						return True
				else:
						return False
	def delete_user(self):
		a = self.user
		a.delete()
		self.delete()
	def create_activity(self, name, theme, locale, start_date, end_date, introduction, act_img_id):
		if not isinstance(theme, list):
			return False
		a = Activity()
		a.name = name
		a.theme = json.dumps(theme)
		a.locale = locale
		a.create_time = datetime.now()
		a.start_date = start_date
		a.end_date = end_date 
		a.introduction = introduction
		a.creator = self.get_id()
		a.act_image = act_img_id
		a.status = 'created'
		a.save()
		flag =  self.append_create_ongoing_acts(a.id)
		return flag
	def get_activities(self, kinds, order_base):
		acts = Activity.objects.order_by(order_base)
		if not isinstance(kinds, str):
			return []
		results = []
		if kinds == 'participate_terminative_acts':
			pta = self.get_participate_terminative_acts()
			results = [var for var in acts if var.id in pta]
		elif kinds == 'create_terminative_acts':
			cta = self.get_create_terminative_acts()
			results = [var for var in acts if var.id in cta]
		elif kinds == 'participate_ongoing_acts':
			poa = self.get_participate_ongoing_acts()
			results = [var for var in acts if var.id in poa]
		elif kinds == 'create_ongoing_acts':
			coa = self.get_create_ongoing_acts()
			results = [var for var in acts if var.id in coa]
		return results
	
	def activity_filter(self, style, reference):
		results = []
		for item in Activity.objects.all():
			results.append((item, 0))
		if style == 'theme':
			i = 0
			while i < len(results):
				temp = self.str_similar(reference, results[i][0].get_theme_content())	
				if temp >  results[i][1]:
					results[i] = (results[i][0], temp)
				i += 1
		elif style == 'status':
			i = 0
			while i < len(results):
				temp = self.str_similar(reference, results[i][0].get_status())
				if temp >  results[i][1]:
					results[i] = (results[i][0], temp)
				i += 1
		elif style == 'name':
			i = 0
			while i < len(results):
				temp = self.str_similar(reference, results[i][0].get_name())
				if temp >  results[i][1]:
					results[i] = (results[i][0], temp)
				i += 1	
		elif style == 'creator':
			i = 0
			while i < len(results):
				temp = self.str_similar(reference, User.objects.get(id = results[i][0].get_creator()).myuser.get_nickname())
				if temp >  results[i][1]:
					results[i] = (results[i][0], temp)
				temp = self.str_similar(reference, User.objects.get(id = results[i][0].get_creator()).myuser.get_username())
				if temp >  results[i][1]:
					results[i] = (results[i][0], temp)
				i += 1	
		elif style == 'locale':
			i = 0
			while i < len(results):
				temp = self.str_similar(reference, results[i][0].get_locale())
				if temp >  results[i][1]:
					results[i] = (results[i][0], temp)
				i += 1
		elif style == 'introduction':
			i = 0
			while i < len(results):
				temp = self.str_similar(reference, results[i][0].get_introduction())
				if temp >  results[i][1]:
					results[i] = (results[i][0], temp)
				i += 1
		i = 0
		while(i < len(results)):
			if results[i][1] == 0:
				del results[i]
			else:
				i += 1
		results = sorted(results, key = lambda asd:asd[1], reverse = True)
		result = []
		for x in results:
			result.append(x[0])
		return result
	def str_similar(self, s, t):
		if s == '' or t == '':
			return 0
		result = 0
		i = 0
		while(i < len(t)):
			j = 0
			while(True):
				if t[i + j] == s[j]:
					j = j + 1
				else:
					if j > result:
						result = j
					break
				if i + j >= len(t) or j >= len(s):
					if j > result:
						result = j
					break
			i = i + 1
		return result

	#data是一个MyUser数组，在该数组中进行查找，同时符合reference中的各种属性的MyUser,
	#reference中的属性不固定，例如：{'city':'重庆'}和{'city':'重庆', 'nickname': '偷心的鱼'}皆可,
	#属性可选范围是MyUser和User的所有属性
	def user_filter(self, style, reference):
		results = []
		for item in MyUser.objects.all():
			results.append((item, 0))
		if style == 'username':
			i = 0
			while i < len(results):
				temp = self.str_similar(reference, results[i][0].get_username())	
				if temp >  results[i][1]:
					results[i] = (results[i][0], temp)
				i += 1
					
		elif style == 'id':
			i = 0
			while i < len(results):
				if reference == results[i][0].get_id():
					results[i] = (results[i][0], 1)
				i += 1
		elif style == 'birthday':
			i = 0
			while i < len(results):
				temp = self.str_similar(reference, str(results[i][0].get_birthday()))
				if temp >  results[i][1]:
					results[i] = (results[i][0], temp)
				i += 1
		elif style == 'friends':
			i = 0
			while i < len(results):
				temp = [var for var in results[i].get_friends() if var in reference]
				if len(temp) >  results[i][1]:
					results[i] = (results[i][0], len(temp))
				i += 1
		elif style == 'email':
			i = 0
			while i < len(results):
				temp = self.str_similar(reference, results[i][0].get_email())
				if temp >  results[i][1]:
					results[i] = (results[i][0], temp)
				i += 1
		elif style == 'nickname':
			i = 0
			while i < len(results):
				temp = self.str_similar(reference, results[i][0].get_nickname())
				if temp >  results[i][1]:
					results[i] = (results[i][0], temp)
				i += 1
		elif style == 'city':
			i = 0
			while i < len(results):
				temp = self.str_similar(reference, results[i][0].get_city())
				if temp >  results[i][1]:
					results[i] = (results[i][0], temp)
				i += 1
		elif style == 'gender':
			i = 0
			while i < len(results):
				temp = self.str_similar(reference, results[i][0].get_gender())
				if temp >  results[i][1]:
					results[i] = (results[i][0], temp)
				i += 1
		elif style == 'interests':
			i = 0
			while i < len(results):
				temp = [var for var in results[i].get_interests() if var in reference]
				if len(temp) >  results[i][1]:
					results[i] = (results[i][0], len(temp))
				i += 1
		print('here', results)
		i = 0
		while(i < len(results)):
			if results[i][1] == 0:
				del results[i]
			else:
				i += 1
		results = sorted(results, key = lambda asd:asd[1], reverse = True)
		result = []
		for x in results:
			result.append(x[0])
		return result
	def create_comment(self, act_id, score, content):
		acts = Activity.objects.filter(id = act_id)
		if len(acts) == 0:
			return False
		else:
			act = acts[0]
			a = Comment()
			a.score = score
			a.content = content
			a.comment_time = datetime.now()
			a.commenter = self.get_id()
			a.save()
			act.append_comments(a.id)
			if a.score > 3:
				act.append_supporters(self.get_id())
			return True


	def get_recommended_user(self):
		temp = []
		for item in MyUser.objects.all():
			if item.get_id() != self.get_id() and item.id not in self.get_friends():
				temp.append((item, 0, [], 0, 0))

		
		i = 0
		while i < len(temp):
			#与用户的每一个共同爱好增加权值20
			same_interests = [var for var in self.get_interests() if var in temp[i][0].get_interests()]
			temp[i] = (temp[i][0], temp[i][1] + len(same_interests) * 20, temp[i][2], len(same_interests), temp[i][4])
			#与用户的每一个共同好友增加权值20
			same_friends = [var for var in self.get_friends() if var in temp[i][0].get_friends()]
			temp_same_friends = []
			for var in same_friends:
				temp_same_friends.append(MyUser.objects.get(id = var).get_nickname())
			temp[i] = (temp[i][0], temp[i][1] + len(same_friends) * 20, temp_same_friends, temp[i][3], temp[i][4])
			#与用户的每一个共同活动增加权值20
			self_acts = []
			for var in self.get_participate_terminative_acts():
				self_acts.append(var)
			for var in self.get_create_terminative_acts():
				self_acts.append(var)
			for var in self.get_participate_ongoing_acts():
				self_acts.append(var)
			for var in self.get_create_ongoing_acts():
				self_acts.append(var)
			same_acts = []
			for var in temp[i][0].get_participate_terminative_acts():
				if var in self_acts:
					same_acts.append(var)
			for var in temp[i][0].get_create_terminative_acts():
				if var in self_acts:
					same_acts.append(var)
			for var in temp[i][0].get_participate_ongoing_acts():
				if var in self_acts:
					same_acts.append(var)
			for var in temp[i][0].get_create_ongoing_acts():
				if var in self_acts:
					same_acts.append(var)
			temp[i] = (temp[i][0], temp[i][1] + len(same_acts) * 20, temp[i][2], temp[i][3], len(same_acts))
			#与用户城市的相似会增加权值
			similar = self.str_similar(self.get_city(), temp[i][0].get_city())
			temp[i] = (temp[i][0], temp[i][1] * (similar * 0.5 + 1), temp[i][2], temp[i][3], temp[i][4])
			i += 1
		#排序
		temp = sorted(temp, key = lambda asd:asd[1], reverse = True)
		result = []
		for x in temp:
			result.append((x[0], x[2], x[3], x[4]))
		return result


	def get_recommended_activities(self):
		temp = []
		for item in Activity.objects.all():
			temp.append((item, 0))
		
		i = 0
		while i < len(temp):
			#参与者人数越多权值越大，一个参与者权值加1，一个好友权值加100
			p = temp[i][0].get_participants()
			p.append(temp[i][0].get_creator())
			f = self.get_friends()
			for x in p:
				if x in f:
					temp[i] = (temp[i][0], temp[i][1] + 100)
				else:
					temp[i] = (temp[i][0], temp[i][1] + 1)
			#地点与用户相似会增加权值
			similar = self.str_similar(self.get_city(), temp[i][0].get_locale())
			temp[i] = (temp[i][0], temp[i][1] + similar * 5)
			#每一个与用户的爱好相关的主题增加权值10
			user_theme = []
			user_interests = self.get_interests()
			for user_interest in user_interests:
				for theme_id in Interest.objects.get(id = user_interest).get_linked_theme():
					user_theme.append(theme_id)
			act_theme = temp[i][0].get_theme()
			for theme_id in user_theme:
				if theme_id in act_theme:
					temp[i] = (temp[i][0], temp[i][1] + 10)
			if temp[i][0].get_status() == 'created':
				temp[i] = (temp[i][0], temp[i][1] + 1000)
			i += 1
		

		#剔除权值为0的和状态不是未开始的
		i = 0
		while(i < len(temp)):
			if temp[i][1] == 0 or temp[i][0].get_status() == 'finished':
				del temp[i]
			else:
				i += 1
		#排序
		temp = sorted(temp, key = lambda asd:asd[1], reverse = True)
		result = []
		for x in temp:
			result.append(x[0])
		return result


	def __str__(self):
		return self.nickname
		
class Activity(models.Model):
	#名字
	name = models.CharField(max_length = 20, default = '')
	#状态
	status = models.CharField(max_length = 20, default = '')
	#发起人ID
	creator = models.IntegerField()
	#参与人ID
	participants = models.CharField(max_length = 300, default = '[]')
	#地点
	locale = models.CharField(max_length = 20, default = '')
	#主题
	theme = models.CharField(max_length = 300, default = '[]')
	#发起时间
	create_time = models.DateTimeField(default = datetime.now)
	#开始时间
	start_date = models.DateTimeField(default = datetime.now)
	#结束时间
	end_date = models.DateTimeField(default = datetime.now)
	#发起介绍
	introduction = models.CharField(max_length = 500, default = '[]')
	#点赞人
	supporters = models.CharField(max_length = 300, default = '[]')
	#评论
	comments = models.CharField(max_length = 300, default = '[]')
	#缩略图
	act_image = models.IntegerField(default = -1)

	#get attribute
	def get_act_image(self):
		return self.act_image
	def get_name(self):
		return self.name
	def get_status(self):
		return self.status
	def get_id(self):
		return self.id
	def get_creator(self):
		return self.creator
	def get_participants(self):
		if isinstance(self.participants, str):
			return json.loads(self.participants)
		return self.participants
	def get_locale(self):
		return self.locale
	def get_theme(self):
		if isinstance(self.theme, str):
			return json.loads(self.theme)
		return self.theme
	def get_theme_content(self):
		temp = self.get_theme()
		result = ''
		for var in temp:
			if len(result) != 0:
				result += ','
			result += Theme.objects.get(id = var).get_content()
		return result
	def get_create_time(self):
		return self.create_time
	def get_start_date(self):
		return self.start_date
	def get_end_date(self):
		return self.end_date
	def get_introduction(self):
		return self.introduction
	def get_comments(self):
		if isinstance(self.comments, str):
			return json.loads(self.comments)
		return self.comments
	def get_comments_content(self):
		if isinstance(self.comments, str):
			temp = json.loads(self.comments)
		else:
			temp = self.comments
		result = []
		for index in range(0, len(temp)):
			result.append(Comment.objects.get(id=temp[index]))
		return result
	def get_supporters(self):
		if isinstance(self.supporters, str):
			return json.loads(self.supporters)
		return self.supporters

	#set
	def set_act_image(self, act_image):
		self.act_image = act_image
		self.save()
	def set_name(self, name):
		self.name = name
		self.save()
	def set_status(self, status):
		self.status = status
		self.save()
	def set_creator(self, creator):
		self.creator = creator
		self.save()
	def set_participants(self, participants):
		if isinstance(participants, str):
			self.participants = participants
		else:
			self.participants = json.dumps(participants)
		self.save()
	def append_participants(self, participant_id):
		p = self.get_participants()
		if participant_id not in p:
			p.append(participant_id)
			self.participants = json.dumps(p)
			self.save()
			return True
		self.participants = json.dumps(p)
		self.save()
		return False
	def remove_participants(self, participant_id):
		p = self.get_participants()
		if participant_id in p:
			p.remove(participant_id)
			self.participants = json.dumps(p)
			self.save()
			return True
		self.participants = json.dumps(p)
		self.save()
		return False
	def set_locale(self, locale):
		self.locale = locale
		self.save()
	def set_theme(self, theme):
		if isinstance(theme, str):
			self.theme = theme
		else:
			self.theme = json.dumps(theme)
		self.save()
	def append_theme(self, theme_id):
		t = self.get_theme()
		if theme_id not in t:
			t.append(theme_id)
			self.theme = json.dumps(t)
			self.save()
			return True
		self.theme = json.dumps(t)
		self.save()
		return False
	def remove_theme(self, theme_id):
		t = self.get_theme()
		if theme_id in t:
			t.remove(theme_id)
			self.theme = json.dumps(t)
			self.save()
			return True
		self.theme = json.dumps(t)
		self.save()
		return False
	def update_start_date(self):
		self.start_date = datetime.now()
		self.save()
	def update_end_date(self):
		self.end_date = datetime.now()
		self.save()

	def set_end_date(self, date):
		self.end_date = date
		self.save()
		
	def set_introduction(self, introduction):
		self.introduction = introduction
		self.save()
	def set_supporters(self, supporters):
		if isinstance(supporters, str):
			self.supporters = supporters
		else:
			self.supporters = json.dumps(supporters)
		self.save()
	def append_supporters(self, supporter_id):
		s = self.get_supporters()
		if supporter_id not in s:
			s.append(supporter_id)
			self.supporters = json.dumps(s)
			self.save()
			return True
		self.supporters = json.dumps(s)
		self.save()
		return False
	def remove_supporters(self, supporter_id):
		s = self.get_supporters()
		if supporter_id in s:
			s.remove(supporter_id)
			self.supporters = json.dumps(s)
			self.save()
			return True
		self.supporters = json.dumps(s)
		self.save()
		return False
	def set_comments(self, comments):
		if isinstance(comments, str):
			self.comments = comments
		else:
			self.comments = json.dumps(comments)
		self.save()
	def append_comments(self, comment_id):
		s = self.get_comments()
		if comment_id not in s:
			s.append(comment_id)
			self.comments = json.dumps(s)
			self.save()
			return True
		self.comments = json.dumps(s)
		self.save()
		return False
	def remove_comments(self, comment_id):
		s = self.get_comments()
		if comment_id in s:
			s.remove(comment_id)
			self.comments = json.dumps(s)
			self.save()
			return True
		self.comments = json.dumps(s)
		self.save()
		return False
	def get_theme_content(self):
		results = []
		for item in self.get_theme():
			results.append(Theme.objects.get(id = item).content)
		return ','.join(results)

	def __str__(self):
		return self.get_name()

class Interest(models.Model):
	content = models.CharField(max_length = 20, default = '')
	linked_theme = models.CharField(max_length = 500, default = '[]')
	#get attribute
	def get_content(self):
		return self.content
	def get_linked_theme(self):
		if isinstance(self.linked_theme, str):
			return json.loads(self.linked_theme)
		return self.linked_theme
	#set
	def set_linked_theme(self, linked_theme):
		if isinstance(linked_theme, str):
			self.linked_theme = linked_theme
		else:
			self.linked_theme = json.dumps(linked_theme)
		self.save()
	def append_linked_theme(self, linked_theme_id):
		s = self.get_linked_theme()
		if linked_theme_id not in s:
			s.append(linked_theme_id)
			self.linked_theme = json.dumps(s)
			self.save()
			return True
		self.linked_theme = json.dumps(s)
		self.save()
		return False
	def remove_linked_theme(self, linked_theme_id):
		s = self.get_linked_theme()
		if linked_theme_id in s:
			s.append(linked_theme_id)
			self.linked_theme = json.dumps(s)
			self.save()
			return True
		self.linked_theme = json.dumps(s)
		self.save()
		return False
	def set_content(self, content):
		self.content = content
		self.save()
	def __str__(self):
		return self.content

class Theme(models.Model):
	content = models.CharField(max_length = 100, default = '')
	#get attribute
	def get_content(self):
		return self.content
	#set
	def set_content(self, content):
		self.content = content
		self.save()
	def __str__(self):
		return self.content

class Comment(models.Model):
	comment_time = models.DateTimeField(default = datetime.now)
	commenter = models.IntegerField()
	score = models.IntegerField()
	content = models.CharField(max_length = 300, default = '')
	#get attribute
	def get_content(self):
		return self.content
	def get_id(self):
		return self.id
	def get_commenter(self):
		return self.commenter
	def get_commenter_name(self):
		return MyUser.objects.get(id = self.commenter).get_nickname()
	def get_score(self):
		return self.score
	def get_comment_time(self):
		return self.comment_time
	#set
	def set_content(self, content):
		self.content = content
		self.save()
	def set_score(self, score):
		self.score = score
		self.save()
	def set_commenter(self, commenter):
		self.commenter = commenter
		self.save()
	def __str__(self):
		return self.content
class Img(models.Model):
	img = models.ImageField(upload_to = 'upload')
	def get_id(self):
		return self.id
	def get_img(self):
		return self.img
