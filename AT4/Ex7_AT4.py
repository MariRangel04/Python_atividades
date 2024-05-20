##sanduiches pedidos
sandwich_orders = ["Frango", "Vegetariano", "Natural", "Queijo", "Presunto e Quiejo"]
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"Preparando seu sanduíche de {sandwich}")
    print(f"Sanduíche de {sandwich} preparado!")
    finished_sandwiches.append(sandwich)

print("\nSanduíches preparados:")
for sandwich in finished_sandwiches:
    print("- " + sandwich)
