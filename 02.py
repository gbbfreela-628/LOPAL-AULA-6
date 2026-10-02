#Lista de tarefas

tarefas = [
    {"titulo":"Estudar","concluida":"sim","prioridade":"alta"},
    {"titulo":"Ler","concluida":"nao","prioridade":"baixa"},
    {"titulo":"Estudar História","concluida":"sim","prioridade":"alta"},
    {"titulo":"Estudar matematica","concluida":"nao","prioridade":"alta"}
]



# Mostrar todas as tarefas

while True:
   print ("1 - Mostrar todas as tarefas")
   print ("2 - Mostrar tarefas concluidas")
   print ("3 - Mostrar tarefas pendentes")
   print ("4 - Mostrar tarefas por prioridade")
   print ("5 - Cadastrar tarefa nova")
   print ("6 - Finalizar tarefa")
   print ("7 - Remover tarefa")
   print ("0 - sair")


   opcao = input ("Escolha uma opcao: ")
   if opcao == "1":
      print ("---> Todas as tarefas: <---")
      print (tarefas)

# Mostrar tarefas concluidas
      
   elif opcao == "2":
      print ("---> Tarefas Concluidas! <---") 
      for tarefa in tarefas:
         if tarefa ["concluida"] == "sim":
          print (tarefa)

# Mostrar tarefas pendentes
   
   elif opcao == "3":
      print ("---> Tarefas Pendentes!!! <---")
      for tarefa in tarefas:
         if tarefa ["concluida"] == "nao":
            print (tarefa)

# Mostrar tarefas por prioridade

   elif opcao == "4":
      print ("---> Tarefas por prioridade <---")
      for tarefa in tarefas:
         if tarefa ["prioridade"] == "alta" and "baixa":
            print (tarefa) 

# Cadastrar nova tarefa   

   elif opcao == "5":
      print ("---> Cadastrar nova tarefa: <---")

      titulo = input("Digite o titulo da tarefa: ")
      concluida = input("Digite se a tarefa está concluida: ")
      prioridade = input (" Qual a prioridade da tarefa? ")


      nova_tarefa = {
         "titulo":titulo,
         "concluida":concluida,
         "prioridade":prioridade
      }
   
      tarefas.append(nova_tarefa)
      print (tarefas)

# Finalizar tarefa

   elif opcao == "6":
      print ("---> Finalizar tarefa <---")

      tarefa_finalizada = input("Qual tarefa deseja finalizar?")
      for tarefa in tarefas:
          if tarefa ["titulo"] == tarefa_finalizada:
            tarefa ["concluida"] = "sim"
            print(f"Tarefa: {tarefa_finalizada} finalizada com sucesso!")

# Remover tarefa

   elif opcao == "7":
     print ("---> Remover tarefa <---")
     remover_tarefa = input(" Qual tarefa deseja remover? ")
     for tarefa in tarefas:
         if tarefa ["titulo"] == remover_tarefa:
           tarefas.remove (tarefa)
           print(f"Tarefa removida com sucesso!")
         
# Sair 

   elif opcao == "0":
      print("Saindo do sistema...")
      break

   


         

      

   



      




