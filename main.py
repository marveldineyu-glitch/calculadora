import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora"
    page.theme_mode = ft.ThemeMode.DARK
    
    pantalla = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, read_only=True, text_size=40)

    def calcular(e):
        try:
            pantalla.value = str(eval(pantalla.value))
        except:
            pantalla.value = "Error"
        page.update()

    def limpiar(e):
        pantalla.value = "0"
        page.update()

    def agregar_numero(e):
        if pantalla.value == "0":
            pantalla.value = e.control.text
        else:
            pantalla.value += e.control.text
        page.update()

    botones = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"],
    ]

    page.add(pantalla)
    for fila in botones:
        btn_fila = []
        for btn in fila:
            if btn == "=":
                btn_fila.append(ft.ElevatedButton(text=btn, on_click=calcular, expand=1))
            elif btn == "C":
                btn_fila.append(ft.ElevatedButton(text=btn, on_click=limpiar, expand=1))
            else:
                btn_fila.append(ft.ElevatedButton(text=btn, on_click=agregar_numero, expand=1))
        page.add(ft.Row(btn_fila))

ft.app(target=main)
