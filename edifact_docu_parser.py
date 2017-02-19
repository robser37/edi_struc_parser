import urllib

page = open('edifact_structure.txt')

tracker = {0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False}

def isOpen(indent):
    return tracker.get(indent)


# print "result: " + str(isOpen(0))
# print "result: " + str(isOpen(1))



for line in page:
    if 'DETAIL' not in line and len(line.split()) > 0:
        struc_str = (line[63:70])[::-1]
        if struc_str != "\n" and len(struc_str) > 0:
            new = (struc_str.replace("-", "")).rstrip()
            struc_list = list(new)
            print new
            #print "curr_sym: " + new
            # print "A----------------------"
            while len(struc_list) != 0:
                indent = len(struc_list) - 1
                sym = struc_list.pop()
                # print "line: " + new
                # print "indent: " + str(indent)
                # print "sym: " + sym
                if sym == '+':
                    if isOpen(indent):
                        print "close"
                        tracker[indent] = False
                    else:
                        print "open"
                        tracker[indent] = True
                # stop = raw_input()
                # print tracker
            # print "Z----------------------"



        # if len(struc_str) > 0:
        #     indent = 0
        #     last_sym = '0'
        #
        #     for sym in struc_str:
        #         if sym == '+' and indent == 0 and open == False:
        #             print 'group-open'
        #             open = True
        #
        #         elif last_sym == '|' and sym == '+' and open == True
        #             print 'sub-group-open'
        #
        #
        #
        #
        #
        #
        #
        #         elif sym == '+' and indent == 0 and open == True:
        #             print 'group-close'
        #             open = False
        #         # elif sym == '+' and group_open == True:
        #         #     print 'group-close'
        #         last_sym = sym
