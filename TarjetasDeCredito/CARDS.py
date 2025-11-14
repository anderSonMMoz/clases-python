 
cards = ['4242424242424242','4000056655665556','5555555555554444','378282246310005','6011111111111117']
 
"""
si la tc comienza con 4, mostrar 4 primeros, 8x y 4 ultimos
si comienza con 5, mostrar 6 primeros, 6xx y ultimos 4
si comienza con 3, igual que el cinco
si comienza con 6, mostrar primeros 4, 6x y ultimos 6
 
"""
for card in cards:
    MaskedCard = ""
    if card.startswith("3") or card.startswith("5"):
        MaskedCard = f"{card[:6]}xxxxxx{card[-4:]}"
        print(MaskedCard)
    elif card.startswith("4"):
        MaskedCard = f"{card[:4]}xxxxxxxx{card[-4:]}"
        print(MaskedCard)
    elif card.startswith("6"):
        MaskedCard = f"{card[:4]}xxxxxx{card[-6:]}"
        print(MaskedCard)
    


        
