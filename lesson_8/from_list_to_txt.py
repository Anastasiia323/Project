"""In this task I have to input four strings and write them to different variables.
After that I have to write them to .txt document"""


"""I've made a cycle to input four strings"""
my_list = []
for i in range(4):
    strings_to_write = input(f'Write the text {i}: ')
    my_list.append(strings_to_write)


new_doc = open('text_1.txt', 'w')
new_doc.write(my_list[0] + '\n' + my_list[1] + '\n')

new_doc.close()

new_doc = open('text_1.txt', 'a')
new_doc.write(my_list[2] + '\n' + my_list[3] + '\n')

new_doc.close()