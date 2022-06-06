name = "Alexander"
univer = "bsmu"
stage = 6


string_template = "My names is: {}. I'm study in: {}.In the {}th year"
print(string_template.format("Alexander", "bsmu", 6))
print(string_template.format(name, univer, stage))

print(string_template.format("Alexander", "bsmu" , 6, 800, "abc", 777))

string_template = "My names is: {0}. I'm: {1} years old. There are {2} people in the class"
print(string_template.format(name, univer, stage))


string_template = "My names is: {1}. I'm: {2} years old. There are {0} people in the class"
print(string_template.format(name, univer, stage))

string_template = "My names is: {1}. I'm: {2} years old. There are {2} people in the class"


string_template = "My names is: {info[0]}. I'm: {info[1]} years old. There are {info[2]} people in the class"
print(string_template.format(info=[name, univer, stage]))

my_string = f"My names is: {name}. I'm: {univer} years old. There are {stage} people in the class"
print(my_string)
