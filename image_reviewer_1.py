import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk

class ImageReviewerApp:
    def __init__(self, root, image_folder):
        self.root = root
        self.root.title("Image Reviewer")
        self.image_folder = image_folder
        self.image_files = self.load_images()
        self.current_image_index = 0
        self.remaining_time = 5
        self.waiting_for_type = False  # Flag to check if waiting for type selection

        self.setup_ui()
        self.display_image()
        self.countdown()

    def load_images(self):
        # Load all GIF files from the image_folder
        image_files = [f for f in os.listdir(self.image_folder) if f.lower().endswith('.gif')]
        image_files.sort()
        return image_files

    def setup_ui(self):
        # Image display area
        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        # Progress label
        self.progress_label = tk.Label(self.root, text="")
        self.progress_label.pack()

        # Remaining time label
        self.time_label = tk.Label(self.root, text="Time remaining: 5")
        self.time_label.pack()

        # Extend time button
        self.extend_button = tk.Button(self.root, text="Extend 5 seconds", command=self.extend_time)
        self.extend_button.pack()

        # Type selection
        type_frame = tk.Frame(self.root)
        type_frame.pack(pady=5)
        tk.Label(type_frame, text="Type:").pack(side=tk.LEFT)
        self.type_var = tk.StringVar()
        type_options = ['E', 'A', 'U*', 'A+E', 'N', 'B']
        self.type_combobox = ttk.Combobox(type_frame, textvariable=self.type_var, values=type_options)
        self.type_combobox.pack(side=tk.LEFT)
        self.type_combobox.bind('<<ComboboxSelected>>', self.type_selected)

        # 'Others' entry field
        tk.Label(type_frame, text="Others:").pack(side=tk.LEFT)
        self.others_var = tk.StringVar()
        self.others_entry = tk.Entry(type_frame, textvariable=self.others_var)
        self.others_entry.pack(side=tk.LEFT)
        self.others_var.trace_add('write', self.others_written)

        # Remarks input
        tk.Label(self.root, text="Remarks:").pack()
        self.remarks_text = tk.Text(self.root, height=4, width=50)
        self.remarks_text.pack()

        # Control buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)
        self.next_button = tk.Button(button_frame, text="Next", command=self.next_image)
        self.next_button.pack(side=tk.LEFT, padx=5)
        self.quit_button = tk.Button(button_frame, text="Quit", command=self.quit_app)
        self.quit_button.pack(side=tk.LEFT, padx=5)

        # Keyboard bindings
        self.root.bind('<KeyPress-e>', self.key_extend_time)
        self.root.bind('<KeyPress-E>', self.key_extend_time)
        self.root.bind('<KeyPress-n>', self.key_next_image)
        self.root.bind('<KeyPress-N>', self.key_next_image)
        self.root.bind('<KeyPress-q>', self.key_quit_app)
        self.root.bind('<KeyPress-Q>', self.key_quit_app)

    def display_image(self):
        if self.current_image_index >= len(self.image_files):
            messagebox.showinfo("Info", "No more images.")
            self.root.quit()
            return
        image_file = self.image_files[self.current_image_index]
        image_path = os.path.join(self.image_folder, image_file)
        self.progress_label.config(text=f"Image {self.current_image_index+1} of {len(self.image_files)}")
        try:
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo  # keep a reference
        except Exception as e:
            messagebox.showerror("Error", f"Cannot open image {image_file}\n{e}")
            self.next_image()

    def countdown(self):
        if self.remaining_time > 0:
            self.time_label.config(text=f"Time remaining: {self.remaining_time}")
            self.remaining_time -= 1
            self.root.after(1000, self.countdown)
        else:
            # Timer has ended
            if self.type_var.get() or self.others_var.get():
                # Type is selected, proceed to next image
                self.next_image()
            else:
                # Type not selected, wait for user input
                self.waiting_for_type = True
                self.time_label.config(text="Time's up! Please select the type to continue.")
                self.extend_button.config(state=tk.DISABLED)
                self.next_button.config(state=tk.DISABLED)

    def extend_time(self):
        self.remaining_time += 5
        self.time_label.config(text=f"Time remaining: {self.remaining_time}")

    def next_image(self, event=None):
        self.save_input()
        self.current_image_index += 1
        if self.current_image_index >= len(self.image_files):
            messagebox.showinfo("Info", "No more images.")
            self.root.quit()
            return
        self.remaining_time = 5
        self.waiting_for_type = False
        self.extend_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.NORMAL)
        self.display_image()
        self.countdown()

    def quit_app(self, event=None):
        self.root.quit()

    def save_input(self):
        image_file = self.image_files[self.current_image_index]
        # Remove the .gif extension
        image_file_name = os.path.splitext(image_file)[0]
        type_input = self.type_var.get()
        others_input = self.others_var.get()
        if others_input:
            type_input = others_input
        remarks_input = self.remarks_text.get("1.0", tk.END).strip()
        try:
            with open('output14.txt', 'a', encoding='utf-8') as f:
                f.write(f"{image_file_name}\t{type_input}\t{remarks_input}\n")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data for {image_file}\n{e}")
        self.type_var.set('')
        self.others_var.set('')
        self.remarks_text.delete('1.0', tk.END)

    def type_selected(self, event):
        self.others_var.set('')
        if self.waiting_for_type:
            # User selected type after timer ended
            self.waiting_for_type = False
            self.next_image()

    def others_written(self, *args):
        if self.others_var.get():
            self.type_var.set('')
            if self.waiting_for_type:
                # User entered 'Others' after timer ended
                self.waiting_for_type = False
                self.next_image()

    def key_extend_time(self, event):
        # Ignore key presses when focus is on Entry or Text widgets
        if isinstance(self.root.focus_get(), (tk.Entry, tk.Text)):
            return
        self.extend_time()

    def key_next_image(self, event):
        # Ignore key presses when focus is on Entry or Text widgets
        if isinstance(self.root.focus_get(), (tk.Entry, tk.Text)):
            return
        self.next_image()

    def key_quit_app(self, event):
        # Ignore key presses when focus is on Entry or Text widgets
        if isinstance(self.root.focus_get(), (tk.Entry, tk.Text)):
            return
        self.quit_app()

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    image_folder = filedialog.askdirectory(title="Select Image Folder")
    if not image_folder:
        print("No folder selected.")
        sys.exit(1)
    root.deiconify()
    app = ImageReviewerApp(root, image_folder)
    root.mainloop()

