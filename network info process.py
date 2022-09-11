from psutil import net_io_counters
import time
import datetime
import os
import sys

exit = False
try:
    f = open("source/settings/process/proceess run by reader check.txt","r")
    f.close()
    os.remove("source/settings/process/proceess run by reader check.txt")
except:
    exit = True

if exit==True:
    sys.exit()

def convert_bytes(s,type,with_decimal,special_data_type=False):
    if type == "speed" :
        datas = ["B/s","KB/s","MB/s","GB/s","TB/s","PB/s","EB/s"]
    else:
        datas = ["B","KB","MB","GB","TB","PB","EB"]
    index= 0

    if special_data_type not in datas:
        while len(str(int(s))) > 3 and (index+1) < len(datas) :
            s = s /1024
            index += 1
    else:
        while special_data_type != datas[index]:
            s = s /1024
            index += 1
    
    if with_decimal == True:
        val = str(round(s,2)) + " " + datas[index]
    else:
        val = str(int(s)) + " " + datas[index]
    return val

def update_timer(s):
    second_1 = 1
    mintue_1 = 1 * 60
    hour_1   = 1 * 60 * 60
    day_1    = 1 * 60 * 60 * 24
    month_1  = 1 * 60 * 60 * 24 * 30
    year_1   = 1 * 60 * 60 * 24 * 30 * 12

    year   = int(s/year_1)
    month  = int((s-(year*year_1))/month_1)
    day    = int((s-((year*year_1)+(month*month_1)))/day_1)
    hour   = int((s-((year*year_1)+(month*month_1)+(day*day_1)))/hour_1)
    mintue = int((s-((year*year_1)+(month*month_1)+(day*day_1)+(hour*hour_1)))/mintue_1)
    second = int((s-((year*year_1)+(month*month_1)+(day*day_1)+(hour*hour_1)+(mintue*mintue_1)))/second_1)

    times  = [year ,month ,day ,hour ,mintue ,second]

    index_temp_001 = 0
    for time_1 in times :
        times[index_temp_001] = "0"*(2-len(str(time_1)))  + str(time_1)
        index_temp_001 += 1

    if s >= year_1 :
        time_converted =  "{0}y {1}m {2}d {3}h {4}m {5}s".format(times[0],times[1],times[2],times[3],times[4],times[5])
    elif s >= month_1 :
        time_converted =  "{0}m {1}d {2}h {3}m {4}s".format(times[1],times[2],times[3],times[4],times[5])
    elif s >= day_1:
        time_converted =  "{0}d {1}h {2}m {3}s".format(times[2],times[3],times[4],times[5])
    elif s >= hour_1 :
        time_converted =  "{0}h {1}m {2}s".format(times[3],times[4],times[5])
    elif s >= mintue_1 :
        time_converted =  "{0}m {1}s".format(times[4],times[5])
    else:
        time_converted =  "{0}s".format(times[5])
    
    return time_converted

#read adapter name
f = open("source/settings/process/adapters.txt","r")
adapter = f.readline()
f.close()

#remve loop for start another loop
while True:
    try:
        os.remove("source/settings/process/done.txt")
        break
    except:
        pass
#create name for file 
#replace unusable characters for file name
replace_name_list = ["/","\\",":","*","?",'"',"<",">","|"]
adapter_text = adapter
for re in replace_name_list:
    adapter_text = adapter_text.replace(re,"")
process_running_State = open("source/settings/process/{}.txt".format(adapter_text),"w")
process_running_State = open("source/settings/process/{}.txt".format(adapter_text),"r")


print("Process Running For : ",adapter)

#get time now
time_before = float(str(datetime.datetime.now())[17:])
time_reset = False

#saved status
try:
    #open file
    file = open("source/settings/adapters/"+adapter_text+".txt","r")
    saved_data_received = float(file.readline())
    saved_data_sent = float(file.readline())
    saved_data_received_sent  =  float(file.readline())
    time_usage = float(file.readline())
    file.close()
except:
    try:
        file = open("source/settings/adapters/"+adapter_text+"_temp.txt","r")
        saved_data_received = float(file.readline())
        saved_data_sent = float(file.readline())
        saved_data_received_sent  =float(file.readline())
        time_usage = float(file.readline())
        file.close()
    except:
        file = open("source/settings/adapters/"+adapter_text+".txt","w")
        file.close()
        saved_data_received = 0
        saved_data_sent = 0
        time_usage = 0


app_closed_req = False
try:
    #get received bytes now
    before_received_bytes_count = net_io_counters(pernic=True)[adapter].bytes_recv
    before_sent_bytes_count = net_io_counters(pernic=True)[adapter].bytes_sent
except:
    app_closed_req = True


while True:
    time.sleep(1)
    try:
        #get sent bytes now
        now_received_bytes_count = net_io_counters(pernic=True)[adapter].bytes_recv
        now_sent_bytes_count = net_io_counters(pernic=True)[adapter].bytes_sent
        if now_received_bytes_count - before_received_bytes_count < 0:
            app_closed_req = True
    except:
        app_closed_req = True

    #when main app cloed this file can delete 
    #file can delete -> app_closed = True
    try:
        os.remove("source/settings/process/running.txt")
        app_closed = True
    except:
        app_closed = False

    #get info about data usage
    total_received_bytes = saved_data_received + (now_received_bytes_count-before_received_bytes_count)
    total_sent_bytes = saved_data_sent + (now_sent_bytes_count- before_sent_bytes_count)
    total_received_sent_bytes = (total_received_bytes +  total_sent_bytes)

  
    #get time now
    time_now = float(str(datetime.datetime.now())[17:])

    if time_now <= time_before :
        time_now += 1
        time_before -= 59
        time_reset = True

    #get time delay
    time_delay = time_now - time_before
    #total time 
    time_usage += time_delay
    #set time before
    time_before =  time_now
    if time_reset == True:
        time_before -= 1 
        time_reset = False

    #save network info in file
    try:
        file = open("source/settings/adapters/"+adapter_text+"_temp.txt","w")
        file.write(str(total_received_bytes)+ "\n")
        file.write(str(total_sent_bytes)  + "\n")
        file.write(str(total_received_sent_bytes)+ "\n")
        file.write(str(time_usage))
        file.close()
        #open file
        file = open("source/settings/adapters/"+adapter_text+".txt","w")
        file.write(str(total_received_bytes)+ "\n")
        file.write(str(total_sent_bytes)  + "\n")
        file.write(str(total_received_sent_bytes)+ "\n")
        file.write(str(time_usage))
        file.close()
    except:
        pass

    try:
        prt = "Received Usage : {} >> Send Usage : {} >> Total Usage : {} >> Time Usage : {}".\
        format(convert_bytes(total_received_bytes,"none",True,special_data_type=False),convert_bytes(total_sent_bytes,"none",True,special_data_type=False),convert_bytes(total_received_sent_bytes,"none",True,special_data_type=False),update_timer(time_usage))
        print(prt,end="\r")
    except:
        pass

    if app_closed == True or app_closed_req==True :
        f = open("source/settings/process/running.txt","w")
        f.close()
        sys.exit()





            