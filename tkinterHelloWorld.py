import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Create main window
root = tk.Tk()
root.title("EXP Calculator")
root.geometry("300x150")

pokemon = tk.StringVar()

def go():
    msg = f'You entered {pokemon.get()}.'
    showinfo(
        title='Information',
        message=msg
    )
    pokemonEntry.delete(0, tk.END)

mainFrame = ttk.Frame(root)
mainFrame.pack(padx=10, pady=10, fill="x", expand=True)

pokemonLabel = ttk.Label(mainFrame, text="Pokemon:")
pokemonLabel.pack(fill='x', expand=True)

pokemonEntry = ttk.Entry(mainFrame, textvariable=pokemon)
pokemonEntry.pack(fill='x', expand=True)
pokemonEntry.focus()

goButton = ttk.Button(mainFrame, text="Go", command=go)
goButton.pack(fill='x', expand=True, pady=10)

root.mainloop()