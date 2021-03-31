from nptdms import TdmsFile
#  import pandas as pd 
import os
import csv
# comment out includes that aren't needed right now
# import datetime 
# import dateutil.parser
# import numpy 
#


files = os.listdir(r"data/")  #Use raw strings with “r” as a prefix to indicate that special characters should not be evaluated
# print(files)

with open('Surface_Pressures.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(['Time', '2H', '4H', '6H', '8H', '10H', '12H', '14H'])
    for item in files:
        if item.endswith(".tdms"):
            print(item)
            tdms_file = TdmsFile.read(item)
            group = tdms_file["Local Formulas"] #groups are the same as tabs in Excel, channels are the same as columns of data
            channel_2H = group['2H Surface']
            channel_4H = group['4H Surface']
            channel_6H = group['6H Surface']
            channel_8H = group['8H Surface']
            channel_10H = group['10H Surface']
            channel_12H = group['12H Surface']
            channel_14H = group['14H Surface']

            channel_time = group['Time Stamp']
            channel_data_time = channel_time[:]

            channel_data_2H  = channel_2H[:]
            channel_data_4H  = channel_4H[:]
            channel_data_6H  = channel_6H[:]
            channel_data_8H  = channel_8H[:]
            channel_data_10H  = channel_10H[:]
            channel_data_12H  = channel_12H[:]
            channel_data_14H  = channel_14H[:]
            # channel_properties = channel.properties

            # print('file loaded')
            # for group in tdms_file.groups():
            #     print(group)

            # for channel in group.channels():
            #     print(channel)
            # print(f"{'Time' : <20}{'2H' : ^6}{'4H' : ^6}{'6H' : ^6}{'8H' : ^7}{'10H' : ^7}{'12H' : ^7}{'14H' : ^7}")
            for time, item2, item4, item6, item8, item10, item12, item14 in zip(channel_data_time, channel_data_2H, channel_4H, channel_6H, channel_8H, channel_10H, channel_12H, channel_14H):
                
                if str(time)[17:19] == "00":  #only grab the minute    Need to add code later to be able to specify an actual interval

                    # temp = [str(time), item2, item4, item6, item8, item10, item12, item14]
                    # print(f"{str(time)[0:16]: <20}{item2:^6.1f}{item4:^6.1f}{item6:^6.1f}{item8:^7.1f}{item10:^7.1f}{item12:^7.1f}{item14:^7.1f}")
                    newtime = str(time)[0:16]
                    item2 = round(item2, 2)
                    item4 = round(item4, 2)
                    item6 = round(item6, 2)
                    item8 = round(item8, 2)
                    item10 = round(item10, 2)
                    item12 = round(item12, 2)
                    item14 = round(item14, 2)

                    csv_writer.writerow([newtime, item2, item4, item6, item8, item10, item12, item14])


            # print(map(datetime.datetime(), channel_data_time)
            # for time in channel_time:
            #     print(str(time))
            # for time in channel_data_time:
            #     ts = pd.to_datetime(str(time)) 
            #     d = ts.strftime('%Y.%m.%d')
            #     print(d)

    #Pandas dataframe stuff to play with later
            # import pandas as pd 
            # ts = pd.to_datetime(str(date)) 
            # d = ts.strftime('%Y.%m.%d')