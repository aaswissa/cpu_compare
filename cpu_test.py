import psutil
import subprocess
import argparse


def cpu_test():

        parser = argparse.ArgumentParser(description='Time to get CPU per seconds')
        parser.add_argument('-t', '--time',
                        type=int, help='python cpu_test -t 4 => 4 seconds of CPU' )

        args = parser.parse_args()
        time = args.time

        cpu_before = psutil.cpu_percent(time)

        subprocess.check_call("sudo apt -y install libreoffice", shell=True)
        cpu_after = psutil.cpu_percent(time)

        subprocess.check_call("libreoffice &", shell=True)
        cpu_open = psutil.cpu_percent(time)

        subprocess.check_call("killall soffice.bin", shell=True)
        subprocess.check_call("sudo apt-get -y remove libreoffice", shell=True)

        print("****************************")
        print(f"CPU of {time} sec. before install: {cpu_before}%")
        print(f"CPU of {time} sec. after install: {cpu_after}%")
        print(f"CPU of {time } sec. after open: {cpu_open}&")

        return cpu_before,cpu_after,cpu_open   


if __name__ == "__main__":
    cpu_test()