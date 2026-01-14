guess_name = "kaka"
guess=" "
guess_count = 0
guess_limit = 3
while guess_name != guess and guess_count<=3:
    
    if guess_count<guess_limit:
        print("you have chances")
        guess = input("enter a name")
        guess_count += 1
    else:
        guess_count = 4
if guess_count >= guess_limit:
    print("you lost no more guesses")
else:
    print("you won")