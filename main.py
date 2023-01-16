from tts_api import lain_say
from openai_api import ask_question
from clear_screen import cls

def menu():
    # cls()
    finished = False
    while finished == False:
        print("MENU")
        print("1) Hacer una pregunta.")
        print("2) Salir.")
        res = int(input("R:"))
        cls()

        if res < 1 or res > 2 or None:
            print("Respuesta invalida, intentalo otra vez.")
            return

        if res == 1:
            prompt = input("¿Cual es tu pregunta?.\nR: ")
            ai_response = ask_question(prompt)
            print("Lain say's:\n", ai_response)
            lain_say(ai_response)
        else:
            exit()

menu()
