from time import sleep
from tqdm import tqdm

loop = tqdm(total = 5000, position = 0, leave = False)
for k in range(5000):
    loop.set_description("POWERING ON".format(k))
    loop.update(1)
sleep(3)
loop.close()

who_am_i = ("arivvid27's bot")
sleep(3)
print('Oh, umm... hi?')
sleep(0.9)
name = input('What your name? \n')
sleep(0.9)
if (name == 'arivvid27'):
	print('Oh, Hi, it\'s you!!')
else:
	print(f"{name}. hmmm... I guess thats a nice name.")
sleep(0.9)
system = input('Do you have a gaming console or something? \n')
if (system == 'no'):
	print('oh... ok. I have a console.')
elif (system == 'NO'):
	print('Ok, ok... I was just asking...')
	sleep(3)
elif (system == 'yes'):
	print('oh, thats nice, I have a console, too!')
elif (system == 'YES'):
	print('I see you like this question')
else:
	print('What? actually, nevermind.')

sleep(0.3)
game = input('So... do you like Rocket League? \n')
if (game == 'no'):
	game2 = input('ok... Do you like Minecraft, though? \n')
	if (game2 == 'no'):
		print('Oh. Those are the only games I play...')
	elif (game2 == 'yes'):
		print('At least thats a game we can play.')
elif (game == 'yes'):
	print('oh, yay! I LOVE Rocket League!!')
else:
	print('... \n')

sleep(0.9)
ask = input('You wanna ask me a question? \n')
if (ask == 'yes'):
	question_1 = input('What is it? \n')
	if (question_1 == 'who are you'):
		print(f"I am {who_am_i}.")
	elif (question_1 == 'what are you'):
		print('I am a bot...')
	elif (question_1 == 'whats your favorite color'):
		print('Blue is my favorite color.')
	else:
		print('I don\'t know')
		print('Ok. don\'t close this yet. There is one more thing.')
elif (ask == 'no'):
	print('Ok. don\'t close this yet. There is one more thing.')
else:
	print('I don\'t know that, but please don\'t close this yet. there is one more thing I need to ask.')
sleep(4)

print('Please comment what you think about me and what arivvid27 should add to me. Oh, and don\'t forget to upvote me!')

sleep(4)
print('SHUTTING DOWN...')

print(':) bye! You might see me next time with more upgrades!')

sleep(3)
exit('~~~~BOT IS SHUT DOWN~~~~')
