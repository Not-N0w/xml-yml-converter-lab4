import re

input = []
output = ""
tabs = 0
ind = 0
past_tags = []
need_dash = False

def head_tag():
    global ind, output, tabs, input, past_tags,need_dash
    if not input[ind] in past_tags:
        past_tags.append(input[ind])
        if need_dash:
            output += (tabs-1) * "  " + "- "
            #need_dash = False
        else:
            output += tabs * "  "
            need_dash = True
        output += input[ind] + ": "
        if input[ind + 1][0] != '"':
            output += '\n'
    else:
        need_dash = True
    tabs += 1
    ind += 1
    return
    
def tail_tag():
    global ind, tabs, output
    output += '\n'
    tabs -= 1
    ind += 1
    return

def content():
    global ind, output, input
    if input[ind][0] == '"':
        output += input[ind][1:len(input[ind]) - 1]
        ind += 1 
        return
    else:
        xml()

def xml():
    global ind, output, tabs, input, past_tags, need_dash
    if len(input) <= ind: return
    if input[ind][0] == '"':
        output += tabs * "  " + 'text: '
    if input[ind][0] == '/':
        ind += 1
        tabs -= 1
    else:
        head_tag()
        content()
        tail_tag()
        past_tags = past_tags[:-1]
        need_dash = False
    xml()

def rebuild_tags(tags):
    result = []
    for tag in tags:
        attrs = re.findall(r"[^\s]+ *\= *\".*?\"", tag)
        for attr in attrs:
            tmp = attr.replace("=", " ").split()
            tag = tag.replace(attr, "<" + tmp[0] + ">" + tmp[1] + "</" + tmp[0] + ">")
        if tag[-2] == '/':
            tag = tag[0:-2] + ">" + "</" + re.search(r"<[^ ]+", tag).group()[1:] + ">"
        result.append(tag)
    return result

def xml_to_yaml_rec(input_file_name, output_file_name):
    global input
    input_file = open(input_file_name, 'r', encoding = "utf-8")
    output_file = open(output_file_name,'w', encoding = "utf-8")

    input = input_file.read() 

    between = re.findall(r">.*<\/", input)
    for text in between: input = input.replace(text, '>"' + text[1:len(text) - 2] + '"</')

    to_change = re.findall(r"<\/?.+\=.*>", input)
    changed = rebuild_tags(to_change)
    for i in range(len(to_change)): input = input.replace(to_change[i], changed[i])
    
    input = input.strip("<>     \n").replace(">", "<").split("<")
    input = [s.strip() for s in input if s.strip("  \n")]

    xml()
    q = "\n".join(line for line in output.splitlines() if line.strip())
    output_file.write(q)

xml_to_yaml_rec("input.xml", "output3.yml")
