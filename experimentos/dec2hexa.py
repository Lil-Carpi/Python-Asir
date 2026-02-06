import customtkinter as ctk
import time
import math


#def dec2hexa(dec: int) -> str:
#    hex_digits = "0123456789abcdef"
#    if dec == 0:
#        return "00"
#    hexa = ""
#    while dec > 0:
#        resto = dec % 16
#        hexa = hex_digits[resto] + hexa
#        dec = dec // 16
#    return hexa.rjust(2, "0")

def rgb2hex(r: int, g: int, b: int) -> str:
    return f"#{r:02x}{g:02x}{b:02x}"

def obtenerIluminancia(r: int, g: int, b: int) -> float:
    return (0.299 * r) + (0.587 * g) + (0.114 * b)

def obtenerColorTexto(r, g, b):
    brillo = obtenerIluminancia(r, g, b)
    return "black" if brillo > 128 else "white"


class AppColor(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("cualquier cosa")
        self.geometry("400x500")
        self.enBucle = False
        self.faseBucle = 0
        self.cuadroColor = ctk.CTkFrame(self, width=400, height=150, corner_radius=20)
        self.cuadroColor.pack(pady=20)
        self.lblHex = ctk.CTkLabel(self.cuadroColor, text="#000000", font=("Arial", 24, "bold"))
        self.lblHex.place(relx=0.5, rely=0.5, anchor="center")
        self.lblInfo = ctk.CTkLabel(self, text="Seleccion Manual:")
        self.lblInfo.pack(pady=(10, 5))
        self.sliderR = self.crearSlider("Rojo", "red")
        self.sliderG = self.crearSlider("Verde", "green")
        self.sliderB = self.crearSlider("Azul", "blue")
        self.btnBucle = ctk.CTkButton(self, text="Activar bucle RGB", command=self.toggleBucle)
        self.btnBucle.pack(pady=30)
        self.actualizarColor()

    def crearSlider(self, nombre, colorTrack):
        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(pady=5)
        lbl = ctk.CTkLabel(frame, text=nombre, width=50)
        lbl.pack(side="left", padx=10)
        slider = ctk.CTkSlider(frame, from_=0, to=255, command=self.eventoSlider, progress_color=colorTrack)
        slider.set(0)
        slider.pack(side="left")
        return slider

    def eventoSlider(self, value):
        if self.enBucle:
            self.toggleBucle()
        self.actualizarColor()

    def actualizarColor(self):
        r = int(self.sliderR.get())
        g = int(self.sliderG.get())
        b = int(self.sliderB.get())

        colorHex = rgb2hex(r, g, b)
        self.cuadroColor.configure(fg_color=colorHex)
        self.lblHex.configure(text=colorHex)

        colorTexto = obtenerColorTexto(r, g, b)
        self.lblHex.configure(text_color=colorTexto)

    def toggleBucle(self):
        self.enBucle = not self.enBucle
        if self.enBucle:
            self.btnBucle.configure(text="Detener Bucle", fg_color="red")
            self.animarBucle()
        else:
            self.btnBucle.configure(text="Activar Bucle RGB", fg_color=["#3B8ED0", "#1F6AA5"])
    
    def animarBucle(self):
        if not self.enBucle:
            return

        frecuencia = 0.1
        self.faseBucle += 1


        r = int(math.sin(frecuencia * self.faseBucle + 0) * 127 + 128)
        g = int(math.sin(frecuencia * self.faseBucle + 2) * 127 + 128)
        b = int(math.sin(frecuencia * self.faseBucle + 4) * 127 + 128)

        self.sliderR.set(r)
        self.sliderG.set(g)
        self.sliderB.set(b)
        
        self.actualizarColor()
        self.after(50, self.animarBucle)


if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    app = AppColor()
    app.mainloop()
