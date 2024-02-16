import os

import settings

try:
    import fastapi
except ImportError:
    print("\033[31mError: \033[0mMissing dependencies.")
    Install = input("Would you like to install the dependencies? (y/n)    ")
    if Install.lower() == "y":
        os.system('pip install fastapi "uvicorn[standard]"')
        print("-" * 10)
        print("Dependencies installed.")
        try:
            import fastapi
        except ImportError:
            print(
                "\033[31mError: \033[0mDependencies didn't install properly please check console for more information")
            exit(1)

import argparse


def main():
    parser = argparse.ArgumentParser(
        prog='SCP: Online API',
        description='This is the backend work for the SCP: Online Plugin'
    )
    parser.add_argument("-H", '--Host', type=str,
                        help='The host of the server')
    parser.add_argument("-p", '--Port', type=int,
                        help='The Port of the server')
    args = parser.parse_args()
    settings._PORT = args.Port
    settings._HOSTNAME = args.Host
    os.system("uvicorn main:app")

if __name__ == "__main__":
    main()