# XML -> YAML (Re)
import re

def xml_to_yaml_re(input_file_name,  output_file_name):
    input_file = open(input_file_name, 'r', encoding = "utf-8") # Открываем ффайл ввода
    output_file = open(output_file_name,'w', encoding = "utf-8") # Открываем файл вывода

    xml = input_file.read()
    xml = re.sub(r"  ", " ", xml)
    tags = re.findall(r"<[^ />]+>", xml)

    for tag in tags:
        if re.search(r" *\n *<\/{0}> *\n *<{0}> *\n".format(tag.strip("<> ")), xml): # ищем 2 одинак тега в соседних строках (close open)
            xml = re.sub(r" *\n *<\/{0}> *\n *<{0}> *\n  ".format(tag.strip("<>")), "\n"  + " -", xml) # значит "-" тк новый тег такой же, как предыдущий
            xml = re.sub(r"{0} *\n  ".format(tag), tag + "\n" + " -", xml) # вставка - перед первым тегом
    
    xml = re.sub(r"</([^>]+)>", "", xml)
    xml = re.sub(r">", ": ", xml)
    xml = re.sub(r"[<>]", "", xml)

    output = ""
    for line in xml.splitlines(): # убрать пустые строки и развернуть dash 
        dash = re.search("^ \-\s*", line, flags=re.MULTILINE)
        if dash:
            line = line.replace(dash.group(), ''.join(reversed(dash.group())))
        if not re.search(r"^[\n ]*$", line):
            output += line + "\n"

    output_file.write(output)

xml_to_yaml_re("input.xml", "output2.yml")