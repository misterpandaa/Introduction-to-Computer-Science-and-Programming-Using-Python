s = 'abcdefghijklmnopqrstuvwxyz'
start_index = -1
longest_count = -1
current_count = 1

for i in range(1, len(s)):    
    prev_char = s[i - 1]
    curr_char = s[i]

    if curr_char >= prev_char:
        current_count += 1
    else:
        if current_count > longest_count:
            longest_count = current_count
            start_index = i - current_count

        current_count = 1
    
    if i == len(s) - 1 and current_count > longest_count:
        longest_count = current_count
        start_index = i - current_count + 1

print('Longest substring in alphabetical order is: ' + s[start_index : start_index + longest_count])