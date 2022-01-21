import psutil
import subprocess
import argparse


def cpu_test():

        parser = argparse.ArgumentParser(description='Get CPU usage per seconds')

        parser.add_argument('-t', '--time',
                        type=int, default=4, help='Example: python cpu_test -t 4')

        parser.add_argument('-p', '--package',
                        type=int, help='Example: python -p mongodb')

        parser.add_argument('-e', '--exec',
                        type=int, help='Example: python -a mongod')

        parser.add_argument('-k', '--kill',
                        type=int, help='Example: python -k mongod')

        parser.add_argument('-r', '--remove',
                        type=int, help='Example: python -r mongodb')

        args = parser.parse_args()

        time = args.time
        package = args.package
        exec = args.exec
        kill = args.kill

        cpu_before = psutil.cpu_percent(time)

        try:
            subprocess.check_call(f"sudo apt -y install {package}", shell=True)
        except subprocess.CalledProcessError:
            
            cpu_after = psutil.cpu_percent(time)
            subprocess.check_call(f"{exec} &", shell=True)
            cpu_open = psutil.cpu_percent(time)

            subprocess.check_call(f"kill -SIGINT `pgrep {kill}`", shell=True)
            subprocess.check_call("sudo apt-get -y remove {libreoffice}", shell=True)

        print("****************************")
        print(f"CPU of {time} sec. before install: {cpu_before}%")
        print(f"CPU of {time} sec. after install: {cpu_after}%")
        print(f"CPU of {time } sec. after open: {cpu_open}&")

        print("*********TOTAL COMAPRE HERE*******************")

        return cpu_before,cpu_after,cpu_open   


if __name__ == "__main__":
    cpu_test()