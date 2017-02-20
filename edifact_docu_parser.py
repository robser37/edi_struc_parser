import urllib

plain_text = open('edifact_structure.txt')
# to track if group is currently open (True) or closed (False)
tracker = {0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False}
# to stack to track group names
groups = []

for line in plain_text:
    if 'DETAIL' not in line and len(line.split()) > 0:
        struc_str = (line[63:70])[::-1]
        group = ''
        segment = ''
        ind_lvl = '  '
        if 'Segment group' in line:
            group_str = line[17:33].rsplit()
            group = group_str[1] + "_" + group_str[2]
        else:
            segment = line[7:10]
        if struc_str != "\n" and len(struc_str) > 0:
            struc_str = (struc_str.replace("-", "")).rstrip()

            max_indent = len(struc_str) - 1
            while len(struc_str) != 0:
                indent = len(struc_str) - 1
                chr = struc_str[-1]
                struc_str = struc_str[:-1]
                if chr == '|':
                    if len(segment.split()) == 0 or indent != max_indent:
                        break
                    print ind_lvl * (indent + 1) + segment
                    break
                elif chr == '+' and tracker.get(indent) == True:
                    if indent == max_indent:
                        print ind_lvl * (indent + 1) + segment
                        print ind_lvl * indent + groups.pop()
                    else:
                        print ind_lvl * indent + groups.pop()
                    tracker[indent] = False
                elif chr == '+' and tracker.get(indent) == False:
                    print ind_lvl * indent + group
                    groups.append(group)
                    tracker[indent] = True
        else:
            if len(segment) > 0:
                print segment
