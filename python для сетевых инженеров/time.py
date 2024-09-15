from datetime import datetime

import time

def print_current_datetime(ptime=datetime.now()):
    print(f">>> {ptime}")

for i in range(1):
    print('сейчас сделаю')
    time.sleep(1)
    print_current_datetime()
