os.system("ping 192.168.5.181> ping.txt")
fp=open("ping.txt","r+")
if((fp.readlines()[9].split(",")[2])== ' Lost = 0 (0% loss)'):
    print"***Ping Succeeded.....Host reachable***"
else:
    print "***Ping Failed.....Host not reachable***"
