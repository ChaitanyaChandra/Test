from halo import Halo
import time

def process_command():
    EMAIL_TO = ['majorchowdary@gmail.com']
    EMAIL_SPACE = ", "
    msg = EMAIL_SPACE.join(EMAIL_TO)
    print(msg)
    time.sleep(1)

spinner = Halo(text='Processing...', spinner='dots')  # You can change the spinner style
spinner.start()
process_command()  # Replace this with your command processing
spinner.stop()
print('Done!')
