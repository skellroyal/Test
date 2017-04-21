import time
weather = input()
items = ['umbrella', 'pen']
if weather == 'raining':
    # some codes here fpr raomomg days
    if 'umbrella' in items:
        print('You have an umbrella! Go outside')
    else:
        print('No umbrella! Wait')
        time.sleep(1)
        while weather == 'raining':
            print('How is the weather now?')
            weather = input()
            time.sleep(1)
        print('go outside')
else:
    print('It\'s not raining. Go outside')
