import customtkinter as ctk
from tkinter import filedialog, messagebox
from autocorrect_logic import autocorrect_text

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("📝 Autocorrect Tool — Teachable AI")
app.geometry("800x650")

title_label = ctk.CTkLabel(
    app, text="📝 Autocorrect Tool — Teachable AI",
    font=ctk.CTkFont(size=24, weight="bold")
)
title_label.pack(pady=10)

frame_input = ctk.CTkFrame(app)
frame_input.pack(pady=5, fill="x", padx=10)

frame_buttons = ctk.CTkFrame(app)
frame_buttons.pack(pady=5, fill="x", padx=10)

frame_output = ctk.CTkFrame(app)
frame_output.pack(pady=5, fill="x", padx=10)

# Input text
input_textbox = ctk.CTkTextbox(frame_input, width=760, height=150)
input_textbox.pack(pady=5)

# Uploaded file label
uploaded_file_label = ctk.CTkLabel(frame_input, text="No file uploaded")
uploaded_file_label.pack(pady=2)

# Output text
output_textbox = ctk.CTkTextbox(frame_output, width=760, height=200)
output_textbox.pack(pady=5)

def load_text_file():
    path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if path:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        input_textbox.delete("1.0", "end")
        input_textbox.insert("end", content)
        uploaded_file_label.configure(text=f"📂 Uploaded: {path}")

def save_text_file(content):
    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

def correct_text():
    user_input = input_textbox.get("1.0", "end").strip()
    if not user_input:
        messagebox.showerror("Error", "Please enter or load some text!")
        return

    corrected = autocorrect_text(user_input)

    # Find changes
    original_words = user_input.split()
    corrected_words = corrected.split()
    changes = []
    for orig, corr in zip(original_words, corrected_words):
        if orig != corr:
            changes.append(f"{orig} → {corr}")

    output_textbox.delete("1.0", "end")
    output_textbox.insert(
        "end",
        f"Original:\n{user_input}\n\nCorrected:\n{corrected}\n\nChanges:\n"
    )
    output_textbox.insert("end", "\n".join(changes) if changes else "No changes!")

def copy_text():
    content = output_textbox.get("1.0", "end").strip()
    app.clipboard_clear()
    app.clipboard_append(content)

def clear_output():
    output_textbox.delete("1.0", "end")

def convert_txt():
    """Load a text file's content into the input textbox."""
    path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if path:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        input_textbox.delete("1.0", "end")
        input_textbox.insert("end", content)
        uploaded_file_label.configure(text=f"📂 Uploaded: {path}")

# Buttons
ctk.CTkButton(
    frame_buttons, text="Convert TXT",
    command=convert_txt, width=140
).pack(side="left", padx=5)

ctk.CTkButton(
    frame_buttons, text="Correct Text",
    command=correct_text, width=140
).pack(side="left", padx=5)

ctk.CTkButton(
    frame_buttons, text="Copy Output",
    command=copy_text, width=140
).pack(side="left", padx=5)

ctk.CTkButton(
    frame_buttons, text="Clear Output",
    command=clear_output, width=140
).pack(side="left", padx=5)

ctk.CTkButton(
    frame_buttons, text="Save Output",
    command=lambda: save_text_file(output_textbox.get("1.0", "end").strip()), width=140
).pack(side="left", padx=5)

app.mainloop()
# autocorrect_tool.py