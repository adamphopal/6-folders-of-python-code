import threading
import time

class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, "a")
        f.write(self.text + '\n')
        f.close()
        time.sleep(2)
        print("Finished Background file write to " + self.out)
        

def Main():
    message = input("Enter your email address and name, seperated by a comma(hamimphopal@yahoo.com , hamim phopal):" )
    background = AsyncWrite(message, 'emails.txt')
    background.start()
    message = input("Enter a new tiny link: ")
    background = AsyncWrite(message, 'schedule.txt')
    background.start()
    print("The program can continue while it writes in another thread")
    print("100 + 400 = ", 100+400)

    background.join()
    print("Waited until thread was complete")

if __name__ == '__main__':
    Main()
