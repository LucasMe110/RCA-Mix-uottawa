import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to calculate the values
def EMV_account():
    try:
        # Input retrieval
        cement = get_input_as_int(cement_entry)
        fines = get_input_as_int(fines_entry)
        natural = get_input_as_int(natural_entry)
        water = get_input_as_int(water_entry)

        rca = get_input_as_float(rca_entry)
        ova = get_input_as_float(ova_entry)
        natural_ca = get_input_as_float(natural_grav_entry)
        residual_mortar_content = get_input_as_float(residual_mortar_content_entry) / 100

        # Math calculations
        replacement = 1 - (1 - residual_mortar_content) * (rca / ova)
        mortal_volume = 1 - (natural / natural_ca / 1000)
        new_mortal = mortal_volume - ((natural / (natural_ca * 1000)) * replacement)

        cement_return = round(cement * (new_mortal / mortal_volume), 2)
        cement_unit_return = round(1, 2)

        fine_agg = round(fines * (new_mortal / mortal_volume), 2)
        fine_agg_unit = round(fine_agg / cement_return, 2)

        natural_return = round((natural / natural_ca / 1000) * replacement * natural_ca * 1000, 2)
        natural_unit_return = round(natural_return / cement_return, 2)

        rca_return = round((natural / (natural_ca * 1000)) * rca * 1000, 2)
        rca_unit_return = round(rca_return / cement_return, 2)

        water_return = round(water * (new_mortal / mortal_volume), 2)
        water_unit_return = round(water_return / cement_return, 2)

        # Update labels with results
        update_labels(cement_return, cement_unit_return, fine_agg, fine_agg_unit,
                      natural_return, natural_unit_return, rca_return, rca_unit_return,
                      water_return, water_unit_return)

    except ValueError as ve:
        messagebox.showerror("Input Error", f"Invalid input: {ve}")
    except Exception as e:
        messagebox.showerror("Error", f"Error calculating: {e}")

def EMV_mode_account():
    try:
        # Input retrieval
        cement = get_input_as_int(cement_entry)
        fines = get_input_as_int(fines_entry)
        natural = get_input_as_int(natural_entry)
        water = get_input_as_int(water_entry)

        cement_gravity = get_input_as_float(cement_grav_entry)
        fines_gravity = get_input_as_float(fines_grav_entry)
        rca = get_input_as_float(rca_entry)
        ova = get_input_as_float(ova_entry)
        natural_ca = get_input_as_float(natural_grav_entry)
        residual_mortar_content = get_input_as_float(residual_mortar_content_entry) / 100
        psi = get_input_as_float(psi_entry)

        # Intermediate calculations
        replacement = 1 - (1 - residual_mortar_content) * (rca / ova)
        mortar_volume = 1000 - (natural / natural_ca)
        new_mortar = ((mortar_volume / 1000) - ((natural / (natural_ca * 1000)) * replacement)) * 1000
        residual_mortar = mortar_volume - new_mortar

        cement_to_sand_ratio = 1 / psi
        bc = 1 / cement_gravity
        bfa = 1 / fines_gravity

       # Output data calculations
        cement_return = round(((cement / cement_gravity) - residual_mortar * bc / (bc + psi * bfa)) * cement_gravity, 2)
        cement_unit_return = round(1, 2)
        natural_return = round(natural / cement * replacement * 100, 2)
        natural_unit_return = round(natural_return / cement_return, 2)
        rca_return = round((natural / natural_ca) * (1 - replacement) / ((1 - residual_mortar_content) * (rca / natural_ca)), 2)
        rca_unit_return = round(rca_return / cement_return, 2)
        water_return = round(water / cement * cement_return, 2)
        water_unit_return = round(water_return / cement_return, 2)
        fine_agg = round((1000 - cement_return - natural_return - rca_return - water_return) * fines_gravity, 2)
        fine_agg_unit = round(fine_agg / cement_return, 2)

        # Update labels with results
        update_labels(cement_return, cement_unit_return, fine_agg, fine_agg_unit,
                      natural_return, natural_unit_return, rca_return, rca_unit_return,
                      water_return, water_unit_return)

    except ValueError as ve:
        messagebox.showerror("Input Error", f"Invalid input: {ve}")
    except Exception as e:
        messagebox.showerror("Error", f"Error calculating: {e}")

def EV_account():
    try:
        # Input retrieval
        cement = get_input_as_int(cement_entry)
        fines = get_input_as_int(fines_entry)
        natural = get_input_as_int(natural_entry)
        water = get_input_as_int(water_entry)

        cement_gravity = get_input_as_float(cement_grav_entry)
        fines_gravity = get_input_as_float(fines_grav_entry)
        natural_ca = get_input_as_float(natural_grav_entry)
        water_gravity = get_input_as_float(water_grav_entry)

        rca = get_input_as_float(rca_entry)
        rm = get_input_as_float(residual_mortar_entry)
        old_cement = get_input_as_float(old_cement_entry)
        old_sand = get_input_as_float(old_fine_entry)
        residual_mortar_content = get_input_as_float(residual_mortar_content_entry) / 100

        # Intermediate calculations 1
        F4 = 1
        F5 = fines / cement
        F6 = natural / cement
        F7 = water / cement

        C24 = F6 * (1 - residual_mortar_content)
        C25 = F6 * residual_mortar_content

        # Intermediate calculations 2
        C21 = C25 * (F4 / (F4 + F5 + F6))
        D21 = C21 / old_cement
        C23 = C25 * (1 - (F4 / (F4 + F5 + F6)))
        D23 = C23 / old_sand
        D24 = C24 / rca

        # Intermediate calculations 3
        D20 = (F4 / cement_gravity) - D21
        D22 = (F5 / fines_gravity) - D23
        D26 = ((F6 / natural_ca) - D24) * (F5 / F6)
        D27 = ((F6 / natural_ca) - D24) * (1 - (F5 / F6))

        # Intermediate calculations 4
        C20 = D20 * cement_gravity
        C22 = fines_gravity * D22
        C26 = fines_gravity * D26
        C27 = rca * D27
        C28 = rm * D27 * residual_mortar_content

        # Output data
        cement_unit_return = round(C20 + C21, 2)
        fine_agg_unit = round((C26 + C22) / C20, 2)
        rca_unit_return = round((C24 + C25 + C27 + C28) / C20, 2)
        water_unit_return = round(F7, 2)
        cement_return = round(1000 / ((cement_unit_return / cement_gravity) + 
                                       (fine_agg_unit / fines_gravity) + 
                                       (rca_unit_return / rm) + 
                                       (water_unit_return)), 2)
        fine_agg = round(cement_return * fine_agg_unit, 2)
        rca_return = round(cement_return * rca_unit_return, 2)
        water_return = round(cement_return * water_unit_return, 2)

        # Natural is not used, setting to 0
        natural_return = 0
        natural_unit_return = 0

        # Update labels with results
        update_labels(cement_return, cement_unit_return, fine_agg, fine_agg_unit,
                      natural_return, natural_unit_return, rca_return, rca_unit_return,
                      water_return, water_unit_return)

    except ValueError as ve:
        messagebox.showerror("Input Error", f"Invalid input: {ve}")
    except Exception as e:
        messagebox.showerror("Error", f"Error calculating: {e}")




def EMV_type():
    #afundar
    EMV_MOD_button.config(bg='gray30')
    EMV_button.config(bg='gray20')
    EV_button.config(bg='gray30')
    #account
    calculate_button.config(command=EMV_account)
    #text
    type_method_title.config(text="Equivalent Mortar Volume")
    #grey
    cement_grav_entry.configure(bg='#2e2e2e')
    fines_grav_entry.configure(bg='#2e2e2e')
    water_grav_entry.configure(bg='#2e2e2e')
    psi_entry.configure(bg='#2e2e2e')
    old_cement_entry.configure(bg='#2e2e2e')
    old_fine_entry.configure(bg='#2e2e2e')
    residual_mortar_entry.configure(bg='#2e2e2e')
    #white
    ova_entry.configure(bg='#FFFFFF')

def EMV_mod_type():
    #afundar
    EMV_MOD_button.config(bg='gray20')
    EMV_button.config(bg='gray30')
    EV_button.config(bg='gray30')
    #account
    calculate_button.config(command=EMV_mode_account)
    #text
    type_method_title.config(text="Equivalent Mortar Volume - modifield")
    #grey
    old_cement_entry.configure(bg='#2e2e2e')
    old_fine_entry.configure(bg='#2e2e2e')
    residual_mortar_entry.configure(bg='#2e2e2e')
    #white
    ova_entry.configure(bg='#FFFFFF')
    cement_grav_entry.configure(bg='#FFFFFF')
    fines_grav_entry.configure(bg='#FFFFFF')
    water_grav_entry.configure(bg='#FFFFFF')
    psi_entry.configure(bg='#FFFFFF')

def EV_type():
    #afundar
    EMV_MOD_button.config(bg='gray30')
    EMV_button.config(bg='gray30')
    EV_button.config(bg='gray20')
    #account
    calculate_button.config(command=EV_account)
    #text
    type_method_title.config(text="Equivalent Volume")
    #grey
    ova_entry.configure(bg='#2e2e2e')
    psi_entry.configure(bg='#2e2e2e')
    #white
    old_cement_entry.configure(bg='#FFFFFF')
    old_fine_entry.configure(bg='#FFFFFF')
    residual_mortar_entry.configure(bg='#FFFFFF')
    cement_grav_entry.configure(bg='#FFFFFF')
    fines_grav_entry.configure(bg='#FFFFFF')
    water_grav_entry.configure(bg='#FFFFFF')


def get_input_as_int(entry):
    return int(entry.get())

def get_input_as_float(entry):
    return float(entry.get())

def update_labels(cement_return, cement_unit_return, fine_agg, fine_agg_unit,
                  natural_return, natural_unit_return, rca_return, rca_unit_return,
                  water_return, water_unit_return):
    cement_emv_label.config(text=str(cement_return))
    cement_emv_unit_label.config(text=str(cement_unit_return))
    fine_agg_emv_label.config(text=str(fine_agg))
    fine_agg_emv_unit_label.config(text=str(fine_agg_unit))
    natural_ca_emv_label.config(text=str(natural_return))
    natural_ca_emv_unit_label.config(text=str(natural_unit_return))
    rca_emv_label.config(text=str(rca_return))
    rca_emv_unit_label.config(text=str(rca_unit_return))
    water_emv_label.config(text=str(water_return))
    water_emv_unit_label.config(text=str(water_unit_return))

# Main window configuration
root = tk.Tk()
root.geometry("890x650")
root.title("RCA Mix")
root.configure(bg='gray20')

# Function to create Labels with default style
def create_label(text, row, column, colspan=1, font=("Helvetica", 12, "bold")):
    label = tk.Label(root, text=text, font=font, fg='white', bg='gray20')
    label.grid(row=row, column=column, columnspan=colspan, pady=5, sticky='w')
    return label

# Function to create Entry with default style
def create_entry(row, column):
    entry = tk.Entry(root, bg='white', fg='black')
    entry.grid(row=row, column=column, sticky='w')
    return entry

# Title
title_label = create_label("Recycled Concrete aggregates Mix-design", 0, 1, 6, ("Helvetica", 16, "bold"))

# "Conventional Mix" section
conv_label = create_label("Conventional Mix", 3, 1, 1)

create_label("Material", 4, 0)
create_label("kg/m³", 4, 1)
create_label("Bulk Specific Gravity", 4, 2)


create_label("Cement", 5, 0)

cement_entry = create_entry(5, 1)
cement_grav_entry = create_entry(5, 2)

create_label("Fines", 6, 0)
fines_entry = create_entry(6, 1)
fines_grav_entry = create_entry(6, 2)


create_label("Coarse", 7, 0)
natural_entry = create_entry(7, 1)
natural_grav_entry = create_entry(7, 2)

create_label("Water", 8, 0)
water_entry = create_entry(8, 1)
water_grav_entry = create_entry(8, 2)

create_label("RCA", 9, 0)
rca_entry = create_entry(9, 2)

create_label("OVA", 10, 0)
ova_entry = create_entry(10, 2)

create_label("Residual mortar", 11, 0)
residual_mortar_entry = create_entry(11, 2)

create_label("Old_cement", 12, 0)
old_cement_entry = create_entry(12, 2)

create_label("Old_fine", 13, 0)
old_fine_entry = create_entry(13, 2)

create_label("Residual Mortar Content", 14, 0)
residual_mortar_content_entry = create_entry(14, 2)

create_label("Ψ", 15, 0)
psi_entry = create_entry(15, 2)

# "Equivalent Mortar Volume - EMV" section

type_method_title = create_label("", 1, 2, 3)

#tipo conta

# Função para criar um botão com estilo padrão
def create_button(text, row, column, command=None, colspan=1, bg='gray30', fg='white'):
    button = tk.Button(root, text=text, command=command, bg=bg, fg=fg)
    button.grid(row=row, column=column, columnspan=colspan, pady=5, sticky='ew')
    return button

# Adicione o botão
EMV_button = create_button("EMV", 2, 1, command=EMV_type)
EMV_MOD_button = create_button("EMV-MOD", 2, 2, command=EMV_mod_type)
EV_button = create_button("EV", 2, 4,command=EV_type)

create_label("kg/m³", 4, 5)
create_label("Unit", 4, 6)

create_label("Cement", 5, 4)
cement_emv_label = tk.Label(root, text="0", fg='white', bg='gray20')
cement_emv_label.grid(row=5, column=5, sticky='w')
cement_emv_unit_label = tk.Label(root, text="0", fg='white', bg='gray20')
cement_emv_unit_label.grid(row=5, column=6, sticky='w')

create_label("Fine Agg.", 6, 4)
fine_agg_emv_label = tk.Label(root, text="0", fg='white', bg='gray20')
fine_agg_emv_label.grid(row=6, column=5, sticky='w')
fine_agg_emv_unit_label = tk.Label(root, text="0", fg='white', bg='gray20')
fine_agg_emv_unit_label.grid(row=6, column=6, sticky='w')

create_label("Natural_CA", 7, 4)
natural_ca_emv_label = tk.Label(root, text="0", fg='white', bg='gray20')
natural_ca_emv_label.grid(row=7, column=5, sticky='w')
natural_ca_emv_unit_label = tk.Label(root, text="0", fg='white', bg='gray20')
natural_ca_emv_unit_label.grid(row=7, column=6, sticky='w')

create_label("RCA", 8, 4)
rca_emv_label = tk.Label(root, text="0", fg='white', bg='gray20')
rca_emv_label.grid(row=8, column=5, sticky='w')
rca_emv_unit_label = tk.Label(root, text="0", fg='white', bg='gray20')
rca_emv_unit_label.grid(row=8, column=6, sticky='w')

create_label("Water", 9, 4)
water_emv_label = tk.Label(root, text="0", fg='white', bg='gray20')
water_emv_label.grid(row=9, column=5, sticky='w')
water_emv_unit_label = tk.Label(root, text="0", fg='white', bg='gray20')
water_emv_unit_label.grid(row=9, column=6, sticky='w')

# Button to start the calculation
calculate_button = tk.Button(root, text="Calculate", command='', bg='gray30', fg='white')
calculate_button.grid(row=17, column=2)
#, columnspan=7, pady=20)

def load_image(path, size, bg_color):
    try:
        # Tenta abrir a imagem
        image = Image.open(path)
        image = image.resize(size)
        return ImageTk.PhotoImage(image)
    except IOError:
        # Se não encontrar a imagem, criar uma imagem sólida da cor de fundo
        solid_color_image = Image.new('RGB', size, bg_color)
        return ImageTk.PhotoImage(solid_color_image)

# Definir a cor de fundo padrão para a imagem
default_bg_color = (50, 50, 50)  # RGB para 'gray20'

# Carregar imagens com tratamento de exceção
photo_structure = load_image("img/structure.jpeg", (130, 72), default_bg_color)
photo_university = load_image("img/uottawa.png", (178, 47), default_bg_color)

# Verificar se a imagem foi carregada corretamente
if photo_structure is not None:
    label_structure = tk.Label(root, image=photo_structure, bg='gray20')
    label_structure.grid(row=11, column=5)

if photo_university is not None:
    label_university = tk.Label(root, image=photo_university, bg='gray20')
    label_university.grid(row=11, column=4)

# Application loop
root.mainloop()
