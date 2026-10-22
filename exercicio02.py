#identação
fruta = "maça"
match fruta: #escolha
    case "maça":
        print("A fruta é uma maçã")
    case "banana":
        print("A fruta é uma banana")
    case _:
        print("Não é uma fruta")