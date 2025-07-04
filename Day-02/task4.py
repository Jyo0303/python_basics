print("How do you prefer to spend your weekend?\n1. Going out, meeting people, or trying something new\n2. Staying in, relaxing, or doing something quiet")
a=int(input("choose a option: (1/2)"))
flag1=0
flag2=0
if a==1:
    flag1+=1
elif a==2:
    flag2+=1
else:
    print("choose option 1 or 2")
print("When making decisions, you usually...\n1. Act quickly based on instinct or excitement\n2. Think things through and weigh the pros and cons")
b=int(input("choose a option: (1/2)"))
if b==1:
    flag1+=1
elif b==2:
    flag2+=1
else:
    print("choose option 1 or 2")
print("In a group project, you prefer to...\n1. Take the lead or jump into action\n2. Observe, plan, and contribute thoughtfully")
c=int(input("choose a option: (1/2)"))
if c==1:
    flag1+=1
elif c==2:
    flag2+=1
else:
    print("choose option 1 or 2")
if flag1>flag2:
    print("The Go-Getter\nYou're energetic, spontaneous, and action-driven. You enjoy social interaction, fast-paced environments, and leading from the front. You act on ideas and make things happen quickly.")
else:
    print("The Reflector\nYou're calm, thoughtful, and introspective. You prefer to take your time, think deeply, and contribute meaningfully. You work best in focused, relaxed environments where quality matters.")
