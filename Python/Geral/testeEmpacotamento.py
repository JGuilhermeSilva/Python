import tkinter as tk

root = tk.Tk()

# 1. tk.TOP (Padrão) - Empacota no topo
entry1 = tk.Button(root, text='top')
entry1.pack(side=tk.TOP, pady=5)

# 2. tk.BOTTOM - Empacota na parte inferior
entry2 = tk.Button(root, text='BOTTOM')
entry2.pack(side=tk.BOTTOM, pady=5)

# 3. tk.LEFT - Empacota no lado esquerdo
entry3 = tk.Button(root, text='LEFT')
entry3.pack(side=tk.LEFT, padx=5)

# 4. tk.RIGHT - Empacota no lado direito
entry4 = tk.Button(root, text='RIGHT')
entry4.pack(side=tk.RIGHT, padx=5)

root.mainloop()