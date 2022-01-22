import psutil
import subprocess
import argparse



def cpu_test():

        parser = argparse.ArgumentParser(description='Get CPU usage per seconds')

        parser.add_argument('-t', '--time',
                        type=int, default=4, help='Example: python cpu_test -t 4')

        parser.add_argument('-p', '--package',
                        type=str, help='Example: python -p mongodb')

        parser.add_argument('-e', '--exec',
                        type=str, help='Example: python -a mongod')

        args = parser.parse_args()

        time = args.time
        package = args.package
        exec = args.exec


        cpu_before = psutil.cpu_percent(time)

        try:
            subprocess.check_call(f"sudo apt -y install {package}", shell=True)
        except subprocess.CalledProcessError:
            print('Failed to install...')
            
        
        cpu_after = psutil.cpu_percent(time)
        subprocess.check_call(f"{exec} &", shell=True)
        cpu_open = psutil.cpu_percent(time)

        try:
            subprocess.check_call(f"sudo apt-get -y remove {package}", shell=True)
        except subprocess.CalledProcessError:
            print('Failed to uninstall...')


        print("****************************")
        print(f"CPU of {time} sec. before install: {cpu_before}%")
        print(f"CPU of {time} sec. after install: {cpu_after}%")
        print(f"CPU of {time} sec. after open: {cpu_open}%")
        print("****************************")

        return cpu_before,cpu_after,cpu_open   


if __name__ == "__main__":
    cpu_test()