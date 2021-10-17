import time
def choice1transportation():
    options={"1":"gå", "2":"cykla", "3":"åka buss", "4": "ta bil"}

    x=1
    while x==1:

        for option in (options):
            print(f"{option}: {options[option]}")
        

        choice=input("välj alternativ: ")
        if choice in options:
            print(f"Du har valt alternativ {choice}")
            print()
            time.sleep(1.5)
            print(f"kul att du valde att {options[choice]}!")
            if choice== "4":
                print()
                time.sleep(1.5)
                print("Oh nej! du krocka och dog!")
                time.sleep(1)
                print("gameover")
                #gameOver()
                x=0
            else:
                print("grattis du tog dig till skolan!!")
                x=0