def crack_layout(config):
    config_layout = {
        'top_center': '',
        'top_left': '',
        'top_right': '',
        'middle': '',
        'bottom_left': '',
        'bottom_right': '',
        'bottom_center': ''
    }
    num_strings = {
        'zero': '',
        'one': '',
        'two': '',
        'three': '',
        'four': '',
        'five': '',
        'six': '',
        'seven': '',
        'eight': '',
        'nine': ''
    }
    nums_with_six_lines = []
    nums_with_five_lines = []
    for num in config:
        if len(num) == 2:
            num_strings['one'] = num
        elif len(num) == 3:
            num_strings['seven'] = num
        elif len(num) == 4:
            num_strings['four'] = num
        elif len(num) == 7:
            num_strings['eight'] = num
        elif len(num) == 6:
            nums_with_six_lines.append(num)
        else:
            nums_with_five_lines.append(num)

    config_layout['top_center'] = num_strings['seven'].replace(
        num_strings['one'][0], '').replace(num_strings['one'][1], '')
    for num in nums_with_six_lines:
        if not num_strings['one'][0] in num or not num_strings['one'][1] in num:
            num_strings['six'] = num
    nums_with_six_lines.remove(num_strings['six'])
    config_layout['top_right'] = num_strings['one'][0] if num_strings['one'][1] in num_strings['six'] else num_strings['one'][1]
    config_layout['bottom_right'] = num_strings['one'][1] if num_strings['one'][1] in num_strings['six'] else num_strings['one'][0]
    for num in nums_with_six_lines:
        if num_strings['four'].replace(num_strings['one']
                                       [0], '').replace(num_strings['one'][1], '')[0] in num and num_strings['four'].replace(num_strings['one']
                                                                                                                             [0], '').replace(num_strings['one'][1], '')[1] in num:
            num_strings['nine'] = num
    nums_with_six_lines.remove(num_strings['nine'])
    num_strings['zero'] = nums_with_six_lines[0]
    for num in nums_with_five_lines:
        if not config_layout['top_right'] in num:
            num_strings['five'] = num
    nums_with_five_lines.remove(num_strings['five'])
    for num in nums_with_five_lines:
        if config_layout['bottom_right'] in num:
            num_strings['three'] = num
    nums_with_five_lines.remove(num_strings['three'])
    num_strings['two'] = nums_with_five_lines[0]
    for i in num_strings['eight']:
        if not i in num_strings['zero']:
            config_layout['middle'] = i
    common = config_layout['top_center'] + config_layout['top_right'] + \
        config_layout['middle'] + config_layout['bottom_right']
    for i in num_strings['three']:
        if not i in common:
            config_layout['bottom_center'] = i
    common += config_layout['bottom_center']
    for i in num_strings['nine']:
        if not i in common:
            config_layout['top_left'] = i
    common += config_layout['top_left']
    for i in num_strings['eight']:
        if not i in common:
            config_layout['bottom_left'] = i
    return(config_layout)


searched_digits = 0
result = 0

for config, nums in zip(((numbers[0][:-1].split(' ') for numbers in (line.split('|') for line in open(
        'day8/day8.txt').readlines()))), ((numbers[1][1:].strip('\n').split(' ') for numbers in (line.split('|') for line in open(
        'day8/day8.txt').readlines())))):

    # FIRST PART
    for num in nums:
        if len(num) == 2 or len(num) == 3 or len(num) == 4 or len(num) == 7:
            searched_digits += 1
    # SECOND PART
    config_layout = crack_layout(config)
    temp_num = ''
    for num in nums:
        temp_digit = ''
        if len(num) == 2:
            temp_digit = '1'
        elif len(num) == 3:
            temp_digit = '7'
        elif len(num) == 4:
            temp_digit = '4'
        elif len(num) == 7:
            temp_digit = '8'
        elif len(num) == 5:
            if config_layout['top_left'] in num:
                temp_digit = '5'
            elif config_layout['bottom_left'] in num:
                temp_digit = '2'
            else:
                temp_digit += '3'
        elif len(num) == 6:
            if not config_layout['middle'] in num:
                temp_digit = '0'
            elif config_layout['top_right'] in num:
                temp_digit = '9'
            else:
                temp_digit = '6'
        temp_num += temp_digit
    result += int(temp_num)

print(searched_digits)
print(result)
