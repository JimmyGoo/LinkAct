#搜索部分网址格式http://192.168.55.33:8000/search/?search_class=nickname&search_content=u&search_page=1
#   search_class表示搜索类别，search_content表示搜索内容,search_content表示搜索的页码号，要在template中动态生成
#


from .models import MyUser,Activity,Theme
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import AnonymousUser
from django.core.mail import send_mail
from .forms import RegisterForm
from .forms import LogForm
from .forms import PersonalInfoForm
from .forms import SetPasswordForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from LinkAct.models import Img, Interest
import string
from datetime import date
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
	has_login = False
	user = request.user
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')

	if request.user.username == AnonymousUser.username:
		has_login = False
		return render(request, 'LinkAct/explore_page.html',
		{'user_name':user.username, 'has_login':has_login})
	else:
		has_login = True
		imgs = Img.objects.filter(id = user.myuser.get_head())
		if len(imgs) != 0:
			img = imgs[0]
			return render(request, 'LinkAct/explore_page.html',
			{'user_name':user.username, 'has_login':has_login, 'img': img, 'has_own_avatar':True})
		else:
			return render(request, 'LinkAct/explore_page.html',
			{'user_name':user.username, 'has_login':has_login, 'has_own_avatar':False})
	#-----------登录判定----------#

	

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
		#判定完毕
		myUser = MyUser()
		myUser.create_user(usernames, password1, email)
		user = auth.authenticate(username=usernames, password=password1)
		auth.login(request,user)
		return render(request, 'LinkAct/result_page.html', {'error_index':0})
 
	return render(request, 'LinkAct/register_page.html', {'form':form})
		


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
		 
		return HttpResponseRedirect('../?search_class=create_time&search_content=None&search_order=1&search_page=1')
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

#修改活动信息，仅活动创建人能进入此页面，修改完成后用input按钮提交，用hidden的input标签传回id及last_page
def check_act_msg(request):
	if request.method == 'GET':
		i = request.GET['id']
		last_page = request.GET['last_page']
		to_check_act = Activity.objects.get(id=i)
		
		form = ActForm()
		
		return render(request, 'LinkAct/actShow.html', {'form': form, 'act_obj':to_check_act, 'last_page':last_page, 'id':i})
	else:
		params = request.POST
		i = request.POST['id']
		last_page = request.POST['last_page']
		to_check_act = Activity.objects.get(id=i)
		to_check_act.set_locale(params.get('locale', ''))
		to_check_act.set_theme(params.get('theme', ''))
		to_check_act.update_start_date(params.get('start_date', ''))
		to_check_act.update_end_date(params.get('end_date', ''))
		to_check_act.set_introduction(params.get('introduction', ''))

		return HttpResponseRedirect(last_page)

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
	has_login = True
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
						'default_province':default_province,
						'default_city':default_city,
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
		current_page = request.GET['last_page'] + "&search_content=" + str(request.GET['search_content']) + "&search_order=" + str(request.GET['search_order']) + "&search_page=" + str(request.GET['search_page'])
		print(index)
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
			print(imgs)
			form = PersonalInfoForm()
			print('fuck', personal_msg.myuser.phone_number)

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
							'my_url':my_url
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
							'my_url':my_url
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
							'my_url':my_url
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
							'my_url':my_url
						})
		else:
			return render(request, 'LinkAct/personal_info.html', 
					{
						'has_login': has_login, 
						'form':form, 
						'interest_msg': interest_msg, 
						'personal_msg':personal_msg, 
						'last_page':current_page, 
						'my_url':my_url
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
				answer = MyUser.objects.all().order_by('id')

			else:
				print('fuck')
				print(search_class)
				answer = user.myuser.user_filter(search_class, search_content)
				print(answer)

			answer = list(answer)
			for i in range(len(answer)):
				if answer[i].user.username == request.user.username:
					del answer[i]


			startPos = (int(search_page) - 1) * 10
			endPos = int(search_page) * 10
			if endPos >= len(answer):
				endPos = len(answer)

			result = answer[startPos:endPos]

			temp_url = request.get_full_path()

			next_page = int(search_page) + 1

			next_page_url = request.path + "?search_class=" + search_class + "&search_content=" + search_content + "&search_order=" + search_order + "&search_page=" + str(next_page)

			#整合用户#
			pass_data = []
		
			for show_user in result:
				other_has_own_avatar = False
				other_imgs = Img.objects.filter(id = show_user.get_head())
				if len(other_imgs) != 0:
					other_img = other_imgs[0]
					other_has_own_avatar = True
				else:
					
					other_img = ''

				other_interests_num = show_user.get_interests()
				print(other_interests_num)
				other_interests = []
				has_interest = True
				if other_interests_num != []:
					for num in other_interests_num:
						print(num)
						other_interests.append(Interest.objects.get(id = int(num)).get_content())
				if other_interests == []:
					has_interest = False
				pass_data.append({'other_user':show_user, 'other_img':other_img, 'other_has_own_avartar':other_has_own_avatar,
					'other_interests':other_interests, 'has_interest':has_interest})

			search_class_pass_text = '无条件筛选'
			search_class_pass_value = 'all'
			for i in search_value_string:
				if i['value'] == search_class:
					search_class_pass_text = i['string']
					search_class_pass_value = i['value']
					print(search_class_pass_value)
					print(search_class_pass_text)
					break;

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
							'requests':request.user.myuser.get_waiting(),
							'user_name': user_name,
							'search_class_pass_value':search_class_pass_value,
							'search_class_pass_text':search_class_pass_text,
							'search_content_pass_text':search_content,
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
							'requests':request.user.myuser.get_waiting(),
							'user_name': user_name,
							'search_class_pass_value':search_class_pass_value,
							'search_class_pass_text':search_class_pass_text,
							'search_content_pass_text':search_content,
						})   

		elif request.method == 'POST':
			params = request.POST

			if request.POST.get('submit') == 'search_submit':

				aim_url = request.path

				if params.get('search_content', '') == '':
					aim_url = aim_url + "?search_class=" + params.get('search_class', '') + "&search_content=" + params.get('search_content', '') + "&search_order=1&search_page=1" 
				else:
					aim_url = aim_url + "?search_class=" + params.get('search_class', '') + "&search_content=" + params.get('search_content', '') + "&search_order=0&search_page=1" 
				return HttpResponseRedirect(aim_url)


			else:
				if request.POST.get('submit') == '同意':
					agreed_id = int(request.POST.get('request_id'))
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
		#搜索类别
		search_class = request.GET['search_class']
		#搜索内容
		search_content = request.GET['search_content'] 
		#搜索页码
		search_page = request.GET['search_page']
		#排序方法，为1时表示按照类别倒序排序，不搜索只排序
		search_order = request.GET['search_order']


		answer = []

		if search_order == '1':
			answer = Activity.objects.all().order_by(search_class)

		#不同检索方式
		elif search_class == 'theme':
			answer = request.user.myuser.activity_filter(Activity.objects.all(), search_class)

		elif search_class == '':
			return

		startPos = (int(search_page) - 1) * 10
		endPos = int(search_page) * 10
		if endPos >= len(answer):
			endPos = len(answer)

		result = answer[startPos:endPos]

		pass_data = []
		for i in result:
			img = Img.objects.filter(id = i.act_image)
			has_show_img = False
			pass_image = ''
			if len(img) > 0:
				pass_image = img[0]
				has_show_img = True
			pass_data.append({'act':i,'pass_img':pass_image, 'has_show_img':has_show_img})
			

		new_movements = request.user.myuser.get_friend_movement()
		new_names = request.user.myuser.get_movement_name()
		new_links = request.user.myuser.get_movement_link()
		new_data = []
		for i in range(0, len(new_movements)):
			new_data.append((new_movements[i], new_names[i], new_links[i]))
		request.user.myuser.clear_friend_movement()
		request.user.myuser.clear_movement_name()
		request.user.myuser.clear_movement_link()
		print('哈哈哈', new_data, type(new_data))
		for (x,y,z) in new_data:
			print(x,y,z)
		next_page = int(search_page) + 1

		temp_url = request.get_full_path()
		next_page_url = request.path + "?search_class=" + search_class + "&search_content=" + search_content + "&search_order=" + search_order + "&search_page=" + str(next_page)

		return render(request, 'LinkAct/activities_page.html', 
			{
				'pass_data':pass_data, 
				'current_page':int(search_page), 
				'current_url':request.get_full_path(), 
				'next_page_url':next_page_url,
			 	'no_param_path':request.path, 
			 	'new_data':new_data
		 	})
	elif request.method == 'POST':
		params = request.POST
		if request.POST.get('submit') == 'search_submit':
			aim_url = request.path
			aim_url = aim_url + "?search_class=" + params.get('search_class', '') + "&search_content=" + params.get('search_content', '') + "&search_order=0&search_page=1" 
			return HttpResponseRedirect(aim_url)

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

	if request.method == 'GET':
		index = int(request.GET['id'])
		current_page = request.GET['last_page'] + "&search_content=" + str(request.GET['search_content']) + "&search_order=" + str(request.GET['search_order']) + "&search_page=" + str(request.GET['search_page'])
		act_obj = Activity.objects.filter(id=index)

		this_page = request.get_full_path()
		this_page_no_para = request.path

		actForm = ActForm()

		#是否活动发起人，决定了是否能修改活动信息
		isCreator = False
		if request.user.id == act_obj[0].creator:
			isCreator = True

		return render(request, 'LinkAct/act_info.html', {'has_login': has_login, 'form':actForm, 'act_obj':act_obj, 'last_page':current_page, 'this_page':this_page, 'this_page_no_para':this_page_no_para, 'isCreator':isCreator, 'act_id':index})

	elif request.method == 'POST':
		if request.POST.get('submit') == '参加':
			index = request.POST.get('act_id', '')
			obj = Activity.objects.filter(id=index)[0]
			obj.append_participants(request.user.id)
			request.user.myuser.append_participate_ongoing_acts(index)

			for i in range(0, len(request.user.myuser.get_friends())):
				other_id = request.user.myuser.get_friends()[i]
				print('我操', other_id)
				friend = User.objects.filter(id=other_id)[0].myuser
				movement_msg = str(request.user.myuser.get_nickname()) + '参加了活动'
				friend.append_friend_movement(movement_msg)
				print(friend.get_friend_movement())
				friend.append_movement_name(str(obj.name))
				friend.append_movement_link(str(request.get_full_path()))
								
		elif request.POST.get('submit') == '退出':
			index = request.POST.get('act_id', '')
			obj = Activity.objects.filter(id=index)
			obj.remove_participants(request.user.id)
			request.user.myuser.remove_participate_ongoing_acts(index)

			for i in range(0, len(request.user.myuser.friends)):
				other_id = request.user.myuser.get_friends()[i]
				print('我操', other_id)
				friend = User.objects.filter(id=other_id)[0].myuser
				movement_msg = str(friend.nickname) + '退出了活动'
				friend.append_friend_movement(movement_msg)
				friend.append_movement_name(str(obj.name))
				friend.append_movement_link(str(request.get_full_path()))
		fresh_path = request.get_full_path()
		return HttpResponseRedirect(fresh_path)

#修改活动信息
def check_act_msg(request):
	if request.method == 'GET':
		index = request.GET['id']
		back_page = request.GET['back_page'] + "&last_page=" + request.GET['last_page'] + "&search_content="+ str(request.GET['search_content']) + "&search_order=" + str(request.GET['search_order']) + "&search_page=" + str(request.GET['search_page'])

		act = Activity.objects.filter(id=index)

		actForm = ActForm()

		return render(request, 'LinkAct/check_act_msg.html', {'form':actForm, 'act':act, 'back_page':back_page})
	elif request.method == 'POST':
				#保存修改并发送邮件
		back_page = request.POST.get('back_page', '')
		return HttpResponseRedirect(back_page)

#添加好友
def request_for_friend(request):
	return render(request, '??弹窗或新页面', {})

def send_emails(email_from, email_to, title, content):
	send_mail('wf', 'wf', "Louyk14@163.com", "Louyk14@163.com", fail_silently=False)

def check_activity_status():
	act_all = Activity.objects.all()

	for index in range(0, len(act_all)):
		if act_all[index].get_status() == 'finished':
			continue
		if timezone.now() > act_all[i].get_start_date() and timezone.now() < act_all[i].get_end_date():
			act_all[index].set_status('ongoing')
		elif timezone.now() > act_all[i].get_end_date():
			act_all[index].set_status('finished')
