print('hello python world')

# sublime ctrl + b, build python

message = 'hello'
print(message)

message = 'hello world'
name = 'heke'
# \t 制表符 \n 换行符
full_message = '\t' + message + '\n\t' + name
print(message.title())
print(full_message.title())

# 删除末尾空白 rstrip()
# 删除头部空白 lstrip()
# 删除首尾空白 strip()
favorite_language = ' python '
print(favorite_language.rstrip())

# 语法错误
favorite_language = ' I\'m Frank.'
print(favorite_language.upper())
print(favorite_language.lower())