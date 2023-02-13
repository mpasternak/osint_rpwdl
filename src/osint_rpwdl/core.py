import gzip
import os
import random
import time

import requests

from fake_useragent import UserAgent

from .const import URL_BASE, UID_LENGTH, OUTPUT_DIR, MAX_UID
from .exceptions import CaptchaException
from .util import pbar


def uid_to_str(uid: int):
    return f"%0.{UID_LENGTH}i" % uid

def uid_to_filename(uid: int, fn=None):
    fn = uid_to_str(uid)
    return f"{OUTPUT_DIR}/{fn}.html.gz"
    
def get_page(uid: int, session=None):
    if session is None:
        session = requests
    page = session.get(URL_BASE.format(uid=uid_to_str(uid)))
    if page.status_code == 200:
        if b"Oznaczenie organu: " in page.content:
            gzip.open(uid_to_filename(uid), "wb").write(page.content)
        elif b"CaptchaInputText" in page.content:
            raise CaptchaException(page.content)
        else:
            breakpoint()

def get_everything(min_uid=1, max_uid=MAX_UID):
    lst = list(range(min_uid, max_uid))
    random.shuffle(lst)

    ua = UserAgent()

    session = None
    #t_start = None
    #t_cnt = None

    for uid in pbar(lst):
        if session is None:
            #t_start = time.time()
            #t_cnt = 0
            session = requests.Session()
            user_agent = ua.random
            session.headers.update({'User-Agent': user_agent})

        fn = uid_to_filename(uid)
        #print(f"\n{fn}")
        if os.path.exists(fn):
            continue

        while True:
            try:
                #t_cnt += 1
                #t_ela = time.time() - t_start
                #print("Time elapsed: %f" % t_ela)
                #print("Pages downloaded: %i" % t_cnt)
                #t_time_pages = (t_ela/float(t_cnt))
                #print("Time/pages: %f" % t_time_pages)
                #print("Pages/time: %f" % (float(t_cnt)/t_ela))
                
                #if t_time_pages >= 1.7:
                #    print("Sleeping for 5 secs")
                #    time.sleep(5)
                
                get_page(uid, session=session)
                break
            
            except CaptchaException as exc:
                i = random.randint(1, 10)
                print(f"\nCaptcha detected. Sleeping for {i} seconds")
                time.sleep(i)
                session = None
