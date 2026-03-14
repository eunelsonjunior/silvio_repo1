# 1. AGENDA TELEFÔNICA SIMPLES
#   Crie um dicionário vazio e adicione 5 contatos com nome como chave e telefone como valor.
#   Depois, permita que o usuário:
#   - Consulte o telefone de um contato pelo nome
#   - Exiba todos os contatos cadastrados
#   - Verifique se um contato específico existe na agenda

n = 5
agenda = {}
for i in range(n):
   nome = input(f"Digite o {i+1}º nome: ")
   fone = input(f"Digite o {i+1}º telefone: ")
   agenda[nome] = fone

while(True):
   print(" MENU ")
   print(" 1 - Consultar telefone de um contato")
   print(" 2 - Exibir todos contatos")
   print(" 3 - Verificar se existe um contatos")
   print(" 0 - Sair")
   opcao = int(input("Digite uma opção: "))
   if opcao == 0:
      print("Saindo...")
      break
   elif opcao == 1:
      busca = input(f"Digite um nome para buscar: ")
      if busca in agenda.keys():
         print("Telefone: ", agenda[busca])
      else:
         print("Contato não existe.")
   elif opcao == 2:
      print("Contatos")
      for nome in agenda.keys():
         print(nome, agenda[nome])
   elif opcao == 3:
      busca = input(f"Digite um nome para buscar: ")
      if busca in agenda.keys():
         print("Contato existe.")
      else:
         print("Contato não existe.")
   else:
      print("Opção inválida.")
      continue