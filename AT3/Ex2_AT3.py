##jogo da forca
print(""" 
      
      *****************
      **Jogo da Forca**            
      *****************
""")

palavra_reservada= 'Banana'
acertou=False
enforcou=False
erros=0

palavra= ['_','_','_','_','_','_']

print(palavra)

chute = input('Chute uma letra:')

for i, letra in enumerate(palavra_reservada):
    if chute.upper() == letra.upper():
        palavra[i]=chute
        
acertou = not '_' in palavra
        
print(palavra)

if acertou == True:
    print("""
         ***************
         **Você venceu**
         ***************    
          """)
