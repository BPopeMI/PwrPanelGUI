import tkinter as tk
from tkinter import scrolledtext
import subprocess

class PowerPanelGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PwrPanel GUI by BPopeMI")

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.status_button = tk.Button(self.frame, text="Get UPS Status", command=self.get_status)
        self.status_button.pack(pady=5)

        self.text_area = scrolledtext.ScrolledText(self.frame, width=50, height=15)
        self.text_area.pack(pady=5)

    def get_status(self):
        try:
            result = subprocess.run(['sudo', 'pwrstat', '-status'], capture_output=True, text=True, check=True)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.INSERT, result.stdout)
        except subprocess.CalledProcessError as e:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.INSERT, f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PowerPanelGUI(root)
    root.mainloop()
