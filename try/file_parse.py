file_list = ["multicast_cc_l2_pi.json",
"multicast_cc_l2_ipv6_pi.json",]

cmd_tmp = "cp " + "{"

for jsonfile in file_list:
    cmd_tmp = cmd_tmp + jsonfile + ","

cmd_tmp = cmd_tmp.replace(cmd_tmp[0:],cmd_tmp[0:len(cmd_tmp)-1] )
cmd_tmp = cmd_tmp + "}" + " temp/"

print cmd_tmp
