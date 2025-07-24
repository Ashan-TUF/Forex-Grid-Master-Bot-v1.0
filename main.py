from pathlib import Path

from networkx.algorithms import cycles

from BotManager import Bot
import MetaTrader5 as mt5
from threading import Thread
import time

from tkinter import Canvas, Entry, Button, PhotoImage, messagebox
import customtkinter as ctk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"
icon_path = OUTPUT_PATH / "Main-icon.ico"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

ctk.set_appearance_mode('system')

window = ctk.CTk()
window.configure(bg='#D92C54')
window.iconbitmap(icon_path)
window.title("Forex Grid Master")
window.configure(fg_color="#D92C54")
# window.overrideredirect(True)

window_width = 467
window_height = 959

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = screen_width - window_width
y = (screen_height - window_height) // 2

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

canvas = Canvas(
    window,
    bg="#1F1F1F",
    height=959,
    width=467,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

# border_width = 4
# animation_speed = 0.05
# start_time = time.time()
# border_lines = []


# def rgb_to_hex(r, g, b):
#     return f"#{int(r):02x}{int(g):02x}{int(b):02x}"
#
#
# def get_neon_color(t):
#     cycle = (t * 0.33) % 1.0
#
#     if cycle < 0.33:  # Red to Green
#         progress = cycle / 0.33
#         r = 255 * (1 - progress)
#         g = 255 * progress
#         b = 0
#     elif cycle < 0.66:  # Green to Blue
#         progress = (cycle - 0.33) / 0.33
#         r = 0
#         g = 255 * (1 - progress)
#         b = 255 * progress
#     else:  # Blue to Red
#         progress = (cycle - 0.66) / 0.34
#         r = 255 * progress
#         g = 0
#         b = 255 * (1 - progress)
#
#     return rgb_to_hex(r, g, b)
#
#
# def get_gradient_colors(base_color, steps=10):
#     """Create gradient effect for neon glow"""
#     colors = []
#     # Extract RGB from hex
#     base_r = int(base_color[1:3], 16)
#     base_g = int(base_color[3:5], 16)
#     base_b = int(base_color[5:7], 16)
#
#     for i in range(steps):
#         intensity = (steps - i) / steps
#         r = int(base_r * intensity)
#         g = int(base_g * intensity)
#         b = int(base_b * intensity)
#         colors.append(rgb_to_hex(r, g, b))
#
#     return colors
#
#
# def create_neon_border():
#     for line_id in border_lines:
#         canvas.delete(line_id)
#     border_lines.clear()
#
#     current_time = time.time() - start_time
#     base_color = get_neon_color(current_time)
#     gradient_colors = get_gradient_colors(base_color, 8)
#
#     for i, color in enumerate(gradient_colors):
#         thickness = max(1, 8 - i)
#         offset = i
#
#
#         line_id = canvas.create_line(
#             offset, offset, 467 - offset, offset,
#             fill=color, width=thickness, capstyle='round'
#         )
#         border_lines.append(line_id)
#
#
#         line_id = canvas.create_line(
#             467 - offset, offset, 467 - offset, 959 - offset,
#             fill=color, width=thickness, capstyle='round'
#         )
#         border_lines.append(line_id)
#
#
#         line_id = canvas.create_line(
#             467 - offset, 959 - offset, offset, 959 - offset,
#             fill=color, width=thickness, capstyle='round'
#         )
#         border_lines.append(line_id)
#
#
#         line_id = canvas.create_line(
#             offset, 959 - offset, offset, offset,
#             fill=color, width=thickness, capstyle='round'
#         )
#         border_lines.append(line_id)
#
#
# def animate_border():
#     create_neon_border()
#     window.after(50, animate_border)
#
#
# Thread(target=animate_border).start()

# Your existing UI elements
canvas.create_text(
    37.0,
    85.0,
    anchor="nw",
    text="Login",
    fill="#BFBFBF",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    37.0,
    128.0,
    anchor="nw",
    text="Password",
    fill="#BFBFBF",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    37.0,
    170.0,
    anchor="nw",
    text="Server",
    fill="#BFBFBF",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    37.0,
    335.0,
    anchor="nw",
    text="Symbol",
    fill="#BFBFBF",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    37.0,
    672.0,
    anchor="nw",
    text="Symbol",
    fill="#BFBFBF",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    37.0,
    378.0,
    anchor="nw",
    text="Volume",
    fill="#BFBFBF",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    37.0,
    715.0,
    anchor="nw",
    text="Volume",
    fill="#BFBFBF",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    37.0,
    421.0,
    anchor="nw",
    text="Profit Target",
    fill="#BFBFBF",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    37.0,
    758.0,
    anchor="nw",
    text="Profit Target",
    fill="#BFBFBF",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    37.0,
    464.0,
    anchor="nw",
    text="No. of Level",
    fill="#BFBFBF",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    37.0,
    801.0,
    anchor="nw",
    text="No. of Level",
    fill="#BFBFBF",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    37.0,
    507.0,
    anchor="nw",
    text="No. of Cycle",
    fill="#BFBFBF",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    37.0,
    844.0,
    anchor="nw",
    text="No. of Cycle",
    fill="#BFBFBF",
    font=("Inter", 12 * -1)
)

txtb_login_image = PhotoImage(
    file=relative_to_assets("entry_1.png"))
canvas.create_image(
    282.0,
    92.0,
    image=txtb_login_image
)
txtb_login = Entry(
    bd=0,
    bg="#262626",
    fg="#BFBFBF",
    highlightthickness=0
)
txtb_login.place(
    x=135.0,
    y=74.0,
    width=294.0,
    height=34.0
)

txtb_password_image = PhotoImage(
    file=relative_to_assets("entry_2.png"))
canvas.create_image(
    282.0,
    135.0,
    image=txtb_password_image
)
txtb_password = Entry(
    bd=0,
    bg="#262626",
    fg="#BFBFBF",
    show='*',
    highlightthickness=0
)
txtb_password.place(
    x=135.0,
    y=117.0,
    width=294.0,
    height=34.0
)

txtb_server_image = PhotoImage(
    file=relative_to_assets("entry_3.png"))
canvas.create_image(
    282.0,
    178.0,
    image=txtb_server_image
)
txtb_server = Entry(
    bd=0,
    bg="#262626",
    fg="#BFBFBF",
    highlightthickness=0
)
txtb_server.place(
    x=135.0,
    y=160.0,
    width=294.0,
    height=34.0
)

initialize_button_image = PhotoImage(file=relative_to_assets("initialize_button.png"))
initialize_button_disabled_image = PhotoImage(file=relative_to_assets("initialize_button_disabled.png"))
run_bot_1_button_image = PhotoImage(file=relative_to_assets("run_bot_1_button.png"))
run_bot_2_button_image = PhotoImage(file=relative_to_assets("run_bot_2_button.png"))
run_bot_1_button_disabled_image = PhotoImage(file=relative_to_assets("run_bot_1_button_disable.png"))
run_bot_2_button_disabled_image = PhotoImage(file=relative_to_assets("run_bot_2_button_disable.png"))

initialize_button = Button(
    image=initialize_button_image,
    borderwidth=0,
    bg='#1F1F1F',
    activebackground='#1F1F1F',
    highlightthickness=0,
    cursor='hand2',
    relief="flat"
)
initialize_button.place(x=37.0, y=213.0, width=409.0, height=36.0)

def lock_initialize_section():
    txtb_login.config(state='disabled', disabledbackground="#262626", disabledforeground="#BFBFBF")
    txtb_password.config(state='disabled', disabledbackground="#262626", disabledforeground="#BFBFBF")
    txtb_server.config(state='disabled', disabledbackground="#262626", disabledforeground="#BFBFBF")

    initialize_button.config(
        state='disabled',
        image=initialize_button_disabled_image,
        cursor='arrow'
    )
def initialize():
    try:
        login_text = txtb_login.get().strip()
        password = txtb_password.get().strip()
        server = txtb_server.get().strip()

        if not login_text or not password or not server:
            messagebox.showerror("Error", "Please fill in all login fields")
            return

        login = int(login_text)

        if not mt5.initialize(login=login, password=password, server=server):
            messagebox.showerror("Error", f"Failed to initialize MT5: {mt5.last_error()}")
        else:
            lock_initialize_section()
            messagebox.showinfo("Success", "Successfully connected to MT5")
    except ValueError:
        messagebox.showerror("Error", "Login must be a valid number")
    except Exception as e:
        messagebox.showerror("Error", f"Connection failed: {str(e)}")

initialize_button.config(command=initialize)

txtb_symbol_b1_image = PhotoImage(
    file=relative_to_assets("entry_4.png"))
canvas.create_image(
    282.0,
    343.0,
    image=txtb_symbol_b1_image
)
txtb_symbol_b1 = Entry(
    bd=0,
    bg="#262626",
    fg="#BFBFBF",
    highlightthickness=0
)
txtb_symbol_b1.place(
    x=135.0,
    y=325.0,
    width=294.0,
    height=34.0
)
txtb_volume_b1_image = PhotoImage(
    file=relative_to_assets("entry_6.png"))
canvas.create_image(
    282.0,
    386.0,
    image=txtb_volume_b1_image
)
txtb_volume_b1 = Entry(
    bd=0,
    bg="#262626",
    fg="#BFBFBF",
    highlightthickness=0
)
txtb_volume_b1.place(
    x=135.0,
    y=368.0,
    width=294.0,
    height=34.0
)
txtb_profitTarget_b1_image = PhotoImage(
    file=relative_to_assets("entry_8.png"))
canvas.create_image(
    282.0,
    429.0,
    image=txtb_profitTarget_b1_image
)
txtb_profitTarget_b1 = Entry(
    bd=0,
    bg="#262626",
    fg="#BFBFBF",
    highlightthickness=0
)
txtb_profitTarget_b1.place(
    x=135.0,
    y=411.0,
    width=294.0,
    height=34.0
)
txtb_no_of_level_b1_image = PhotoImage(
    file=relative_to_assets("entry_10.png"))
canvas.create_image(
    282.0,
    472.0,
    image=txtb_no_of_level_b1_image
)
txtb_no_of_level_b1= Entry(
    bd=0,
    bg="#262626",
    fg="#BFBFBF",
    highlightthickness=0
)
txtb_no_of_level_b1.place(
    x=135.0,
    y=454.0,
    width=294.0,
    height=34.0
)
txtb_no_of_cycle_b1_image = PhotoImage(
    file=relative_to_assets("entry_12.png"))
canvas.create_image(
    282.0,
    515.0,
    image=txtb_no_of_cycle_b1_image
)
txtb_no_of_cycle_b1 = Entry(
    bd=0,
    bg="#262626",
    fg="#BFBFBF",
    highlightthickness=0
)
txtb_no_of_cycle_b1.place(
    x=135.0,
    y=497.0,
    width=294.0,
    height=34.0
)

def lock_bot1_section():
    txtb_symbol_b1.config(state='disabled', disabledbackground="#262626", disabledforeground="#BFBFBF")
    txtb_volume_b1.config(state='disabled', disabledbackground="#262626", disabledforeground="#BFBFBF")
    txtb_profitTarget_b1.config(state='disabled', disabledbackground="#262626", disabledforeground="#BFBFBF")
    txtb_no_of_level_b1.config(state='disabled', disabledbackground="#262626", disabledforeground="#BFBFBF")
    txtb_no_of_cycle_b1.config(state='disabled', disabledbackground="#262626", disabledforeground="#BFBFBF")

    run_bot_1_button.config(
        state='disabled',
        image=run_bot_1_button_disabled_image,
        cursor='arrow'
    )

txtb_symbol_b2_image = PhotoImage(
    file=relative_to_assets("entry_5.png"))
canvas.create_image(
    282.0,
    680.0,
    image=txtb_symbol_b2_image
)
txtb_symbol_b2 = Entry(
    bd=0,
    bg="#262626",
    fg="#BFBFBF",
    highlightthickness=0
)
txtb_symbol_b2.place(
    x=135.0,
    y=662.0,
    width=294.0,
    height=34.0
)
txtb_volume_b2_image = PhotoImage(
    file=relative_to_assets("entry_7.png"))
canvas.create_image(
    282.0,
    723.0,
    image=txtb_volume_b2_image
)
txtb_volume_b2 = Entry(
    bd=0,
    bg="#262626",
    fg="#BFBFBF",
    highlightthickness=0
)
txtb_volume_b2.place(
    x=135.0,
    y=705.0,
    width=294.0,
    height=34.0
)
txtb_profitTarget_b2_image = PhotoImage(
    file=relative_to_assets("entry_9.png"))
canvas.create_image(
    282.0,
    766.0,
    image=txtb_profitTarget_b2_image
)
txtb_profitTarget_b2 = Entry(
    bd=0,
    bg="#262626",
    fg="#BFBFBF",
    highlightthickness=0
)
txtb_profitTarget_b2.place(
    x=135.0,
    y=748.0,
    width=294.0,
    height=34.0
)
txtb_no_of_level_b2_image = PhotoImage(
    file=relative_to_assets("entry_11.png"))
canvas.create_image(
    282.0,
    809.0,
    image=txtb_no_of_level_b2_image
)
txtb_no_of_level_b2 = Entry(
    bd=0,
    bg="#262626",
    fg="#BFBFBF",
    highlightthickness=0
)
txtb_no_of_level_b2.place(
    x=135.0,
    y=791.0,
    width=294.0,
    height=34.0
)
txtb_no_of_cycle_b2_image = PhotoImage(
    file=relative_to_assets("entry_13.png"))
canvas.create_image(
    282.0,
    852.0,
    image=txtb_no_of_cycle_b2_image
)
txtb_no_of_cycle_b2 = Entry(
    bd=0,
    bg="#262626",
    fg="#BFBFBF",
    highlightthickness=0
)
txtb_no_of_cycle_b2.place(
    x=135.0,
    y=834.0,
    width=294.0,
    height=34.0
)
def lock_bot2_section():
    txtb_symbol_b2.config(state='disabled', disabledbackground="#262626", disabledforeground="#BFBFBF")
    txtb_volume_b2.config(state='disabled', disabledbackground="#262626", disabledforeground="#BFBFBF")
    txtb_profitTarget_b2.config(state='disabled', disabledbackground="#262626", disabledforeground="#BFBFBF")
    txtb_no_of_level_b2.config(state='disabled', disabledbackground="#262626", disabledforeground="#BFBFBF")
    txtb_no_of_cycle_b2.config(state='disabled', disabledbackground="#262626", disabledforeground="#BFBFBF")

    run_bot_2_button.config(
        state='disabled',
        image=run_bot_2_button_disabled_image,
        cursor='arrow'
    )

logo = PhotoImage(
    file=relative_to_assets("logo.png"))
canvas.create_image(
    80.0,
    40.0,
    image=logo
)

canvas.create_line(
    25.0,
    285.0,
    446.0,
    285.0,
    fill="#BFBFBF",
    width=1
)

canvas.create_line(
    25.0,
    622.0,
    446.0,
    622.0,
    fill="#BFBFBF",
    width=1
)


def unlock_bot1_section():
    def unlock():
        entry_widgets = [
            txtb_symbol_b1,
            txtb_volume_b1,
            txtb_profitTarget_b1,
            txtb_no_of_level_b1,
            txtb_no_of_cycle_b1
        ]
        for entry in entry_widgets:
            entry.config(state='normal')
            entry.delete(0, 'end')

        run_bot_1_button.config(
            state='normal',
            image=run_bot_1_button_image,
            cursor='hand2'
        )
        messagebox.showinfo("Success", "Bot 1 mission completed")
    window.after(0, unlock)

def unlock_bot2_section():
    def unlock():
        entry_widgets = [
            txtb_symbol_b2,
            txtb_volume_b2,
            txtb_profitTarget_b2,
            txtb_no_of_level_b2,
            txtb_no_of_cycle_b2
        ]
        for entry in entry_widgets:
            entry.config(state='normal')
            entry.delete(0, 'end')

        run_bot_2_button.config(
            state='normal',
            image=run_bot_2_button_image,
            cursor='hand2'
        )
        messagebox.showinfo("Success", "Bot 1 mission completed")
    window.after(0, unlock)

def run_bot1():
    try:
        symbol = str(txtb_symbol_b1.get()).strip()
        volume_str = txtb_volume_b1.get().strip()
        profit_target_str = txtb_profitTarget_b1.get().strip()
        no_of_levels_str = txtb_no_of_level_b1.get().strip()
        cycles_str = txtb_no_of_cycle_b1.get().strip()

        print(symbol, volume_str,profit_target_str,no_of_levels_str,cycles_str)

        if not all([symbol, volume_str, profit_target_str, no_of_levels_str, cycles_str]):
            messagebox.showerror("Input Error", "Please fill in all required fields for Bot 1.")
            return

        volume = float(volume_str)
        profit_target = float(profit_target_str)
        no_of_levels = int(no_of_levels_str)
        cycles = int(cycles_str)

        bot = Bot(symbol, volume, profit_target, no_of_levels, cycles, unlock_callback=unlock_bot1_section)
        thread = Thread(target=bot.run)
        thread.start()
        lock_bot1_section()

        messagebox.showinfo("Success", "Bot 1 started successfully!")

    except ValueError:
        messagebox.showerror("Type Error", "Please enter valid numbers in Volume, Profit Target, No. of Levels, and No. of Cycles fields.")


def run_bot2():
    try:
        symbol = str(txtb_symbol_b2.get()).strip()
        volume_str = txtb_volume_b2.get().strip()
        profit_target_str = txtb_profitTarget_b2.get().strip()
        no_of_levels_str = txtb_no_of_level_b2.get().strip()
        cycles_str = txtb_no_of_cycle_b2.get().strip()

        print(symbol, volume_str, profit_target_str, no_of_levels_str, cycles_str)

        if not all([symbol, volume_str, profit_target_str, no_of_levels_str, cycles_str]):
            messagebox.showerror("Input Error", "Please fill in all required fields for Bot 2.")
            return

        volume = float(volume_str)
        profit_target = float(profit_target_str)
        no_of_levels = int(no_of_levels_str)
        cycles = int(cycles_str)

        bot = Bot(symbol, volume, profit_target, no_of_levels, cycles, unlock_callback=unlock_bot2_section)
        thread = Thread(target=bot.run)
        thread.start()
        lock_bot2_section()
        messagebox.showinfo("Success", "Bot 2 started successfully!")

    except ValueError:
        messagebox.showerror("Type Error",
                             "Please enter valid numbers in Volume, Profit Target, No. of Levels, and No. of Cycles fields.")

run_bot_1_button = Button(
    image=run_bot_1_button_image,
    borderwidth=0,
    bg='#1F1F1F',
    activebackground='#1F1F1F',
    highlightthickness=0,
    command=run_bot1,
    cursor='hand2',
    relief="flat"
)
run_bot_1_button.place(
    x=37.0,
    y=550.0,
    width=409.0,
    height=36.0
)

run_bot_2_button = Button(
    image=run_bot_2_button_image,
    borderwidth=0,
    bg='#1F1F1F',
    activebackground='#1F1F1F',
    highlightthickness=0,
    command=run_bot2,
    cursor='hand2',
    relief="flat"
)
run_bot_2_button.place(
    x=37.0,
    y=887.0,
    width=409.0,
    height=36.0
)


window.resizable(False, False)
window.mainloop()