from halo import Halo
import time
from datetime import datetime

# Generate timestamp in desired format
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M')

def process_command():
    EMAIL_TO = ['majorchowdary@gmail.com']
    EMAIL_SPACE = ", "
    msg = EMAIL_SPACE.join(EMAIL_TO)
    print("\n")
    print(msg)
    print(timestamp)
    print("\n")
    # time.sleep(1)

spinner = Halo(text='Processing...', spinner='dots')  # You can change the spinner style
spinner.start()
process_command()  # Replace this with your command processing
spinner.stop()
print('Done!')
