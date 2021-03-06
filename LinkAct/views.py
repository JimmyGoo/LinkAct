#搜索部分网址格式http://192.168.55.33:8000/search/?search_class=nickname&search_content=u&search_page=1
#   search_class表示搜索类别，search_content表示搜索内容,search_content表示搜索的页码号，要在template中动态生成
#


from .models import MyUser,Activity,Theme,User
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import AnonymousUser
from django.core.mail import send_mail
from .forms import RegisterForm
from .forms import LogForm
from .forms import PersonalInfoForm
from .forms import SetPasswordForm
from .forms import CommentForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from LinkAct.models import Img, Interest
import string
from datetime import date, datetime
from .forms import ActForm
from django.utils import timezone

base_url = 'http://127.0.0.1:8000'



#   search_class表示搜索类别，search_content表示搜索内容,search_content表示搜索的页码号，要在template中动态生成
#
#ERROR_INDEX
#
#用户注册
#0 -----  输入正确
#1 -----  两次输入密码不一致
#2 -----  用户名已存在
#3 -----  信息不完整
#4 -----  密码错误
#5 -----  用户不存在

#修改密码
#6 -----  修改密码成功
#7 -----  两次输入密码不一致
#8 -----  原密码错误

#修改个人信息
#9 -----  修改信息成功

#用户登录
#10 ----- 用户登录成功
#11 ----- 不存在该用户
#12 ----- 用户密码不匹配

#-1 ----  未知错误

# user attr #
# user basic attr:
# username
# password
# email

# extension:MyUser
# nickname
# birthday
# friends
# city
# head
# participate_terminative_acts
# create_terminative_acts
# participate_ongoing_acts
# create_ongoing_acts
# commented_acts
# gender
# interests



#
#搜索部分网址格式http://192.168.55.33:8000/search/?search_class=nickname&search_content=u&search_page=1
#   search_class表示搜索类别，search_content表示搜索内容,search_content表示搜索的页码号，要在template中动态生成
#
#
#def install(request):
#    '''服务安装'''
#    iplist = IP.objects.all()
#    server_list = AddServer.objects.all()
#	mserver_list = MServer.objects.all()
#    if request.method == "POST":
#        if request.POST.has_key('install'):    #这里判断，如果是name值为install的，则执行此段代码
#           ……代码段省略……
#        else:   #这里判断，如果不是name值为install的，则执行此段代码，因为我们就只有2个name，所以就不用elif request.POST.has_key('server'):了

# Create your views here.
#导航栏
#页面按钮绑定
# def user_manage(request):
#     if request.method == 'POST':
#         if request.POST.get('submit') == "register":
#             return HttpResponseRedirect('register/')
#         elif request.POST.get('submit') == "login":
#             return HttpResponseRedirect('login/')
#         elif request.POST.get('submit') == 'check':
#             return HttpResponseRedirect('check/')
#         else:
#             form = LogForm()
#             return render(request, 'LinkAct/login.html', {'form':form})
	
#     return render(request, 'LinkAct/user_manage.html', {})

#搜索对#
search_value_string = [
	{"value":"nickname", "string":"按照昵称搜索"},
	{"value":"all","string":"无筛选条件"},
	{"value":"username","string":"按照用户搜索"},
	{"value":"city","string":"按照城市搜索"},
	{"value":"theme", "string":"按照主题搜索"},
	{"value":"status","string":"按照状态搜索"},
	{"value":"name","string":"按照名字搜索"},
	{"value":"creator","string":"按照创建者搜索"},
	{"value":"locale","string":"按照地点搜索"},
	{"value":"introduction","string":"按照介绍搜索"},
]


def start_page_show(request):
	#-----------登录判定----------#
	has_login = False
	
	user = request.user
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')

	if request.user.username == AnonymousUser.username:
		has_login = False
		return render(request, 'LinkAct/start_page.html',
		{'user_name':user.username, 'has_login':has_login})
	else:
		has_login = True
		imgs = Img.objects.filter(id = user.myuser.get_head())
		if len(imgs) != 0:
			img = imgs[0]
			return render(request, 'LinkAct/start_page.html',
			{'user_name':user.username, 'has_login':has_login, 'img': img, 'has_own_avatar':True})
		else:
			return render(request, 'LinkAct/start_page.html',
			{'user_name':user.username, 'has_login':has_login, 'has_own_avatar':False})
	#-----------登录判定----------#


	

def linker_page_show(request):
	#-----------登录判定----------#
	has_login = False

	user = request.user
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')

	if request.user.username == AnonymousUser.username:
		has_login = False
		return render(request, 'LinkAct/linker_page.html',
		{'user_name':user.username, 'has_login':has_login})
	else:
		has_login = True
		imgs = Img.objects.filter(id = user.myuser.get_head())
		if len(imgs) != 0:
			img = imgs[0]
			return render(request, 'LinkAct/linker_page.html',
			{'user_name':user.username, 'has_login':has_login, 'img': img, 'has_own_avatar':True})
		else:
			return render(request, 'LinkAct/linker_page.html',
			{'user_name':user.username, 'has_login':has_login, 'has_own_avatar':False})
	#-----------登录判定----------#

	

def explore_page_show(request):
	#-----------登录判定----------#
	has_login = True
	has_own_avatar = False
	head_img = ''
	username = ''
	user = request.user
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')
	if request.user.username == AnonymousUser.username:
		has_login = False
		return HttpResponseRedirect('../login/')

	else:
		username = request.user.username
		has_login = True
		head_imgs = Img.objects.filter(id = user.myuser.get_head())
		if len(head_imgs) != 0:
			head_img = head_imgs[0]
			has_own_avatar = True
	#-----------------------------#

	if request.method == 'GET':
		check_activity_status(Activity.objects.all())
		act_answer = user.myuser.get_recommended_activities()
		user_answer = user.myuser.get_recommended_user()
		act_result = act_answer[0:20]
		user_result = user_answer[0:5]
		act_result = check_activity_status(act_result)

		#整合用户#
		user_data = []
	
		for show_user in user_result:
			other_can_friends = '0'
			if show_user[0].get_id() in user.myuser.get_friends():
				other_can_friends = '2'
			if user.myuser.get_id() in show_user[0].get_waiting():
				other_can_friends = '1'
			other_has_own_avatar = False
			other_imgs = Img.objects.filter(id = show_user[0].get_head())
			if len(other_imgs) != 0:
				other_img = other_imgs[0]
				other_has_own_avatar = True
			else:
				
				other_img = ''

			other_interests_num = show_user[0].get_interests()
			print(other_interests_num)
			other_interests = []
			has_interest = True
			if other_interests_num != []:
				for num in other_interests_num:
					print(num)
					other_interests.append(Interest.objects.get(id = int(num)).get_content())
			if other_interests == []:
				has_interest = False
			p_act_number = len(show_user[0].get_participate_terminative_acts())	+ len(show_user[0].get_participate_ongoing_acts())
			c_act_number = len(show_user[0].get_create_ongoing_acts()) + len(show_user[0].get_create_terminative_acts())
			user_data.append({'c_act_number':c_act_number, 'p_act_number':p_act_number, 'friends_number':len(show_user[0].get_friends()), 'same_acts_number':show_user[3], 'same_interests_number':show_user[2], 'same_friends':show_user[1], 'other_user':show_user[0], 'other_img':other_img, 'other_has_own_avartar':other_has_own_avatar,
				'other_interests':other_interests, 'other_can_friends': other_can_friends, 'has_interest':has_interest})
		pass_data = []
		for i in act_result:
			img = Img.objects.filter(id = i.act_image)
			has_show_img = False
			pass_image = ''
			if len(img) > 0:
				pass_image = img[0]
				has_show_img = True
			pass_data.append({'act':i,'pass_img':pass_image, 'has_show_img':has_show_img})
			

	
		if has_own_avatar:
			return render(request, 'LinkAct/explore_page.html', 
			{
				'user_name':username,
				'img':head_img,
				'pass_data':pass_data, 
			 	'no_param_path':request.path, 
			 	'user_data':user_data,
			 	'has_login':has_login,
			 	'has_own_avatar':has_own_avatar,
			 	'current_url':request.get_full_path(),
		 	})
		else:
		 	return render(request, 'LinkAct/explore_page.html', 
			{
				'user_name':username,
				'pass_data':pass_data, 
			 	'no_param_path':request.path, 
			 	'user_data':user_data,
			 	'has_login':has_login,
			 	'has_own_avatar':has_own_avatar,
			 	'current_url':request.get_full_path(),
		 	})
	elif request.method == 'POST':
		params = request.POST
		if request.POST.get('submit') == 'search_submit':
			aim_url = request.path
			aim_url = aim_url + "?search_class=" + params.get('search_class', '') + "&search_content=" + params.get('search_content', '') + "&search_order=0&search_page=1" 
			return HttpResponseRedirect(aim_url)
		elif request.POST.get('submit') == '加为好友':
			index = request.POST.get('person_id')
			User.objects.filter(id=index)[0].myuser.append_waiting(request.user.id)
			return HttpResponseRedirect(request.get_full_path())

	

def share_page_show(request):
	#-----------登录判定----------#
	has_login = False
	user = request.user
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')

	if request.user.username == AnonymousUser.username:
		has_login = False
		return render(request, 'LinkAct/share_page.html',
		{'user_name':user.username, 'has_login':has_login})
	else:
		has_login = True
		imgs = Img.objects.filter(id = user.myuser.get_head())
		if len(imgs) != 0:
			img = imgs[0]
			return render(request, 'LinkAct/share_page.html',
			{'user_name':user.username, 'has_login':has_login, 'img': img, 'has_own_avatar':True})
		else:
			return render(request, 'LinkAct/share_page.html',
			{'user_name':user.username, 'has_login':has_login, 'has_own_avatar':False})
	#-----------登录判定----------#

	

def activities_page_show(request):
	#-----------登录判定----------#
	has_login = False
	user = request.user
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')

	if request.user.username == AnonymousUser.username:
		has_login = False
		return render(request, 'LinkAct/activities_page.html',
		{'user_name':user.username, 'has_login':has_login})
	else:
		has_login = True
		imgs = Img.objects.filter(id = user.myuser.get_head())
		if len(imgs) != 0:
			img = imgs[0]
			return render(request, 'LinkAct/activities_page.html',
			{'user_name':user.username, 'has_login':has_login, 'img': img, 'has_own_avatar':True})
		else:
			return render(request, 'LinkAct/activities_page.html',
			{'user_name':user.username, 'has_login':has_login, 'has_own_avatar':False})
	#-----------登录判定----------#

	

#用户注册
def user_register(request):

	form = RegisterForm()

	if request.method == "POST":
		params = request.POST
		usernames = params.get('username', '')
		password1 = params.get('password1', '')
		password2 = params.get('password2', '')
		nickname = params.get('nickname','')
		email = params.get('email', '')
		#一系列合法性判定
		
		if usernames == None or password1 == None or password2 == None or email == None:
			#信息不完整
			print('incomplete info')
			return render(request, 'LinkAct/result_page.html', {'error_index':3})
		if password1 != password2:
			print('password1 is not equal to password2')
			return render(request, 'LinkAct/result_page.html', {'error_index':1})
		if len(User.objects.filter(username=usernames)):
			#用户名已存在
			print('username already exists')
			return render(request, 'LinkAct/result_page.html', {'error_index':2})

		print(type(password1))
		url = "请进入下列链接完成邮箱验证：" + "http://"+request.get_host() + '/confirm/?username=' + usernames + '&nickname=' + nickname + '&password=' + str(password1) + '&email='+  str(email)
		print(url)
		send_mail("加入领客验证", url, 'LinkActs@163.com', [email], fail_silently=False)
		#判定完毕
		# myUser = MyUser()
		# myUser.create_user(usernames, password1, email ,nickname)
		# user = auth.authenticate(username=usernames, password=password1)
		# auth.login(request,user)
		return render(request, 'LinkAct/result_page.html', {'error_index':0})
 
	return render(request, 'LinkAct/register_page.html', {'form':form})
		

def confirm(request):
	if request.method == 'GET':
		params = request.GET
		username = params.get('username','')
		nickname = params.get('nickname','')
		password = params.get('password','')
		email = params.get('email','')
		myUser = MyUser()
		myUser.create_user(username, password, email ,nickname)
		user = auth.authenticate(username=username, password=password)
		auth.login(request,user)
		return render(request, 'LinkAct/confirm_page.html')

#创建完成
def create_act(request):

	#-----------登录判定----------#
	has_login = True
	user = request.user
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')

	#-----------------------------#
	imgs = Img.objects.filter(id = user.myuser.get_head())
	img = ''
	if len(imgs) != 0:
		img = imgs[0]
		has_own_avatar = True
	else:
		has_own_avatar = False
		img = ''
	#-----------------------------#

	#应该修改这里#
	if request.user.username == AnonymousUser.username:
		has_login = False
	else:
		has_login = True
	#-----------登录判定----------#
	#在全局绑定函数中判断按下了哪个按钮，此处需知道当前用户名，默认活动form为ActForm


	check_theme_msg = []
	for x in Theme.objects.all():
		t = (x.id, x.get_content())
		check_theme_msg.append(t)


	if request.method == 'POST':

		params = request.POST
		temp = params.getlist('theme', '')
		theme = [int(var) for var in temp]
		print('fuck')
		print(theme)
		name = params.get('name', '')
		start_date = params.get('start_date', '')
		end_date = params.get('end_date', '')

		city_string = params.get('province', '')
		city_string += ' '
		city_string += params.get('city','')

		introduction = ''
		act_img_id = -1
		introduction = params.get('intro', '')

		if request.FILES.get('act_img_upload'):
			act_img = Img(img = request.FILES.get('act_img_upload'))
			act_img.save()
			act_img_id = act_img.id
				
		request.user.myuser.create_activity(name, theme, city_string, start_date, end_date, introduction, act_img_id)
		 
		return HttpResponseRedirect('../?search_class=create_time&search_content=&search_order=1&search_page=1')
	else:

		if request.user.myuser.city != '':
			default_province = request.user.myuser.city.split(' ');
			default_city = default_province[1]
			default_province = default_province[0]
		else:
			default_city = "未填写"
			default_province = "未填写"

		form = ActForm()
		return render(request, 'LinkAct/create_act.html', 
			{
				'form': form, 
				'has_login':has_login, 'has_own_avatar':has_own_avatar,
				'user_name':user.username, 
				"img":img,
				'default_province':default_province,
				'default_city':default_city,
				'theme_type':check_theme_msg,
			})

#修改活动信息
def check_act_msg(request):

	user = request.user
	user_name = ''
	has_login = False
	has_own_avatar = False
	if request.user.username == AnonymousUser.username:
		has_login = False
	else:
		user_name = user.username
		has_login = True
		imgs = Img.objects.filter(id = user.myuser.get_head())
		if len(imgs) != 0:
			img = imgs[0]
			has_own_avatar = True

	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')

		index = request.GET['id']
		

		if request.GET.get('search_order','') == '':
			back_page = request.GET['back_page'] + "&last_page=" + request.GET['last_page']
		else:
			back_page = request.GET['back_page'] + "&last_page=" + request.GET['last_page'] + "&search_content="+ str(request.GET['search_content']) + "&search_order=" + str(request.GET['search_order']) + "&search_page=" + str(request.GET['search_page'])

		act = Activity.objects.get(id=index)
		act_infomation = {}
		act_infomation['act'] = act
		act_infomation['creator'] = User.objects.get(id = act.get_creator()).myuser
		temp_p_id = act.get_participants()
		temp_p_myuser = []
		for x in temp_p_id:
			temp_p_myuser.append(User.objects.get(id = x).myuser)
		act_infomation['participants'] = temp_p_myuser
		temp_theme_id = act.get_theme()
		temp_theme = []
		for x in temp_theme_id:
			temp_theme.append(Theme.objects.get(id = x))
		act_infomation['theme'] = temp_theme
		temp_p_id = act.get_supporters()
		temp_p_myuser = []
		for x in temp_p_id:
			temp_p_myuser.append(User.objects.get(id = x).myuser)
		act_infomation['supporters'] = temp_p_myuser

		act_id = act_infomation['act'].id

		default_province = act.get_locale().split(' ')
		default_city = default_province[1]
		default_province = default_province[0]


		print(act_infomation['act'].start_date)

		if has_own_avatar:
			return render(request, 'LinkAct/check_act_msg.html', 
				{
					
					'act_infomation':act_infomation, 
					'back_page':back_page,
					'has_own_avatar':has_own_avatar,
					'img': img,
					'has_login': has_login,
					'user_name':user_name,
					'act_id':act_id,
					'default_province':default_province
				})
		else:
			return render(request, 'LinkAct/check_act_msg.html', 
				{
					
					'act_infomation':act_infomation, 
					'back_page':back_page,
					'has_own_avatar':has_own_avatar,
					'has_login': has_login,
					'user_name':user_name,
					'act_id':act_id,
					'default_province':default_province
				})
	elif request.method == 'POST':
		act_id = request.POST.get('act_id', '')
		c_act = Activity.objects.get(id=act_id)

		c_act.set_name(request.POST.get('name',''))

		city_string = request.POST.get('province', '')
		city_string += ' '
		city_string += request.POST.get('city','')

		c_act.set_locale(city_string)
		c_act.set_introduction(request.POST.get('intro',''))
		c_act.set_end_date(request.POST.get('end_date',''))

		if request.FILES.get('act_img_upload') != '':
			print("我在寒风中", request.FILES.get('act_img_upload'))
			new_img = Img(img = request.FILES.get('act_img_upload'))
			new_img.save()
			c_act.set_act_image(new_img.get_id())
		


		mails_to = []	
		participants = c_act.get_participants()
		



		for index in range(0, len(participants)):
			mails_to.append(User.objects.get(id=participants[index]).email)

		info_msg = "您参加的活动" + c_act.name + "的信息被修改，请及时查看。"

		send_mail("活动信息修改通知", info_msg, 'LinkActs@163.com', mails_to, fail_silently=False)
		print(mails_to)
				#保存修改并发送邮件
		back_page = request.POST.get('back_page')
		return HttpResponseRedirect(back_page)
#登录
def log_in(request):

	if request.method == "POST":
		#根据用户名找到对应用户信息及信息网页
		log_username = request.POST['username']

		log_password = request.POST['password']

		user = auth.authenticate(username=log_username, password=log_password)
		
		if len(User.objects.filter(username=log_username)) == 0:
			return render(request, 'LinkAct/result_page.html', {'error_index':11})
 
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('../')
 
		else:
			return render(request, 'LinkAct/result_page.html', {'error_index':12})
 
		
	form = LogForm()
	return render(request, 'LinkAct/login_page.html', {'form':form})

#登出
def log_out(request):
	auth.logout(request)

#查看个人信息--可以通过使用request.user.myuser.nickname获取附加信息
def check_personal_msg(request):
	
	info_change_status = False
	check_history_status = False
	has_login = True
	user_name = request.user.username
	#-----------登录判定----------#
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')
	#-----------登录判定----------#
		set_info = request.GET.get('info_change','-1')
		if set_info=='1':
			info_change_status = True

		check_his = request.GET.get('check_history','-1')
		if check_his=='1':
			check_history_status = True


	check_interest_msg = []
	for x in Interest.objects.all():
		if x.id in request.user.myuser.get_interests():
			t = (x.id, x.get_content(), 1)
		else:
			t = (x.id, x.get_content(), 0)
		check_interest_msg.append(t)

	#修改个人信息
	if request.method == 'POST':

		if request.POST.get('change_info') == 'change':
			
			params = request.POST
			obj = User.objects.get(username=request.user.username)
			
			obj.myuser.set_nickname(params.get('nickname', ''))
			obj.myuser.set_birthday(params.get('birthday', '1970-01-01'))
			obj.myuser.set_city(params.get('city', ''))
			obj.myuser.set_gender(params.get('gender', ''))
			obj.myuser.set_phonenumber(params.get('phone_number', ''))

			city_string = ''
			if params.get('province','') != '未填写':
				city_string += params.get('province', '')
				city_string += ' '
				city_string += params.get('city','')

			obj.myuser.set_city(city_string)

			temp_list = params.getlist('interests', '')
			obj.myuser.set_interests([])
			for x in temp_list:
				obj.myuser.append_interests(int(x))
			

			imgs = Img.objects.filter(id = obj.myuser.get_head())
			if len(imgs) != 0:
				img = imgs[0]
				return render(request, 'LinkAct/result_page.html', {'error_index':9})
			else:
				return render(request, 'LinkAct/result_page.html', {'error_index':9})

		
		if request.POST.get('img_upload_btn') == 'upload':
			
			new_img = Img(img = request.FILES.get('img_upload'))
			new_img.save()
			request.user.myuser.set_head(new_img.get_id())
			return HttpResponseRedirect('.')

	#查看个人信息
	else :       
		imgs = Img.objects.filter(id = request.user.myuser.get_head())

		has_own_avatar = False

		if len(imgs) != 0:
			img = imgs[0]
			has_own_avatar = True

		temp = request.user.myuser.get_interests()
		interest_msg = ""
		for s in temp:
			if len(interest_msg) != 0:
				interest_msg += '、'
			interest_msg += Interest.objects.get(id = int(s)).get_content()
		
		if interest_msg == "":
			interest_msg = "未填写"	

		if request.user.myuser.city != '':
			default_province = request.user.myuser.city.split(' ');
			default_city = default_province[1]
			default_province = default_province[0]
		else:
			default_city = "未填写"
			default_province = "未填写"

		history_p_event_id = []
		history_c_event_id = []
		history_p_event = []
		history_c_event = []
		if check_history_status:
			print('wocaonimawocaim')

			history_p_event_id = request.user.myuser.get_participate_terminative_acts()
			for i in request.user.myuser.get_participate_ongoing_acts():
				history_p_event_id.append(i)
			history_c_event_id = request.user.myuser.get_create_terminative_acts()
			for i in request.user.myuser.get_create_ongoing_acts():
				history_c_event_id.append(i)

			for i in history_p_event_id:
				history_p_event.append(Activity.objects.get(id=i).get_name())
			for i in history_c_event_id:
				history_c_event.append(Activity.objects.get(id=i).get_name())
			print(history_p_event)
			print(history_c_event)





		if has_own_avatar:
			print(request.user.myuser.nickname)
			return render(request, 'LinkAct/user_info.html', 
					{
						'check_interest_msg': check_interest_msg,
						'has_login':True, 
						'personal_msg':request.user, 
						'interest_msg':interest_msg, 
						'img': img, 
						'has_own_avatar':has_own_avatar,
						'info_change_status':info_change_status,

						'check_history_status':check_history_status,
						'history_c_event':history_c_event,
						'history_p_event':history_p_event,

						'default_province':default_province,
						'default_city':default_city,
						'user_name':user_name,

					})
		else:
			print(request.user.myuser.nickname)
			return render(request, 'LinkAct/user_info.html', 
					{
						'check_interest_msg': check_interest_msg,
						'has_login':True,
						'personal_msg':request.user, 
						'interest_msg':interest_msg, 
						'has_own_avatar':has_own_avatar,
						'info_change_status':info_change_status,
						'default_province':default_province,
						'default_city':default_city,
						'user_name':user_name,

						'check_history_status':check_history_status,
						'history_c_event':history_c_event,
						'history_p_event':history_p_event,
					})

def set_password_func(request):

	#-----------登录判定----------#
	has_login = True
	user = request.user
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')

	#-----------------------------#
	imgs = Img.objects.filter(id = user.myuser.get_head())
	if len(imgs) != 0:
		img = imgs[0]
		has_own_avatar = True
	else:
		has_own_avatar = False
	#-----------------------------#

	#应该修改这里#
	if request.user.username == AnonymousUser.username:
		has_login = False
	else:
		has_login = True
	#-----------登录判定----------#

	form = SetPasswordForm()

	if request.method == 'POST':
		params = request.POST
		obj = User.objects.get(username=request.user.username)
		origin_password = params.get('origin_password','')
		new_password1 = params.get('new_password1','')
		new_password2 = params.get('new_password2','')
		if auth.authenticate(username=request.user.username, password=origin_password) == None:
			return render(request, 'LinkAct/result_page.html',{'error_index':8, 'img': img})
		if new_password1 != new_password2:
			return render(request, 'LinkAct/result_page.html',{'error_index':7, 'img': img})

		obj.myuser.set_password(new_password1)
		log_out(request)

		return render(request, 'LinkAct/result_page.html', {'error_index':6, 'has_login':False})
	else:
		if has_own_avatar:
			return render(request, 'LinkAct/user_password.html', {'form':form, 'has_login':True, 
			'user_name':request.user.username, 'img':img, 'has_own_avatar': has_own_avatar})
		else:
			return render(request, 'LinkAct/user_password.html', {'form':form, 'has_login':True, 
			'user_name':request.user.username, 'has_own_avatar': has_own_avatar})

#评价活动——需要评价Form，先定义为CommentForm

#完成评价
def evaluate_act(request):
	if request.method == 'POST':
		params = request.POST
		newComment = Comment()
		newComment.commenter = request.user.id
		newComment.score = params['score']
		newComment.content = params['content']
		newComment.save()

		itemID = request.POST['itemID']
		#活动评论列表append这条新评论
		
		return #跳转评论成功
	elif request.method == 'GET':
		params = request.GET
		itemID = params['id']
		return render(request, '任务信息界面', {'itemID':itemID})
		
def show_people(request):
	#-----------登录判定----------#
	has_login = True
	user = request.user
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')
	if request.user.username == AnonymousUser.username:
		has_login = False
	else:
		has_login = True
	#-----------------------------#

	if request.method == 'GET':
	
		index = int(request.GET['id'])
		current_page = ''
		if request.GET.get('back_page', '') != '':
			current_page = request.GET['back_page'] +"&last_page=" +request.GET['last_page'] + "&search_content=" + str(request.GET['search_content']) + "&search_order=" + str(request.GET['search_order']) + "&search_page=" + str(request.GET['search_page'])
		else:
			if request.GET.get('search_order', '') == '':
				current_page = request.GET['last_page']
			else:
				current_page = request.GET['last_page'] + "&search_content=" + str(request.GET['search_content']) + "&search_order=" + str(request.GET['search_order']) + "&search_page=" + str(request.GET['search_page'])
		
	
		personal_msg = User.objects.filter(id=index)[0]

		temp = personal_msg.myuser.get_interests()

		my_url = request.path

		interest_msg = ""
		for s in temp:
			if len(interest_msg) != 0:
				interest_msg += '，'
			interest_msg += Interest.objects.get(id = int(s)).get_content()
		if interest_msg == "":
			interest_msg = "未填写"	


		if has_login:
			imgs = Img.objects.filter(id = request.user.myuser.get_head())
			form = PersonalInfoForm()
			


			other_can_friends = '0'
			if personal_msg.myuser.get_id() in request.user.myuser.get_friends():
				other_can_friends = '2'
			if request.user.myuser.get_id() in personal_msg.myuser.get_waiting():
				other_can_friends = '1'


			if len(imgs) != 0:
				img = imgs[0]
				if personal_msg.myuser.get_head() != -1:
					other_flag = True
					other_img = Img.objects.get(id = personal_msg.myuser.get_head())
					return render(request, 'LinkAct/personal_info.html', 
						{
							'other_img': other_img, 
							'other_flag': other_flag, 
							'has_login': has_login, 
							'img': img, 
							'has_own_avatar':True, 
							'form':form, 
							'interest_msg': interest_msg, 
							'personal_msg':personal_msg, 
							'last_page':current_page,
							'my_url':my_url,
							'other_can_friends':other_can_friends,
							'user_name':request.user.username,
						})
				else:
					other_flag = False
					return render(request, 'LinkAct/personal_info.html', 
						{
							'other_flag': other_flag, 
							'has_login': has_login, 
							'img': img, 
							'has_own_avatar':True, 
							'form':form, 
							'interest_msg': interest_msg, 
							'personal_msg':personal_msg, 
							'last_page':current_page,
							'my_url':my_url,
							'other_can_friends':other_can_friends,
							'user_name':request.user.username,
						})
			else:
				if personal_msg.myuser.get_head() != -1:
					other_flag = True
					other_img = Img.objects.get(id = personal_msg.myuser.get_head())
					return render(request, 'LinkAct/personal_info.html', 
						{
							'other_img': other_img, 
							'other_flag': other_flag, 
							'has_login': has_login, 
							'has_own_avatar':False, 
							'form':form, 
							'interest_msg': interest_msg, 
							'personal_msg':personal_msg, 
							'last_page':current_page,
							'my_url':my_url,
							'other_can_friends':other_can_friends,
							'user_name':request.user.username,
						})
				else:
					other_flag = False
					return render(request, 'LinkAct/personal_info.html', 
						{
							'other_flag': other_flag, 
							'has_login': has_login, 
							'has_own_avatar':False, 
							'form':form, 
							'interest_msg': interest_msg, 
							'personal_msg':personal_msg, 
							'last_page':current_page,
							'my_url':my_url,
							'other_can_friends':other_can_friends,
							'user_name':request.user.username,
						})
		else:
			return render(request, 'LinkAct/personal_info.html', 
					{
						'has_login': has_login, 
						'form':form, 
						'interest_msg': interest_msg, 
						'personal_msg':personal_msg, 
						'last_page':current_page, 
						'my_url':my_url,
						
					})

	else:
		if request.POST.get('submit') == "request_friend":
			index = request.POST.get('person_id')
			User.objects.filter(id=index)[0].myuser.append_waiting(request.user.id)
		return HttpResponseRedirect(request.get_full_path())

def search_people(request):
	#-----------登录判定----------#
	has_login = True
	user = request.user
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')
	if request.user.username == AnonymousUser.username:
		has_login = False
	else:
		has_login = True
	#-----------------------------#
	if has_login:
		imgs = Img.objects.filter(id = user.myuser.get_head())
		if len(imgs) != 0:
			img = imgs[0]
			has_own_avatar = True
		else:
			has_own_avatar = False

		user_name = user.myuser.get_username()
		if request.method == 'GET':                                  
			search_class = request.GET['search_class']
			search_content = request.GET['search_content']                                  
			search_page = request.GET['search_page']
			search_order = request.GET['search_order']

			answer = []


			if search_order == '1':
				answer = MyUser.objects.all().order_by('-id')

			else:
				print('fuck')
				print(search_class)
				answer = user.myuser.user_filter(search_class, search_content)
				print('在这', answer)

			answer = list(answer)
			for i in range(len(answer)):
				if answer[i].user.username == request.user.username:
					del answer[i]
					break


			is_last_page = False
			is_first_page = False
			
			startPos = (int(search_page) - 1) * 10
			endPos = int(search_page) * 10
			if endPos >= len(answer):
				endPos = len(answer)
				is_last_page = True

			if startPos == 0:
				is_first_page = True

			result = answer[startPos:endPos]

			temp_url = request.get_full_path()

			next_page = int(search_page) + 1
			front_page = next_page - 2

			next_page_url = request.path + "?search_class=" + search_class + "&search_content=" + search_content + "&search_order=" + search_order + "&search_page=" + str(next_page)
			front_page_url = request.path + "?search_class=" + search_class + "&search_content=" + search_content + "&search_order=" + search_order + "&search_page=" + str(front_page)
			first_page_url = request.path + "?search_class=" + search_class + "&search_content=" + search_content + "&search_order=" + search_order + "&search_page=1"

			#整合用户#
			pass_data = []
		
			for show_user in result:
				other_can_friends = '0'
				if show_user.get_id() in user.myuser.get_friends():
					other_can_friends = '2'
				print('这个', user.myuser.get_id(), show_user.get_waiting())
				if user.myuser.get_id() in show_user.get_waiting():
					other_can_friends = '1'
				other_has_own_avatar = False
				other_imgs = Img.objects.filter(id = show_user.get_head())
				if len(other_imgs) != 0:
					other_img = other_imgs[0]
					other_has_own_avatar = True
				else:
					
					other_img = ''

				other_interests_num = show_user.get_interests()
				
				other_interests = []
				has_interest = True
				if other_interests_num != []:
					for num in other_interests_num:
						other_interests.append(Interest.objects.get(id = int(num)).get_content())
				if other_interests == []:
					has_interest = False

				p_act_number = len(show_user.get_participate_terminative_acts())+ len(show_user.get_participate_ongoing_acts())
				c_act_number = len(show_user.get_create_ongoing_acts()) + len(show_user.get_create_terminative_acts())

				pass_data.append({
					'other_user':show_user, 
					'other_img':other_img, 
					'other_has_own_avartar':other_has_own_avatar,
					'other_interests':other_interests, 
					'other_can_friends': other_can_friends, 
					'has_interest':has_interest,
					'p_act_number':p_act_number,
					'c_act_number':c_act_number,
					'friends_num':len(show_user.get_friends()),
					})

			search_class_pass_text = '无条件筛选'
			search_class_pass_value = 'all'
			for i in search_value_string:
				if i['value'] == search_class:
					search_class_pass_text = i['string']
					search_class_pass_value = i['value']
					print(search_class_pass_value)
					print(search_class_pass_text)
					break;

			waiting_id = request.user.myuser.get_waiting()
			waiting_link = []

			c_path = request.get_full_path()

			for index in range(0, len(waiting_id)):
				aim = request.path + "../personal_info/?id=" + str(waiting_id[index]) + "&last_page=" + c_path
				waiting_link.append(aim)


			requests = []
			for i in range(0, len(waiting_id)):
				requests.append((waiting_id[i], waiting_link[i], User.objects.get(id=waiting_id[i]).myuser.nickname))

			if has_own_avatar:
				return render(request, 'LinkAct/linker_page.html', 
						{
							'img': img,
							'has_own_avatar': has_own_avatar,
							'has_login': has_login, 
							'pass_data':pass_data,
							'current_page':int(search_page), 
							'current_url':temp_url, 
							'next_page_url':next_page_url,
							'front_page_url':front_page_url,
							'first_page_url':first_page_url, 
							'requests':requests,
							'user_name': user_name,
							'search_class_pass_value':search_class_pass_value,
							'search_class_pass_text':search_class_pass_text,
							'search_content_pass_text':search_content,
							'is_last_page':is_last_page,
							'is_first_page':is_first_page,
						})
			else:
				return render(request, 'LinkAct/linker_page.html', 
						{
							'has_own_avatar': has_own_avatar,
							'has_login': has_login, 
							'pass_data':pass_data,
							'current_page':int(search_page), 
							'current_url':temp_url, 
							'next_page_url':next_page_url,
							'front_page_url':front_page_url,
							'first_page_url':first_page_url,
							'requests':requests,
							'user_name': user_name,
							'search_class_pass_value':search_class_pass_value,
							'search_class_pass_text':search_class_pass_text,
							'search_content_pass_text':search_content,
							'is_last_page':is_last_page,
							'is_first_page':is_first_page,
						})   

		elif request.method == 'POST':
			params = request.POST

			if request.POST.get('submit') == 'search_submit':

				aim_url = request.path

				if params.get('search_order', '') == '':
					aim_url = aim_url + "?search_class=" + params.get('search_class', '') + "&search_content=" + params.get('search_content', '') + "&search_order=1&search_page=1" 
				else:
					aim_url = aim_url + "?search_class=" + params.get('search_class', '') + "&search_content=" + params.get('search_content', '') + "&search_order=0&search_page=1" 
				return HttpResponseRedirect(aim_url)

			elif request.POST.get('submit') == "加为好友":
				index = request.POST.get('person_id')
				User.objects.filter(id=index)[0].myuser.append_waiting(request.user.id)
				return HttpResponseRedirect(request.get_full_path())

			elif request.POST.get('submit') == "同意" or request.POST.get('submit') == "拒绝":
				agreed_id = int(request.POST.get('request_id'))
				if request.POST.get('submit') == '同意':				
					request.user.myuser.append_friends(agreed_id)
					User.objects.get(id = agreed_id).myuser.append_friends(request.user.id)
				request.user.myuser.del_waiting_friends(agreed_id)
				return HttpResponseRedirect(request.POST.get('old_url'))
	else:
		return HttpResponseRedirect('../login/')



								
#查找活动   //搜索页面不同于主页面 默认每页10条，所有展示活动的界面都绑定此函数
				#urls.py r'^searchActs/'    绝对路径为127.0.0.0.1/searchActs/      因而展示界面上的各详情链接为  <a href='../showActs/?id='+ {{ result[index].id }} + '&last_page=' + {{ current_url }}>
				#“下一页”按钮链接应为<a href={{ next_page_url }}>
def search_act(request):
	#-----------登录判定----------#
	has_login = True
	has_own_avatar = False
	head_img = ''
	username = ''
	user = request.user
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')
	if request.user.username == AnonymousUser.username:
		has_login = False
		return HttpResponseRedirect('../login/')


	else:
		username = request.user.username
		has_login = True
		head_imgs = Img.objects.filter(id = user.myuser.get_head())
		if len(head_imgs) != 0:
			head_img = head_imgs[0]
			has_own_avatar = True
	#-----------------------------#

	if request.method == 'GET':
		#搜索类别
		search_class = request.GET['search_class']
		#搜索内容
		search_content = request.GET['search_content'] 
		#搜索页码
		search_page = request.GET['search_page']
		#排序方法，为1时表示按照类别倒序排序，不搜索只排序
		search_order = request.GET['search_order']

		if search_class == 'status':
			check_activity_status(Activity.objects.all())


		answer = []

		if search_order == '1':
			answer = Activity.objects.all().order_by('-create_time')

		#不同检索方式
		else:
			answer = request.user.myuser.activity_filter(search_class, search_content)
		print("我在寒风里", search_class)
		is_last_page = False
		is_first_page = False

		startPos = (int(search_page) - 1) * 10
		endPos = int(search_page) * 10
		if endPos >= len(answer):
			endPos = len(answer)
			is_last_page = True

		if startPos == 0:
			is_first_page = True

		result = answer[startPos:endPos]
		result = check_activity_status(result)

		pass_data = []
		for i in result:
			img = Img.objects.filter(id = i.act_image)
			has_show_img = False
			pass_image = ''
			if len(img) > 0:
				pass_image = img[0]
				has_show_img = True
			pass_intro = i.introduction
			
			if len(i.introduction) > 10:
				pass_intro = i.introduction[0:10]
				pass_intro += ''
			print(pass_intro)

			pass_data.append({'act':i,'pass_img':pass_image, 'has_show_img':has_show_img, 'pass_intro':pass_intro})
			
		new_movement_ids = request.user.myuser.get_friend_movement_id()
		new_movements = request.user.myuser.get_friend_movement()
		new_names = request.user.myuser.get_movement_name()
		new_links = request.user.myuser.get_movement_link()
		new_person_names = []

		has_moment = True
		if len(new_movements) == 0:
			has_moment = False

		for index in range(0, len(new_movements)):
			# new_person_names.append(User.objects.get(int(new_movements[index])).myuser.nickname)
			new_person_names.append(User.objects.get(id=new_movement_ids[index]).myuser.nickname)

		new_data = []
		for i in range(0, len(new_movements)):
			new_data.append((new_movements[i], new_names[i], new_links[i], new_person_names[i]))
		
		
		next_page = int(search_page) + 1
		front_page = next_page - 2

		temp_url = request.get_full_path()
		next_page_url = request.path + "?search_class=" + search_class + "&search_content=" + search_content + "&search_order=" + search_order + "&search_page=" + str(next_page)
		
		front_page_url = request.path + "?search_class=" + search_class + "&search_content=" + search_content + "&search_order=" + search_order + "&search_page=" + str(front_page)
		first_page_url = request.path + "?search_class=" + search_class + "&search_content=" + search_content + "&search_order=" + search_order + "&search_page=1"


		search_class_pass_text = '按照主题搜索'
		search_class_pass_value = 'theme'
		for i in search_value_string:
			if i['value'] == search_class:
				search_class_pass_text = i['string']
				search_class_pass_value = i['value']
				print(search_class_pass_value)
				print(search_class_pass_text)
				break;

		if has_own_avatar:
			return render(request, 'LinkAct/activities_page.html', 
			{
				'user_name':username,
				'img':head_img,
				'pass_data':pass_data, 
				'current_page':int(search_page), 
				'current_url':request.get_full_path(), 
				'next_page_url':next_page_url,
				'front_page_url':front_page_url,
				'first_page_url':first_page_url,
				'is_first_page':is_first_page,
				'is_last_page':is_last_page,

			 	'no_param_path':request.path, 
			 	'new_data':new_data,
			 	'has_login':has_login,
			 	'has_own_avatar':has_own_avatar,
			 	'search_class_pass_text':search_class_pass_text,
			 	'search_class_pass_value':search_class_pass_value,
				'search_content_pass_text':search_content,

				'has_moment':has_moment,
		 	})
		else:
		 	return render(request, 'LinkAct/activities_page.html', 
			{
				'user_name':username,
				'pass_data':pass_data, 
				'current_page':int(search_page), 
				'current_url':request.get_full_path(), 
				'next_page_url':next_page_url,

				'front_page_url':front_page_url,
				'first_page_url':first_page_url,
				'is_first_page':is_first_page,
				'is_last_page':is_last_page,

			 	'no_param_path':request.path, 
			 	'new_data':new_data,
			 	'has_login':has_login,
			 	'has_own_avatar':has_own_avatar,
			 	'search_class_pass_text':search_class_pass_text,
			 	'search_class_pass_value':search_class_pass_value,
				'search_content_pass_text':search_content,
				'has_moment':has_moment,
		 	})
	elif request.method == 'POST':
		params = request.POST
		if request.POST.get('submit') == 'search_submit':
			aim_url = request.path
			aim_url = aim_url + "?search_class=" + params.get('search_class', '') + "&search_content=" + params.get('search_content', '') + "&search_order=0&search_page=1" 
			return HttpResponseRedirect(aim_url)
		elif request.POST.get('submit') == '全部忽略':
			request.user.myuser.clear_friend_movement()
			request.user.myuser.clear_movement_name()
			request.user.myuser.clear_movement_link()
			request.user.myuser.clear_friend_movement_id()
			return HttpResponseRedirect(request.get_full_path())

#展示具体活动的界面，返回按钮的链接应为<a href={{ last_page }}>， 若是创建者，则应存在链接“修改活动信息”，应为<a href=this_page_no_para + 'change/?id=' + act_obj.id + '&last_page=' + this_page>
def show_act(request):
	#-----------登录判定----------#
	has_login = True
	user = request.user
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')

	#-----------------------------#
	imgs = Img.objects.filter(id = user.myuser.get_head())
	img = ''
	if len(imgs) != 0:
		img = imgs[0]
		has_own_avatar = True
	else:
		has_own_avatar = False
		img = ''
	#-----------------------------#

	#应该修改这里#
	if request.user.username == AnonymousUser.username:
		has_login = False
	else:
		has_login = True

	#-----------------------------#

	if request.method == 'GET':
		index = int(request.GET['id'])
		if request.GET.get('search_order', '') == '':
			current_page = request.GET['last_page']
		else:
			current_page = request.GET['last_page'] + "&search_content=" + str(request.GET['search_content']) + "&search_order=" + str(request.GET['search_order']) + "&search_page=" + str(request.GET['search_page'])
		print(current_page)


		act_obj = Activity.objects.filter(id=index)[0]

		this_page = request.get_full_path()
		this_page_no_para = request.path

		check_activity_status([act_obj])

		actForm = ActForm()

		#是否活动发起人，决定了是否能修改活动信息
		isCreator = False
		if request.user.id == act_obj.creator:
			isCreator = True

		isParticipant = isCreator
		if request.user.id in act_obj.get_participants():
			isParticipant = True

		comments = act_obj.get_comments_content()
		comment_info = []
		j = len(comments) - 1
		while j >= 0:
			comment_info.append((comments[j].get_commenter_name(), comments[j].get_score(), comments[j].get_content(), comments[j].get_comment_time()))
			j -= 1
			
		print('mada', comment_info)
		newCommentForm = CommentForm()

		act_infomation = {}
		act_infomation['act'] = act_obj
		act_infomation['creator'] = User.objects.get(id = act_obj.get_creator()).myuser

		temp_p_id = act_obj.get_participants()
		temp_p_myuser = []
		for x in temp_p_id:
			temp_p_myuser.append(User.objects.get(id = x).myuser)
		act_infomation['participants'] = temp_p_myuser


		temp_theme_id = act_obj.get_theme()
		temp_theme = []
		for x in temp_theme_id:
			temp_theme.append(Theme.objects.get(id = x))
		act_infomation['theme'] = temp_theme
		temp_p_id = act_obj.get_supporters()
		temp_p_myuser = []
		for x in temp_p_id:
			temp_p_myuser.append(User.objects.get(id = x).myuser)
		act_infomation['supporters'] = temp_p_myuser


		creator_interests_num = act_infomation['creator'].get_interests()
	
		creator_interests = []
		creator_has_interests = True
		if creator_interests_num != []:
			for num in creator_interests_num:
				creator_interests.append(Interest.objects.get(id = int(num)).get_content())
		if creator_interests == []:
			creator_has_interests = False
		

		creator_has_own_avatar = False
		creator_imgs = Img.objects.filter(id = act_infomation['creator'].get_head())
		if len(creator_imgs) != 0:
			creator_img = creator_imgs[0]
			creator_has_own_avatar = True
		else:
			creator_img = ''


		act_imgs = Img.objects.filter(id = act_obj.act_image)
		act_has_show_img = False
		act_img = ''
		if len(act_imgs) > 0:
			act_img = act_imgs[0]
			act_has_show_img = True

		participants_data = [];
		for i in act_infomation['participants']:
			participants_has_own_avatar = False
			participants_imgs = Img.objects.filter(id = i.get_head())
			if len(participants_imgs) != 0:
				participants_img = participants_imgs[0]
				participants_has_own_avatar = True
			else:
				participants_img = ''
			participants_data.append({
				'user':i,
				'participants_img':participants_img,
				'participants_has_own_avatar':participants_has_own_avatar
				})

		return render(request, 'LinkAct/act_info.html', 
			{
				'has_login': has_login,
				'has_own_avatar':has_own_avatar,
				'img':img,
				'user_name':request.user.username,

				'creator_interests':creator_interests,
				'creator_has_interests':creator_has_interests,

				'creator_has_own_avatar':creator_has_own_avatar,
				'creator_img':creator_img,

				'act_infomation':act_infomation,
				'act_img':act_img,
				'act_has_show_img':act_has_show_img,

				'participants_data':participants_data,

				'last_page':current_page,
				'this_page':this_page,
				'this_page_no_para':this_page_no_para,
				'isCreator':isCreator,
				'isParticipant':isParticipant,
				'act_id':index,
				'comment_info':comment_info,

				})
	elif request.method == 'POST':
		if request.POST.get('submit') == '参加':
			index = request.POST.get('act_id', '')
			obj = Activity.objects.filter(id=index)[0]
			obj.append_participants(request.user.id)
			request.user.myuser.append_participate_ongoing_acts(index)

			for i in range(0, len(request.user.myuser.get_friends())):
				other_id = request.user.myuser.get_friends()[i]
				friend = User.objects.filter(id=other_id)[0].myuser
				movement_msg = str(request.user.myuser.get_nickname()) + '参加了活动'
				friend.append_friend_movement_id(request.user.id)
				friend.append_friend_movement(movement_msg)
				friend.append_movement_name(str(obj.name))
				friend.append_movement_link(str(request.get_full_path()))
								
		elif request.POST.get('submit') == '退出':
			index = request.POST.get('act_id', '')
			obj = Activity.objects.get(id=index)
			obj.remove_participants(request.user.id)
			request.user.myuser.remove_participate_ongoing_acts(index)

			for i in range(0, len(request.user.myuser.get_friends())):
				other_id = request.user.myuser.get_friends()[i]
				friend = User.objects.filter(id=other_id)[0].myuser
				movement_msg = str(request.user.myuser.get_nickname()) + '退出了活动'
				friend.append_friend_movement_id(request.user.id)
				friend.append_friend_movement(movement_msg)
				friend.append_movement_name(str(obj.name))
				friend.append_movement_link(str(request.get_full_path()))
		else:
			index = request.POST.get('act_id', '')
			score = request.POST.get('score', '')
			content = request.POST.get('user_comment', '')
			request.user.myuser.create_comment(int(index), int(score), content)
		fresh_path = request.get_full_path()
		return HttpResponseRedirect(fresh_path)

def check_activity_status(acts):
	for index in range(0, len(acts)):
		if acts[index].get_status() == 'finished':
			continue
		if timezone.now() > acts[index].get_start_date() and timezone.now() < acts[index].get_end_date():
			acts[index].set_status('ongoing')
		elif timezone.now() > acts[index].get_end_date():
			acts[index].set_status('finished')
			participants = acts[index].get_participants()
			for i in range(0, len(participants)):
				mine = User.objects.get(id=participants[i]).myuser
				mine.remove_participate_ongoing_acts(acts[index].id)
				mine.append_participate_terminative_acts(acts[index].id)

			create = acts[index].get_creator()
			creator = User.objects.get(id=create).myuser
			creator.remove_create_ongoing_acts(acts[index].id)
			creator.append_create_terminative_acts(acts[index].id)
	return acts


