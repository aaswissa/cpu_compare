from tqdm import tqdm
from time import sleep
import psutil

with tqdm(total=100, desc='cpu%', position=1) as cpubar:
    while True:
        cpubar.n=psutil.cpu_percent()
        cpubar.refresh()
        sleep(0.5)