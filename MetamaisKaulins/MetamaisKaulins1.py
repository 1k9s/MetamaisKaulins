import tkinter as tk
from PIL import Image, ImageTk
import random
from pathlib import Path

metienu_skaits = 0
kopejie_punkti = 0
gajiena_punkti = 0

BASE_DIR = Path(__file__).resolve().parent

def SagatavoAttelu(p):
    # attēlu saraksts
    att = [
        BASE_DIR /"atteli/dice1.png",
        BASE_DIR /"atteli/dice2.png",
        BASE_DIR /"atteli/dice3.png",
        BASE_DIR /"atteli/dice4.png",
        BASE_DIR /"atteli/dice5.png",
        BASE_DIR /"atteli/dice6.png"
    ]

    # nejauši izvēlas attēlu
    attels = Image.open(att[p-1])

    # iegūst attēla izmērus
    w, h = attels.size
    platums = int(w * 0.5)
    augstums = int(h * 0.5)

    # samazina attēla izmēru
    attels = attels.resize((platums, augstums))

    # konvertē attēlu uz Tkinter formātu
    return ImageTk.PhotoImage(attels)

def MetKaulinu():
  metieni = 0
  def Animacija():
      nonlocal metieni
      metieni += 1
      p = random.randint(1, 6)
      if metieni <= 10:
          jkaulins = SagatavoAttelu(p)
          mkaulins.config(image = jkaulins)
          mkaulins.image = jkaulins     # saglabā atsauci uz attēlu
          window.after(100, Animacija)  # atkārto pēc 100 ms
      if metieni == 10:
          #punkti.config(text=f"Punkti: {p}")
          Punkti(p)

  Animacija()  # uzsāk animāciju

def Punkti(p):
    global metienu_skaits
    global gajiena_punkti

    metienu_skaits += 1

    if p == 1:
        gajiena_punkti = 0
    else:
        gajiena_punkti += p

    gajiena.config(text=f"gājiena punkti: {gajiena_punkti}")

def Saglabat():
    global kopejie_punkti, gajiena_punkti

    if gajiena_punkti > 2 :
        kopejie_punkti += gajiena_punkti - 2
        gajiena_punkti = 0
    if kopejie_punkti >= 50:
        RaditRezultatu()

    gajiena.config(text=f"gājiena punkti: {gajiena_punkti}")
    kopejie.config(text=f"kopējie punkti: {kopejie_punkti}")

def RaditRezultatu():
    main_frame.pack_forget()  # paslēpj spēles rāmi
    win_frame.pack(expand=True)

    metieni.config(text=f"metienu skaits: {metienu_skaits}")

def Atkartot():
    global gajiena_punkti, kopejie_punkti, metienu_skaits
    gajiena_punkti = 0
    kopejie_punkti = 0
    metienu_skaits = 0
    gajiena.config(text=f"gājiena punkti: {gajiena_punkti}")
    kopejie.config(text=f"kopējie punkti: {kopejie_punkti}")
    win_frame.pack_forget()
    main_frame.pack(expand=True)
    
# izveido Tkinter logu
window = tk.Tk()
window.title("Metamais kauliņš")
window.geometry("400x300")

p = random.randint(1, 6)

# -------------------- spēles skats --------------------
main_frame = tk.Frame(window)
main_frame.pack(expand=True)

# ielādē un parāda attēlu
foto = SagatavoAttelu(p)
mkaulins = tk.Label(main_frame, image=foto)
mkaulins.pack()

# rāmis tekstam
text_frame = tk.Frame(main_frame)
text_frame.pack(padx=30, pady=30)

# teksti
gajiena = tk.Label(text_frame, text="gājiena punkti: 0")
gajiena.pack(pady=1)

kopejie = tk.Label(text_frame, text="kopējie punkti: 0")
kopejie.pack(pady=1)

# rāmis pogām
pogas_frame = tk.Frame(main_frame)
pogas_frame.pack()

# poga mest
mest = tk.Button(pogas_frame, text="mest", width=12, command=MetKaulinu)
mest.pack(side=tk.LEFT, padx=10)

# poga saglabāt
saglabat = tk.Button(pogas_frame, text="saglabāt", width=12, command=Saglabat)
saglabat.pack(side=tk.RIGHT, padx=10)

# -------------------- uzvaras skats --------------------
win_frame = tk.Frame(window)

uzvaras_teksts = tk.Label(win_frame, text="Tu uzvarēji!", font=("Arial", 20))
uzvaras_teksts.pack(pady=20)

metieni = tk.Label(win_frame)
metieni.pack(pady=10)

atkartot = tk.Button(win_frame, text="atkārtot", command=Atkartot, width=12)
atkartot.pack(pady=10)

window.mainloop()