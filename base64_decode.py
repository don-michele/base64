### This is a program that will decode any base64 string using base64 decription

final_user_input=raw_input("Please type the string you want to decrypt: ")

base64_string_alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

# Defining a function that will convert the base64 string into base64 code values

def strbase64_to_valuebase64(str_to_convert):
    value_base64_list=[]
    for character in str_to_convert:
        if (character != '='):
            value_base64_list.append(base64_string_alphabet.index(character))
        else:
            value_base64_list.append(character)
    return value_base64_list

#print strbase64_to_valuebase64(final_user_input)

# Defining a function that will convert the base64 codes into binary

def valuebase64_to_binary(base64_code_list):
    binary_base64_list=[]
    static_binary_base64_lenght=6
    for element in base64_code_list:
        if (element != '='):
            binary_base64_value="{0:b}".format(int(element))
            final_binary_base64_value=(static_binary_base64_lenght - len(binary_base64_value)) * '0' + binary_base64_value
            binary_base64_list.append(final_binary_base64_value)
        else:
            binary_base64_list.append('000000')
    return binary_base64_list

#print valuebase64_to_binary(strbase64_to_valuebase64(final_user_input))

# Defining a function that will create a string from the binary list

def get_str_from_binary_list(binary_list):
    binary_string=''
    for element in binary_list:
        binary_string += element
    return binary_string

#print get_str_from_binary_list(valuebase64_to_binary(strbase64_to_valuebase64(final_user_input)))

# Defining a function that will split the string in 8-bit elements

def split_binary_string(bin_string):
    list_8_bit=[]
    len_bin_string=len(bin_string)
    for i in range(0, len_bin_string, 8):
        list_8_bit.append(bin_string[i:i+8])
    return list_8_bit

#print split_binary_string(get_str_from_binary_list(valuebase64_to_binary(strbase64_to_valuebase64(final_user_input))))

# Defining a function that will remove the extra added bites

def remove_extra_bites(base64_binary_list):
    final_binary_list=[]
    for item in base64_binary_list:
        if (item != '00000000'):
            final_binary_list.append(item)
    return final_binary_list

#print remove_extra_bites(split_binary_string(get_str_from_binary_list(valuebase64_to_binary(strbase64_to_valuebase64(final_user_input)))))

# Defining a function that will convert the binary into ascii values

def convert_binary_to_ascii(final_list):
    ascii_value_list=[]
    for x in final_list:
        ascii_value_list.append(int(x, 2))
    return ascii_value_list

#print convert_binary_to_ascii(remove_extra_bites(split_binary_string(get_str_from_binary_list(valuebase64_to_binary(strbase64_to_valuebase64(final_user_input))))))

# Defining a function that will convert the values to initial code

def final_convert(ascii_val_list):
    final_string=''
    ascii_final_list=[]
    for i in ascii_val_list:
        ascii_final_list.append(chr(i))
    for val in ascii_final_list:
        final_string += val
    return final_string

#print final_convert(convert_binary_to_ascii(remove_extra_bites(split_binary_string(get_str_from_binary_list(valuebase64_to_binary(strbase64_to_valuebase64(final_user_input)))))))

intermediate_step_1=strbase64_to_valuebase64(final_user_input)
intermediate_step_2=valuebase64_to_binary(intermediate_step_1)
intermediate_step_3=get_str_from_binary_list(intermediate_step_2)
intermediate_step_4=split_binary_string(intermediate_step_3)
intermediate_step_5=remove_extra_bites(intermediate_step_4)
intermediate_step_6=convert_binary_to_ascii(intermediate_step_5)
final_value=final_convert(intermediate_step_6)
print final_value