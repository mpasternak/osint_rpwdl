import time
from datetime import timedelta
import os
from osint_rpwdl.const import MAX_UID

def get_cnt():
    return len(list(os.walk("results"))[0][2])

t_start = time.time()
cnt_start = get_cnt()

while True:
    cur_cnt = get_cnt()
    n_pages = cur_cnt - cnt_start
    span = time.time() - t_start
    pages_per_sec =n_pages/span
    print("%i per %f sec = %f pages / sec" % (n_pages, span,pages_per_sec ))
    print("Downloaded %i of %i, that's %.2f %%" % (cur_cnt, MAX_UID, cur_cnt*100/MAX_UID))
    if pages_per_sec > 0:
        time_left = (MAX_UID-cur_cnt) / pages_per_sec
        print("I need %s more seconds" % timedelta(seconds=time_left))
    time.sleep(10)
