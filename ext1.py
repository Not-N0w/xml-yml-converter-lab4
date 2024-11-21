import xmltodict
import yaml

def xml_to_yaml_lib(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as input_file:
        xml_dict = xmltodict.parse(input_file.read())

    yaml_data = yaml.dump(xml_dict, default_flow_style=False, allow_unicode=True)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(yaml_data)

xml_to_yaml_lib("input.xml", "output1.yml")