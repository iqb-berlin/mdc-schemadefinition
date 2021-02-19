import xmltodict, json
import sys



if len(sys.argv) > 1 and str(sys.argv[1]) == "help":
  exit("Please add a input xml file to the command line [optional] name of output file")

input_file =  sys.argv[1]
output_file = sys.argv[2] if len(sys.argv) > 2 and str(sys.argv[2]) else "output.json"

with open(input_file, 'r', encoding="utf-8") as myfile:
    obj = xmltodict.parse(myfile.read())



with open(output_file, 'w') as outfile:
    json.dump(obj, outfile, indent=4, ensure_ascii=False)
