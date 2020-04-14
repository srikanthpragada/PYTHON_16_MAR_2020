import threading


def print_numbers():
    for n in range(10):
        print(threading.current_thread().name, n)


print("Current Thread : ", threading.current_thread().name)

t = threading.Thread(target=print_numbers)
t.start()

t.join()  # Wait until t is terminated
print("End of Main")