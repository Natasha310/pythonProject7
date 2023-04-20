import os


class player():
    play = bool
    pause = bool
    switcher = range(1, 20)
    quality = []
    def play_on(self):
        self.play = True
    def play_off(self):
        self.play = False

    def pause(self):
        self.pause = True

    def switch_next(self):
        self.switcher += 1

    def change_quality(self):
        self.quality = [240, 360, 720, 1060]


#print(os.getcwd())
#os.mkdir('film_storage')
films = os.chdir('film_storage')
print(os.getcwd())
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = []
letter.split(',')
for l in letter:
    # print(letter)
    alphabet.append(l)

#print(alphabet)
def create_alpha():
    for a in alphabet:
        os.mkdir(str(a))
        continue
        os.chdir('../')




