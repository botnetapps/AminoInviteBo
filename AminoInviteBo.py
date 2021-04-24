from colorama import init, Fore, Back, Style
init()
print(Back.BLACK)
print(Fore.YELLOW)
print(Style.NORMAL)
print("Script by Zevi/Скрипт сделан Zevi")
print("┌────────────────────────────────────┐")
print("│Author :  LilZevi                   │")
print("│Github : https://github.com/LilZevi │")
print("└────────────────────────────────────┘")
print("YouTube: https://www.youtube.com/channel/UCJ61JlXJckmO6yJr8BDRuGQ")
print("▄▀▄ █▄░▄█ ▀ █▄░█ ▄▀▄ ▀ █▄░█ ▐▌░▐▌ ▀ ▀█▀ █▀▀ █▀▄ ▄▀▄")
print("█▀█ █░█░█ █ █░▀█ █░█ █ █░▀█ ░▀▄▀░ █ ░█░ █▀▀ █▀█ █░█")
print("▀░▀ ▀░░░▀ ▀ ▀░░▀ ░▀░ ▀ ▀░░▀ ░░▀░░ ▀ ░▀░ ▀▀▀ ▀▀░ ░▀░")
import amino, concurrent.futures, getpass
client = amino.Client()
def login():
	try:
		email = input("Email/Почта: ")
		password = getpass.getpass("Password/Пароль: ")
		client.login(email=email, password=password)
	except amino.exceptions.ActionNotAllowed:
		print("Replace deviceId or Use Vpn|Proxy|Смените deviceId Или используйте Впн/Прокси.")
	except amino.exceptions.InvalidPassword:
		print("Invalid Password/Неверный пароль")
	except amino.exceptions.InvalidEmail:
		print("Invalid Email/Неверная почта")
	except amino.exceptions.FailedLogin:
		print("Failed Login/Не удалось зайти")
	except:
		pass
login()
clients = client.sub_clients(size=100)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
communityid = clients.comId[int(input("Выберите сообщество/Select the community: "))-1]
sub_client = amino.SubClient(comId=communityid, profile=client.profile)
chats = sub_client.get_chat_threads(size=150)
for z, title in enumerate(chats.title, 1):
	print(f"{z}.{title}")
chatx = chats.chatId[int(input("Выберите чат/Select the chat: "))-1]

#Threadpool invite bot def
def threadinvite():
	sub_client.invite_to_chat(userId=userId, chatId=chatx)

def thread():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor1:
        _ = [executor1.submit(threadinvite) for _ in range(20)]
#Threadpool invite bot def

print("1.Invite Online Users/Пригласить онлайн пользователей")
print("2.Invite User Followers/Пригласить подписчиков пользователя")
inviteselect = input("Type Number/Введите цифру: ")

if inviteselect == "1":
	with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
		for i in range(0, 20000, 250):
			onlineusers = sub_client.get_online_users(start=i, size=100).profile.userId
			recentusers = sub_client.get_all_users(type="recent", start=i, size=100).profile.userId
			curators = sub_client.get_all_users(type="curators", start=i, size=100).profile.userId
			leaders = sub_client.get_all_users(type="leaders", start=i, size=100).profile.userId
			users = [*onlineusers, *recentusers, *curators, *leaders]
			if users:
				for userId in users:
					print(f"{userId} Invited/Приглашен")
					_ = [executor.submit(sub_client.invite_to_chat, userId, chatx)]
					thread()
			else:
				break
		for i in range(0, 20000, 250):
			publichats = sub_client.get_public_chat_threads(type="recommended", start=i, size=100).chatId
			chatsuin = sub_client.get_chat_threads(start=i, size=100).chatId
			chats = [*publichats, *chatsuin]
			if chats:
				for chatid in chats:
					for u in range(0, 1000, 50):
						users = sub_client.get_chat_users(chatId=chatid, start=u, size=100).userId
						if users:
							for userId in users:
								try:
									print(f"{userId} Invited/Приглашен")
									_ = [executor.submit(sub_client.invite_to_chat, userId, chatx)]
									thread()
								except:
									pass
						else:
							break
							print("Invited All Online Users/Пригласили всех онлайн пользователей")

if inviteselect == "2":
	userlink=input("Type user link/Введите ссылку на пользователя: ")
	user=client.get_from_code(userlink)
	userx=user.objectId
	with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
		for i in range(0, 20000, 250):
			followers = sub_client.get_user_followers(userId=userx, start=i, size=100).profileyy.userId
			if followers:
				for userId in followers:
					try:
						print(f"{userId} Invited/Приглашен")
						_ = [executor.submit(sub_client.invite_to_chat, userId, chatx)]
						thread()
					except:
						pass
			else:
				break
				print("Invited User Followers/Пригласили подписчиков пользователя!")
