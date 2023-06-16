from tkinter import *
window = Tk()
window.geometry("800x400")
window.title("Decode/Code")
Input = Entry()
Input.pack()
KeyInput = Entry()
KeyInput.pack()
Return = Entry()
Return.pack()

def code():
    message = Input.get()
    key = KeyInput.get()
    List = list(message)
    Sypher = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26," ":" "}
    message_decode = []
    index = 0
    answer = []
    for Item in List:
        message_decode.append(Sypher[Item])
    er = list(str(key))
    for lag in message_decode:
        if lag == ' ':
            answer.append(' ')
        try:
            lag+=int(er[index])
        
        except IndexError:
            try:
                index = 0
                lag+=int(er[index])

            except TypeError:
                continue
        except TypeError:
            continue
        index+=1
        answer.append(lag)
    window.clipboard_append(answer)
    print(f"закодировано без ключа {message_decode}")
    print(f"закодировано с ключем {answer}")
def encode():
    Return.insert(0," ")
    message = Return.get()
    key = KeyInput.get()
    List = message.split(",")
    res = ""
    Decode_message = []
    EnSypher = {" 1": "a", " 2": " b", " 3": "c", " 4": "d", " 5": "e", " 6": "f", " 7": "g", " 8": "h", " 9": "i",
                " 10": "j", " 11": "k", " 12": "l",
                " 13": "m", " 14": "n", " 15": "o", " 16": "p", " 17": "q", " 18": "r", " 19": "s", " 20": "t",
                " 21": "u", " 22": "v", " 23": "w",
                " 24": "x", " 25": "y", " 26": "z", ' \' \'':None }
    KeyList = list(key)
    index = 0
    for item in List:
        try:

            item=int(item)-int(KeyList[index])
            if int(item)<0:
                item+=26
            index+=1
            Decode_message.append(item)

        except ValueError:
            Decode_message.append(item)
        except IndexError:
            index=0
            item=int(item)-int(KeyList[index])
            if int(item)<0:
                item+=26
            index+=1
            Decode_message.append(item)


    for AHAHAHAHAHA in Decode_message:
        try:
            res+=EnSypher[" "+str(AHAHAHAHAHA)]
        except KeyError:
            try:
                res+=EnSypher["  "+str(AHAHAHAHAHA)]
            except KeyError:
                res+=" "
            except TypeError:
                res+=" "
    print(res)
def enncode():
    EnSypher = {" 1": "a", " 2": " b", " 3": "c", " 4": "d", " 5": "e", " 6": "f", " 7": "g", " 8": "h", " 9": "i", " 10": "j", " 11": "k", " 12": "l",
              " 13": "m", " 14": "n", " 15": "o", " 16": "p", " 17": "q", " 18": "r", " 19": "s", " 20": "t", " 21": "u", " 22": "v", " 23": "w",
              " 24": "x", " 25": "y", " 26": "z", ' ': " "}
    Return.insert(0, " ")
    Cipher11 = Return.get()
    Decode = Cipher11.split(",")
    res = ""
    for Thing2 in Decode:
        try:
            res+=EnSypher[Thing2]
        except KeyError:
            res+=" "
    print(f"раскодировано {res}")
button = Button(text="Просто закодировать",command=code)
button.pack()
button2 = Button(text="раскодировать",command=enncode)
button2.pack()
button3 = Button(text="Раскодировать с ключем",command=encode)
button3.pack()
window.mainloop()