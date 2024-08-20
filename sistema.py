# 1 - Pessoa Fisica / 2 - Pessoa Juridica / 3 - Sair 
# 1 - Cadastrar Pessoa Fisica / 2 - Listar pessoa física / 3 - Sair 
# 1 - Cadastrar Pessoa Juridica / 2 - Listar pessoa Juridica / 3 - Sair 

from datetime import date, datetime
from pessoa import Endereco, PessoaFisica, PessoaJuridica


def main():
    
    lista_pf = []
    lista_pj = []
    
    while True:
        
        opcao = int(input("Escolha uma opcao:\n[1] Pessoa física [2] Pessoa Jurídica [3] Sair\n"))
        
        if opcao == 1:
            while True:
                opcao_PF = int(input("Escolha uma opcao:\n[1] Cadastrar [2] Listar [3] Voltar ao menu anterior\n"))
                #Cadastrar uma pessoa física
                if opcao_PF == 1:
                    novaPF = PessoaFisica()
                    nova_end_PF = Endereco()
                    
                    novaPF.nome= input("Digite o Nome da pessoa física:\n")
                    novaPF.cpf= input("Digite o CPF da pessoa física:\n")
                    novaPF.rendimento= float(input("Digite o rendimento mensal da pessoa física (DIGITE APENAS NUMEROS):\n"))
                    
                    data_nascimento = input("Digite a data de nascimento (dd/NN/aaaa):\n") # Solicita a data de nascimento
                    novaPF.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novaPF.dataNascimento).days // 365
                    
                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos. Retorne ao menu...")
                        continue # Retorna ao inicio do loop
                    
                    # Cadastro de endereco
                    nova_end_PF.logradouro = input("Digite o logradouro:\n")
                    nova_end_PF.numero = input("Digite o numero:\n")
                    end_comercial = input("Este endereco é comercial? [S] [N]\n") # Solicitar se o endereco é comercial
                    nova_end_PF.endereco_Comercial = end_comercial.strip().upper() == 'S' # Define maiusculo
                    
                    
                    novaPF.endereco = nova_end_PF
                    
                    lista_pf.append(novaPF)
                    
                    print("Cadastro realizado com sucesso")


                # Listar pessoa física
                elif opcao_PF == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"Nome:\n{cada_pf.nome}")
                            print(f"CPF:\n{cada_pf.cpf}")
                            print(f"Endereco\n{cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}")
                            print(f"Data Nascimento\n{cada_pf.dataNascimento.strftime('%d/%m/%Y')}")
                            print(f"Imposto a ser pago\n{cada_pf.calcular_imposto(cada_pf.rendimento)}")
                            print(f"Digite 0 para sair")
                            input()
                            
                    else:
                        print('Lista vazia')
                        
                # Sair do menu
                elif opcao_PF == 3:
                    print("Voltando ao menu anterior")
                    break
                
                else:
                    print("Opcao inválida, por favor digite uma das opcoes indicadas:\n")
               
               
               
        elif opcao == 2:
            while True:
                opcao_PJ = int(input("Escolha uma opcao:\n[1] Cadastrar [2] Listar [3] Voltar ao menu anterior\n"))
                #Cadastrar uma pessoa Juridica
                if opcao_PJ == 1:
                    novaPJ = PessoaJuridica()
                    nova_end_PJ = Endereco()
                    
                    novaPJ.nome= input("Digite o Nome da pessoa Jurídica:\n")
                    novaPJ.cnpj= input("Digite o CNPJ da pessoa Jurídica:\n")
                    novaPJ.rendimento= float(input("Digite o rendimento mensal da pessoa Jurídica (DIGITE APENAS NUMEROS):\n"))
                    
                    
                    # Cadastro de endereco
                    nova_end_PJ.logradouro = input("Digite o logradouro:\n")
                    nova_end_PJ.numero = input("Digite o numero:\n")
                    end_comercial = input("Este endereco é comercial? [S] [N]\n") # Solicitar se o endereco é comercial
                    nova_end_PJ.endereco_Comercial = end_comercial.strip().upper() == 'S' # Define maiusculo
                    
                    
                    novaPJ.endereco = nova_end_PJ
                    
                    lista_pj.append(novaPJ)
                    
                    print("Cadastro realizado com sucesso")


                # Listar pessoa juridica
                elif opcao_PJ == 2:
                    if lista_pj:
                        for cada_pj in lista_pj:
                            print(f"Nome:\n{cada_pj.nome}")
                            print(f"CNPJ:\n{cada_pj.cnpj}")
                            print(f"Endereco\n{cada_pj.endereco.logradouro}, {cada_pj.endereco.numero}")
                            print(f"Imposto a ser pago\n{cada_pj.calcular_imposto(cada_pj.rendimento)}")
                            print(f"Digite 0 para sair")
                            input()
                            
                    else:
                        print('Lista vazia')
                        
                # Sair do menu
                elif opcao_PJ == 3:
                    print("Voltando ao menu anterior")
                    break
                
                else:
                    print("Opcao inválida, por favor digite uma das opcoes indicadas:\n")            
        
        
        elif opcao == 3:
            print('Obrigado por utilizar nosso sistema')
            break
        
        
        else:
            print('Opcao invalida, por favor digite uma das opcoes listadas!')
            
            
if __name__ == '__main__':
    main() # Chama a funcao main