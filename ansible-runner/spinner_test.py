from halo import Halo
import time

def process_command():
    time.sleep(5)  # Simulate a long-running command

spinner = Halo(text='Processing...', spinner='dots')  # You can change the spinner style
spinner.start()
process_command()  # Replace this with your command processing
spinner.stop()
print('Done!')
