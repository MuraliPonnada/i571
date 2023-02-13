import re
import sys
import json

def parse(inp):
    tokens = re.findall(r'\b\w+\b|[{};:^#]', inp)
    pos = 0
    result = []
    i=0
    # print(tokens)

    def parse_declaration():
        nonlocal pos
        if tokens[pos] == 'var':
            pos += 1
            var_name = tokens[pos]
            if var_name in ['number', 'string', 'record']:
                sys.exit("Error: expecting 'id' but got '"+var_name+"'")
            pos += 1
            if tokens[pos] == ':':
                pos += 1
                var_type = parse_type()
                result.append([var_name, var_type])
            else:
                sys.exit("Error: Either Missing colon ':' or TypeId in the input")
        # try:    
        elif tokens[pos] == ';':
            pos+=1
            if pos < len(tokens)-1:
                parse_declaration()
        else:
            sys.exit("Error: missing 'var")
        # except:
        #     sys.exit("Error: line 32 Input is missing a semi colon ';'")
        
    def parse_record_declaration():
        nonlocal pos
        var_name = tokens[pos]
        if var_name in ['number', 'string', 'record']:
                sys.exit("Error: expecting 'id' but got '"+var_name+"'")
        pos += 1
        # print(pos, tokens[pos], tokens[pos-1])
        if tokens[pos] == ':':
            pos += 1
            var_type = parse_type()
            return [var_name, var_type]
        else:
            sys.exit("Error: field Missing colon ':'")

    def parse_type():
        nonlocal pos
        if tokens[pos] == 'number':
            pos += 1
            if pos>=len(tokens) or tokens[pos]!=";":
                sys.exit("Error: field is missing semi-colon ';'")
            return 'number'
        elif tokens[pos] == 'string':
            pos += 1
            if pos>=len(tokens) or tokens[pos]!=";":
                sys.exit("Error: field is missing semi-colon ';'")
            return 'string'
        elif tokens[pos] == 'record':
            pos += 1
            return parse_record()
        else:
            sys.exit('Error: Invalid type, Input has no type')

    def parse_record():
        nonlocal pos
        record = []
        # try:
        while tokens[pos] != 'end':
            if tokens[pos] == ';':
                pos+=1
            if tokens[pos] == 'end':
                break
            if pos < len(tokens)-1:
                record.append(parse_record_declaration())
        pos += 1
        if record == []:
            sys.exit("Error: Empty record in the Input")
        else:
            return record
        # except:
        #     sys.exit("Error: Invalid Input")

    while pos < len(tokens)-1:
        parse_declaration()

    return result
lines = []
d=[]

# while True:
#     line = input()
#     if line:
#         if "#" in line:
#             h=line.split("#")
#             h=h[0]
#             line = h
#         lines.append(line)
#     else:
#         break
# text = '\n'.join(lines)
# rep = parse(str(text))
# print("line 81---->", rep)

# lines1 = sys.stdin.read()
# for i in range(0,len(lines1)):
#     f1=lines1[i].split('#')
#     print(f1,lines1)
#     lines1[i]=f1[0]
# t1=lines1
# rep1=parse(str(t1))
# print("line 89-->", rep1)

b = sys.stdin.readlines()
# print("line 108")
# print(b)
for i in range(0,len(b)):
    if "\n" in b[i]:
        b[i]=b[i].split('\n')[0]
    if "\t" in b[i]:
        b[i]=b[i].split('\t')[1]
    f=b[i].split('#')
    b[i]=f[0]
    if '.' in b[i]:
        sys.exit("Error: Bad character")
# print("line 113")
# print(b)
# if '.' in b:
#     sys.exit("Error: Bad character")
res1=parse(str(b))
# print(json.dumps(res1,indent=4))
sys.stdout.write(json.dumps(res1,indent=4))

# file1 = open("52-missing-colon.err.txt","r+")
# a=file1.readlines()
# print("line 113")
# print(a)
# for i in range(0,len(a)):
#     f=a[i].split('#')
#     a[i]=f[0]
# print("line 112-->")
# print(a)
# t=''.join(a)
# if '.' in t:
#     sys.exit("Error: Bad character")
# res=parse(str(t))
# print(res)
# import csv
# file2 = open("52-missing-colon.errout.txt","w")
# file2.write(json.dumps(res,indent=4))