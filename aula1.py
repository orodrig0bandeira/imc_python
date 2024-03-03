# print serve para exibir no terminal determinada coisa 

# 
usuario = input("qual é o seu usuário?")
senha = input("qual é sua senha?")
u = "negao"
s = "123"

if usuario == u and senha == s:
    print("aceito")
    n1 = float(input("qual a sua peso?")) 
    n2 = float(input("qual é o seu altura?"))
    n3 = (float(n1/(n2*n2)))
    
    if n3<18.5:
        print (f"Qual o valor do seu MC {n1/(n2*n2)}")
        print("magresa")

    elif n3>=18.5 and n3<=24.9:
        print (f"Qual o valor do seu MC {n1/(n2*n2)}")
        print("normal")

    elif n3 >=25.0 and n3<=29.9:
        print (f"Qual o valor do seu MC {n1/(n2*n2)}")
        print("sobrepeso")
        
    else:
        print("teste")

else:
    print("inválido")
