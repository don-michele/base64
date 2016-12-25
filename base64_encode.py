### This is a program that will encode any string using base64 encription

final_user_input=raw_input("Please type the string you want to encrypt: ")

#final_user_input=user_input.replace(" ", "")

# Defining the base64 string values

base64_string_alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

# Defining a function that will make a list with the ascii value for each character in the string

def char2asciinumvalue(str_to_convert):
    ascii_item_num_list=[]
    for item in str_to_convert:
        ascii_num_value=ord(item)
        ascii_item_num_list.append(ascii_num_value)
    return ascii_item_num_list

###print char2asciinumvalue(final_user_input)

# Defining a function that will convert the values of the list we just made to their binaty values

def int2binary(int_list_value):
    default_byte_lenght = 8
    binary_list_values=[]
    for element in int_list_value:
        bin_val="{0:b}".format(element)
        if len(bin_val) == default_byte_lenght:
            binary_list_values.append(bin_val)
        else:
            new_bin_val=(default_byte_lenght - len(bin_val)) * '0' + bin_val
            binary_list_values.append(new_bin_val)
    return binary_list_values

###print int2binary(char2asciinumvalue(final_user_input))

# Defining a function that will return a one-piece string from the binary list

def binarylist2string(binarylist):
    old_binary_string=''
    for item in binarylist:
        old_binary_string = old_binary_string + item
    return old_binary_string

###print binarylist2string(int2binary(char2asciinumvalue(final_user_input)))

# Defining a function that will make a complete binary string

def new_binary_list2string(old_string):
    old_string_lenght=len(old_string)
    if old_string_lenght % 24 == 0:
        new_string=old_string
    else:
        new_string = old_string + (24 - (old_string_lenght % 24)) * '0'
    return new_string

###print new_binary_list2string(binarylist2string(int2binary(char2asciinumvalue(final_user_input))))

# Defining a function that will create the base64 binary element list

def getbase64binarylist(bin_string):
    base64_bin_list=[]
    len_bin_string=len(bin_string)
    if (len_bin_string % 24 != 0):
        print "Bad base64 binary string!"
    for i in range(0, len_bin_string, 6):
        base64_bin_list.append(bin_string[i:i+6])
    return base64_bin_list

###print getbase64binarylist(new_binary_list2string(binarylist2string(int2binary(char2asciinumvalue(final_user_input)))))

# Defining a function that returns the list with encoded elements

def encodebin2base64(base64_list):
    encoded_list=[]
    #pad_count=0
    if ((base64_list[-1] == '000000') and (base64_list[-2] == '000000')):
        pad_count = 2
    elif ((base64_list[-1] == '000000') and (base64_list[-2] != '000000')):
        pad_count = 1
    else:
        pad_count = 0
    diff = len(base64_list) - pad_count
    for i in range(0, diff):
        encoded_list.append(base64_list[i])
    if (pad_count != 0):
        for j in range(0, pad_count):
            encoded_list.append('pad')
    return encoded_list

###print encodebin2base64(getbase64binarylist(new_binary_list2string(binarylist2string(int2binary(char2asciinumvalue(final_user_input))))))

# Defining a function that converts base64 binary into base64 codes

def base64bin_to_code64(managed_list):
    final_list=[]
    for x in managed_list:
        if (x != 'pad'):
            member=int(x, 2)
            final_list.append(member)
        else:
            final_list.append('=')
    return final_list

###print base64bin_to_code64(encodebin2base64(getbase64binarylist(new_binary_list2string(binarylist2string(int2binary(char2asciinumvalue(final_user_input)))))))

# Defining a function that coverts base64 codes to base64 characters

def base64_code_to_char(good_list):
    final_string=''
    base64_list=[]
    for value in good_list:
        if (value != '='):
            code_char=base64_string_alphabet[value]
            base64_list.append(code_char)
        else:
            base64_list.append(value)
    for val in base64_list:
        final_string += val
    return final_string

###print base64_code_to_char(base64bin_to_code64(encodebin2base64(getbase64binarylist(new_binary_list2string(binarylist2string(int2binary(char2asciinumvalue(final_user_input))))))))

intermediate_step_1=char2asciinumvalue(final_user_input)
intermediate_step_2=int2binary(intermediate_step_1)
intermediate_step_3=binarylist2string(intermediate_step_2)
intermediate_step_4=new_binary_list2string(intermediate_step_3)
intermediate_step_5=getbase64binarylist(intermediate_step_4)
intermediate_step_6=encodebin2base64(intermediate_step_5)
intermediate_step_7=base64bin_to_code64(intermediate_step_6)
final_value=base64_code_to_char(intermediate_step_7)
print final_value