import xmltodict, json
import sys



if len(sys.argv) > 1 and str(sys.argv[1]) == "help":
  exit("Please add a xml file to the command line")

input_file =  sys.argv[1]

with open(input_file, 'r', encoding="utf-8") as myfile:
    obj = xmltodict.parse(myfile.read())

with open('output.json', 'w', encoding="utf-8") as outfile:
    json.dump(obj, outfile, indent=4, ensure_ascii=False)
