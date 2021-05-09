'''
f = open("./tf_examples.tfrecord", 'rb')  # 二进制读
lines = f.readlines()
for line in lines:
    print(line)
f.close()
'''
# ==================================================================
f = open("./2018data.txt", 'r', encoding='utf-8')  # 二进制读
lines = f.readlines()
new_list = {}
for line in lines:
    line = line.strip()
    line = line.split('\t')
    big_number = line[0]
    small_number = line[1]
    number = line[2]
    father_number = line[3]
    name = line[4]
    elements = eval(line[5])
    sentence_a = number + '|' + '商品名称|' + '|'.join([key for key in elements.keys()])
    sentence_b = number + '|' + name + '|' + '|'.join([values for values in elements.values()])
    if father_number in new_list.keys():
        new_list[father_number][0].append(sentence_a)
        new_list[father_number][0].append(sentence_b)
        new_list[father_number][1].append(number)
    else:
        new_list[father_number] = [[], []]
f.close()

with open('./all_train.txt', 'w', encoding='utf-8')as f:
    for key, value in new_list.items():
        elements = value[0]
        id = set(value[1])
        if len(id) == 0:
            continue
        if len(id) == 1:
            # f.write(str(len((id))) + '\n')
            f.write('\n')
            for element in elements:
                element = '1' + '|' + '|'.join(element.split('|')[1:])
                element = '|'.join(element.split('|')[1:])
                f.write(element)
                f.write('\n')
        else:
            # f.write(str(len((id))) + '\n')
            f.write('\n')
            for element in elements:
                element = str(list(id).index(element.split('|')[0]) + 1) + '|' + '|'.join(element.split('|')[1:])
                element = '|'.join(element.split('|')[1:])
                f.write(element)
                f.write('\n')
    print('finish')

# import random
# rng = random.Random(12345)
# for _ in range(10):
#     print(rng.randint(1, 5))
# import re
# iter = re.finditer('\|', 'hjgshdb|sjdb|sjdvb')
# for i in iter:
#     print(i.group())
#     print(i.span())
# import random
# rng = random.Random(12345)
# print(rng.randint(1, 1))