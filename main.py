import random
import string
import customtkinter as ctk
import pyperclip

def generate_password(length, use_digits, use_letters, use_specials):
    characters = ''
    if use_digits:
        characters += string.digits
    if use_letters:
        characters += string.ascii_letters
    if use_specials:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate():
    global password_window
    try:
        length = int(length_slider.get())
        use_digits = digits_var.get()
        use_letters = letters_var.get()
        use_specials = specials_var.get()
        password = generate_password(length, use_digits, use_letters, use_specials)
        
        if password_window is not None:
            password_window.destroy()
        
        show_password_window(password)
    except ValueError as e:
        result_label.configure(text=str(e))

def show_password_window(password):
    global password_window
    password_window = ctk.CTkToplevel(app)
    password_window.title("Сгенерированный пароль")
    password_window.geometry("300x100")
    password_window.resizable(False, False)
    password_window.attributes("-topmost", True)
    
    password_label = ctk.CTkLabel(password_window, text=password, font=("Arial", 14))
    password_label.pack(pady=10)
    
    copy_button = ctk.CTkButton(password_window, text="Скопировать", command=lambda: copy_to_clipboard(password))
    copy_button.pack(pady=5)

def copy_to_clipboard(password):
    pyperclip.copy(password)

def update_length_label(value):
    length_label.configure(text=f"Длина пароля: {int(value)}")

def apply_color_theme():
    color = "blue"
    app.configure(fg_color=color)
    length_label.configure(fg_color=color)
    length_slider.configure(button_color=color)
    digits_check.configure(fg_color=color)
    letters_check.configure(fg_color=color)
    specials_check.configure(fg_color=color)
    generate_button.configure(fg_color=color)
    result_label.configure(fg_color=color)
    
    if password_window is not None:
        for widget in password_window.winfo_children():
            widget.configure(fg_color=color)

def toggle_theme():
    if theme_var.get():
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

# Настройка окна
app = ctk.CTk()
app.title("Генератор паролей")
app.geometry("400x400")
app.resizable(False, False)

password_window = None

# Поле для ввода длины пароля
length_label = ctk.CTkLabel(app, text="Длина пароля: 25")
length_label.pack(pady=10)
length_slider = ctk.CTkSlider(app, from_=1, to=50, number_of_steps=49, command=update_length_label)
length_slider.set(25)  # Установим начальное значение
length_slider.pack(pady=10)

# Чекбоксы для выбора параметров
digits_var = ctk.BooleanVar(value=True)
letters_var = ctk.BooleanVar(value=True)
specials_var = ctk.BooleanVar(value=True)

checkbox_frame = ctk.CTkFrame(app)
checkbox_frame.pack(pady=10)

digits_check = ctk.CTkCheckBox(checkbox_frame, text="Цифры", variable=digits_var)
digits_check.grid(row=0, column=0, padx=5)
letters_check = ctk.CTkCheckBox(checkbox_frame, text="Буквы", variable=letters_var)
letters_check.grid(row=0, column=1, padx=5)
specials_check = ctk.CTkCheckBox(checkbox_frame, text="Спецсимволы", variable=specials_var)
specials_check.grid(row=0, column=2, padx=5)

# Кнопка для генерации пароля
generate_button = ctk.CTkButton(app, text="Сгенерировать пароль", command=on_generate)
generate_button.pack(pady=20)

# Метка для отображения результата
result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=10)

# Галочка для смены темы
theme_var = ctk.BooleanVar(value=True)
theme_check = ctk.CTkCheckBox(app, text="Чёрная тема", variable=theme_var, command=toggle_theme)
theme_check.pack(pady=10)

# Установим начальную тему
toggle_theme()

# Запуск приложения
app.mainloop()