s = 'azcbobobegghakl'
bob_count = 0
start_pos = 0

while True:
    index = s.find('bob', start_pos)

    if (index == -1):
        break
    
    bob_count += 1
    start_pos = index + 1

print('Number of times bob occurs is: ' + str(bob_count))