import re

def xml_to_xaml(input_file_name,  output_file_name):
    input_file = open(input_file_name, 'r', encoding = "utf-8") # Открываем ффайл ввода
    output_file = open(output_file_name,'w', encoding = "utf-8") # Открываем файл вывода

    lines = input_file.readlines() 
    tabs = 0
    for line in lines:
        splited_line = line.strip('>    <\n').replace('<', '>').split('>')
        if len(splited_line) == 0: continue 
        elif len(splited_line) == 1: 
            output_file.write(line)
        else:
            new_tag = "<" + splited_line[0]
            new_tag += " text = '" + splited_line[1] + "'"
            new_tag += "/>"

            prev_tag = re.search(r"<.*>.*<\/.*>", line).group()
            line = line.replace(prev_tag, new_tag)
            output_file.write(line)

    input_file.close()
    output_file.close()

xml_to_xaml("input.xml", "output5.xaml")