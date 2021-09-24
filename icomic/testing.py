import os
import datetime as dt
import time

now = dt.datetime.now()
ago = now-dt.timedelta(minutes=10)

for root, dirs,files in os.walk('.snakemake/log/'):  
    for fname in files:
        path = os.path.join(root, fname)
        st = os.stat(path)    
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            print(path)
            
            file = open(path, 'r')
            while 1:
                where = file.tell()
                line = file.readline()
                if not line:
                    time.sleep(1)
                    file.seek(where)
                else:
                    print(line)
                    
    