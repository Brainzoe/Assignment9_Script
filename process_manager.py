#! /usr/bin/python3

import psutil

def list_all_processes():
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_info']):
        print(f"PID: {proc.info['pid']}  Name: {proc.info['name']}  CPU%: {proc.info['cpu_percent']}  Memory: {proc.info['memory_info'].rss / (1024 * 1024)} MB")

def kill_process(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f"Process {pid} terminated.")
    except psutil.NoSuchProcess:
        print(f"No process with PID {pid} found.")

def search_process_by_name(name):
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if name in proc.info['name']:
            print(f"PID: {proc.info['pid']}  Name: {proc.info['name']}")

def process_details(pid):
    try:
        process = psutil.Process(pid)
        print(f"Process ID: {pid}")
        print(f"Command: {process.cmdline()}")
        print(f"Status: {process.status()}")
        print(f"CPU usage: {process.cpu_percent()}%")
        print(f"Memory usage: {process.memory_info().rss / (1024 * 1024)} MB")
    except psutil.NoSuchProcess:
        print(f"No process with PID {pid} found.")

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. List all processes")
        print("2. Kill a specific process")
        print("3. Search for processes by name")
        print("4. Display detailed information about a process")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_all_processes()
        elif choice == "2":
            pid_to_kill = int(input("Enter the PID of the process to kill: "))
            kill_process(pid_to_kill)
        elif choice == "3":
            process_name = input("Enter the name of the process to search: ")
            search_process_by_name(process_name)
        elif choice == "4":
            pid_to_show = int(input("Enter the PID of the process: "))
            process_details(pid_to_show)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

