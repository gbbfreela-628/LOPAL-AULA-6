aluno = {"nome":"Ana", "nota":8, "cel":"1178781234"}

clientes = [
    {"nome":"Ana","cel":"12345678", "empresa":"FIAT"},
    {"nome":"Pedro", "cel":"12345567", "empresa":"INTEL"},
    {"nome":"Maria", "cel":"12345567", "empresa":"SEBRAE"},
    {"nome":"Felipe", "cel":"12345567", "empresa":"Microsoft"}
]

#Pesquisa de um cliente pela Empresa

empresa_digitada = input ("Digite o nome da empresa: ")
for cliente in clientes:
    if cliente ["empresa"] == empresa_digitada:
        print(cliente["nome"])

#Cadastrar um novo Cliente

print ("---> Cadastrando um novo CLIENTE <---")
nome = input ("Digite o nome do cliente: ")
celular = input ("Digite o número de celular do cliente: ")
empresa = input ("Qual a empresa: ")

novo_cliente = {
    "nome": nome,
    "cel": celular,
    "empresa": empresa
}

clientes.append(novo_cliente)
print (clientes)



# Remover um Cliente

print ("---> Removendo um cliente pelo nome <---")
nome_cliente = input ("Digite o nome do cliente para remover: ")
for cliente in clientes:
    if cliente["nome"] == nome_cliente:
        clientes.remove (cliente)
        break


print (clientes)








