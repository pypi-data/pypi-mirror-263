from BCGM_Python import feature_handler, helper, file_mods, encrypt_decrypt

root = None
tk = None
fd = None

try:
    import tkinter as tk
    from tkinter import filedialog as fd

    root = tk.Tk()
    root.withdraw()
except Exception:
    print(
        "Failed to initialize tkinter. File / folder selection will not be gui based."
    )
