name=input("enter your name: ")

match name:
    case "rifat" | "rakib" | "sakib":
        print("pagla")
    # case "rakib":
    #     print("pagla")
    # case "sakib":
    #     print("pagla")
    case "bulbul":
        print("valo manush")
    case _:
        print("go home")