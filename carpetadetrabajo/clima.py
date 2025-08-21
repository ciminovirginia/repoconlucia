temperature = float(input("Ingrese la temperatura en °C: "))
is_raining = input("¿Está lloviendo? (s/n): ") == "s"
if temperature > 30:
        if is_raining:
            print("Calor y lluvia. Traiga un paraguas y use ropa liviana.")
        else:
            print("¡Mucho calor! Use protector solar y manténgase hidratado.")
elif temperature > 20:
    if is_raining:
        print("Cálido y lluvioso. Traiga un paraguas.")
    else:
        print("Clima agradable. ¡Disfrute su día!")
elif temperature > 10:
    if is_raining:
        print("Frío y lluvioso. Traiga una chaqueta y un paraguas.")
    else:
        print("Clima fresco. Es posible que necesite una chaqueta ligera.")
else:
    if is_raining:
        print("Frío y lluvioso. Lleve un abrigo abrigado y un paraguas.")
    else:
        print("Clima frío. ¡Abríguese!")