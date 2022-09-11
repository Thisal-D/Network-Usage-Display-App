#check run by app 

from psutil import net_if_stats
import time
import os
import sys

exit = False
try:
    f = open("source/settings/process/reader run by app check.txt","r")
    f.close()
    os.remove("source/settings/process/reader run by app check.txt")
except:
    exit = True

if os.path.exists("source/settings/process/reader run by app.txt"):
    try:
        os.remove("source/settings/process/reader run by app.txt")
        exit = True
    except:
        pass
else:
    exit= True
   
if exit== True:
    sys.exit()

x = 0

#running save 
state_of_program_check_file = open("source/settings/process/running_2.txt","w")
state_of_program_check_file = open("source/settings/process/running_2.txt","r")

needs = []
before_adapters = []
#remove old 
try:
    os.remove("source/settings/process/done.txt")
except:
    pass

print("Adapter Reader Running")

while True:
    adapters = str(net_if_stats().keys()).replace(("dict_keys"),"")\
                        .replace("(","").replace(")","").replace("[","")\
                        .replace("]","").replace(" '","").replace("'","").split(",")

  
    #check process os end tasked ?
    for i in adapters:
        replace_name_list = ["/","\\",":","*","?",'"',"<",">","|"]
        adapter_text = i
        for re in replace_name_list:
            adapter_text = adapter_text.replace(re,"")
        file = "source/settings/process/{}.txt".format(adapter_text)

        if os.path.exists(file):
            try:
                os.remove(file)
                needs.append(i)
            except:
                pass
        else:
            needs.append(i)

        needs = list(needs)

    
        before_adapters = adapters
        for adapter in  needs:
            check = open("source/settings/process/done.txt","w")
            check.close()

            #write adapter name for process
            f = open("source/settings/process/adapters.txt","w")
            f.write(adapter)
            f.close()

            f = open("source/settings/process/proceess run by reader check.txt","w")
            f.close()
            try:
                os.startfile("network info process.exe")
            except:
                os.startfile("network info process.py")

            while True:
                if os.path.exists("source/settings/process/done.txt") or os.path.exists("source/settings/process/proceess run by reader check.txt"):
                    pass
                else:
                    break
        
        needs = []

    try:
        os.remove("source/settings/process/running.txt")
        app_closed = True
    except:
         app_closed = False

    if app_closed == True:
        f = open("source/settings/process/running.txt","w")
        f.close()
        sys.exit()
    time.sleep(0.5)
    


                



