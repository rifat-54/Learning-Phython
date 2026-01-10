import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

# if(timestamp<10):
#     print("good morning Rifat!")
# elif(timestamp<2):
#     print("good noon!")
# elif(timestamp<6):
#     print("good afternoon")
# else:
#     print("good evening")
