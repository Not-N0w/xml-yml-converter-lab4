# XML -> YAML
def xml_to_yaml_base(input_file_name,  output_file_name):
    input_file = open(input_file_name, 'r', encoding = "utf-8") # Открываем ффайл ввода
    output_file = open(output_file_name,'w', encoding = "utf-8") # Открываем файл вывода

    lines = input_file.readlines() # Считываем данные
    tabs = 0 # Счетчик пробелов
    past_tags = [] # теги, которые уже были (избегаем повторения тегов)
    need_dash = False
    saved_scope = []
    for line in lines:
        splited_line = line.strip('><    \n').replace('<', '>').split('>') # Получаем массив в формате (1) ["tag", "content", "/tag"] или (2) ["tag"] или (3) ["/tag"]
    
        if len(splited_line) == 0: continue # Проверка на пустую строку
        if len(splited_line) == 1: # Если случай 2 или 3
            if splited_line[0][0] == '/': # Случай 3
                tabs -= 1 
                past_tags = past_tags[0:saved_scope[-1]]
                saved_scope.pop()
            else: # Случай 2
                if not splited_line[0] in past_tags:
                    past_tags.append(splited_line[0])
                    output_file.write(tabs * '  ' + splited_line[0] + ':\n') # Вывод head-тега
                tabs += 1
                saved_scope.append(len(past_tags))
                need_dash = True
        else: # Случай 1
            output_file.write((tabs-1) * '  ') 
            if need_dash:
                output_file.write('- ')
                need_dash = False
            else: 
                output_file.write('  ')
            output_file.write(splited_line[0] + ': ' +  splited_line[1] + '\n') # Вывод тега и контента
    input_file.close()
    output_file.close()

xml_to_yaml_base("input.xml", "output.yml")