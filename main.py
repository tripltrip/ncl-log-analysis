from datetime import datetime, timezone

#raw hex bytes are here
arr = []

sources = []
destinations = []
timestamps = []
total_bytes_transferred = 0
byte_date_log = {}

for i in range(len(arr) / 16):
    sourceip = ""
    destinationip = ""
    timestamp = ""
    bytenumber = 0
    
    #concatenate source ip
    for j in range(3):
        sourceip = sourceip + str(int(arr[0])) + "."
        arr.remove(arr[0])
    sourceip = sourceip + str(int(arr[0]))
    arr.remove(arr[0])
    sources.append(sourceip)
    
    #concatenate destination ip
    for k in range(3):
        destinationip = destinationip + str(int(arr[0])) + "."
        arr.remove(arr[0])
    destinationip = destinationip + str(int(arr[0]))
    arr.remove(arr[0])
    destinations.append(destinationip)
    
    #create timestamp
    timestamp = int.from_bytes(arr[0:4])
    del arr[0:4]
    timestamp = str(datetime.fromtimestamp(timestamp, tz=timezone.utc))[:11]
    
    #concatenate byte amt
    byteint = int.from_bytes(arr[0:4])
    del arr[0:4]
    total_bytes_transferred += byteint
    
    if timestamp in byte_date_log:
        byte_date_log[timestamp] = byte_date_log[timestamp] + byteint
    else:
        byte_date_log[timestamp] = byteint
 

bytecheck = 0
#print dated entries sorted by byte size, one of the checks on ncl exercise
print(dict(sorted(byte_date_log.items(), key=lambda item: item[1], reverse=True)))
for num in list(byte_date_log.values()):
    bytecheck += num

#check if all bytes match up, if not check the for loop
if bytecheck == total_bytes_transferred:
    print("byte check pass")
else:
    print("byte check fail")
