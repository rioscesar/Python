import threading

class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

x = BuckysMessenger(name="Send out messages")
y = BuckysMessenger(name="Receive messages")

y.start()
x.start()




