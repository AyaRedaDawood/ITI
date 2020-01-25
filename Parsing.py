import re

log_file_name = "access.log"

def parse(log_file):
    log_file = open(log_file_name)
    lines=log_file.readlines()
    log_file.close()
    allilst =[]
    for line in lines:
          allilst.append(line.split()[0]+" "+line.split()[5][1:] + " " + line.split()[6]+ " " +(' '.join(line.split()[11:-1])))



    for i in range(0,len(allilst)):
           res = allilst[i]
           print (res)

parse(log_file_name)
