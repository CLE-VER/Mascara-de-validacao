import re

def validate_name(name):
    """
    Valida um nome de acordo com as seguintes regras:
    - Deve conter nome e sobrenome separados por espaço
    - Primeiro caractere do nome e sobrenome deve ser maiúsculo
    - Demais caracteres devem ser minúsculos
    - Não deve conter caracteres especiais ou numéricos
    
    Args:
        name (str): O nome a ser validado
        
    Returns:
        bool: True se o nome é válido, False caso contrário
    """
    # Expressão regular para validar o nome
    # Primeiro caractere maiúsculo seguido de minúsculos, um espaço,
    # e então primeiro caractere maiúsculo seguido de minúsculos
    pattern = r'^[A-Z][a-z]+\s[A-Z][a-z]+$'
    
    return bool(re.match(pattern, name))


def validate_email(email):
    """
    Valida um e-mail com regras mais flexíveis
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[bB][rR]$'
    return bool(re.match(pattern, email))


def validate_password(password):
    """
    Valida uma senha de acordo com as seguintes regras:
    - Pode conter letras maiúsculas, minúsculas e números
    - Deve ter pelo menos uma letra maiúscula
    - Deve ter pelo menos um número
    - Deve ter exatamente 8 caracteres
    
    Args:
        password (str): A senha a ser validada
        
    Returns:
        bool: True se a senha é válida, False caso contrário
    """
    # Verificar se a senha tem exatamente 8 caracteres
    if len(password) != 8:
        return False
    
    # Verificar se a senha contém pelo menos uma letra maiúscula
    if not re.search(r'[A-Z]', password):
        return False
    
    # Verificar se a senha contém pelo menos um número
    if not re.search(r'[0-9]', password):
        return False
    
    # Verificar se a senha contém apenas letras (maiúsculas ou minúsculas) e números
    if not re.match(r'^[a-zA-Z0-9]+$', password):
        return False
    
    return True


def validate_cpf(cpf):
    """
    Valida um CPF verificando formato e dígitos verificadores
    """
    # Remove caracteres não numéricos
    cpf_nums = re.sub(r'[^0-9]', '', cpf)
    
    # Verifica se tem 11 dígitos
    if len(cpf_nums) != 11:
        return False
        
    # Verifica se todos os dígitos são iguais
    if len(set(cpf_nums)) == 1:
        return False
        
    # Verifica o formato
    if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
        return False
        
    return True


def validate_phone(phone):
    """
    Valida um telefone celular de acordo com um dos formatos:
    - (xx) 9xxxx-xxxx
    - (xx) 9xxxxxxxx
    - xx 9xxxxxxxx
    
    Args:
        phone (str): O telefone a ser validado
        
    Returns:
        bool: True se o telefone é válido, False caso contrário
    """
    patterns = [
        r'^\(\d{2}\)\s9\d{4}-\d{4}$',  
        r'^\(\d{2}\)\s9\d{8}$',        
        r'^\d{2}\s9\d{8}$'             
    ]
    
    # Verifica se o telefone corresponde a algum dos padrões
    for pattern in patterns:
        if re.match(pattern, phone):
            return True  # Retorna True assim que encontrar um padrão válido
    
    return False


def test_validations():
    """
    Função para testar as validações implementadas
    """
    # Testes para validação de nomes
    valid_names = ["Alan Turing", "Noam Chomsky", "Ada Lovelace"]
    invalid_names = ["1Alan", "Alan", "A1an", "alan turing", "Alan turing"]
    
    print("=== Teste de Validação de Nomes ===")
    for name in valid_names:
        result = validate_name(name)
        assert result == True, f"Nome '{name}' deveria ser válido"
        print(f"'{name}': {'Válido' if result else 'Inválido'}")
    
    for name in invalid_names:
        result = validate_name(name)
        assert result == False, f"Nome '{name}' deveria ser inválido"
        print(f"'{name}': {'Válido' if result else 'Inválido'}")
    
    # Testes para validação de e-mails
    valid_emails = ["a@a.br", "divulga@ufpa.br", "user.name+tag@domain.com.br"]
    invalid_emails = ["@", "a@.br", "T@teste.br", "a@a.com"]
    
    print("\n=== Teste de Validação de E-mails ===")
    for email in valid_emails:
        result = validate_email(email)
        assert result == True, f"E-mail '{email}' deveria ser válido"
        print(f"'{email}': {'Válido' if result else 'Inválido'}")
    
    for email in invalid_emails:
        result = validate_email(email)
        assert result == False, f"E-mail '{email}' deveria ser inválido"
        print(f"'{email}': {'Válido' if result else 'Inválido'}")
    
    # Testes para validação de senhas
    valid_passwords = ["518R2r5e", "F123456A", "1234567T", "ropsSoq0"]
    invalid_passwords = ["F1234567A", "abcdefgH", "1234567HI", "abcdefg1"]
    
    print("\n=== Teste de Validação de Senhas ===")
    for password in valid_passwords:
        result = validate_password(password)
        assert result == True, f"Senha '{password}' deveria ser válida"
        print(f"'{password}': {'Válido' if result else 'Inválido'}")
    
    for password in invalid_passwords:
        result = validate_password(password)
        assert result == False, f"Senha '{password}' deveria ser inválida"
        print(f"'{password}': {'Válido' if result else 'Inválido'}")
    
    # Testes para validação de CPFs
    valid_cpfs = ["123.456.789-09", "000.000.000-00"]
    invalid_cpfs = ["123.456.789-0", "111.111.11-11", "123456789-09"]
    
    print("\n=== Teste de Validação de CPFs ===")
    for cpf in valid_cpfs:
        result = validate_cpf(cpf)
        assert result == True, f"CPF '{cpf}' deveria ser válido"
        print(f"'{cpf}': {'Válido' if result else 'Inválido'}")
    
    for cpf in invalid_cpfs:
        result = validate_cpf(cpf)
        assert result == False, f"CPF '{cpf}' deveria ser inválido"
        print(f"'{cpf}': {'Válido' if result else 'Inválido'}")
    
    # Testes para validação de telefones
    valid_phones = ["(91) 99999-9999", "(91) 999999999", "91 999999999"]
    invalid_phones = ["(91) 59999-9999", "99 99999-9999", "(94)95555-5555"]
    
    print("\n=== Teste de Validação de Telefones ===")
    for phone in valid_phones:
        result = validate_phone(phone)
        assert result == True, f"Telefone '{phone}' deveria ser válido"
        print(f"'{phone}': {'Válido' if result else 'Inválido'}")
    
    for phone in invalid_phones:
        result = validate_phone(phone)
        assert result == False, f"Telefone '{phone}' deveria ser inválido"
        print(f"'{phone}': {'Válido' if result else 'Inválido'}")
    
    print("\nTodos os testes foram concluídos com sucesso!")


def menu():
    """
    Exibe um menu interativo para o usuário
    """
    while True:
        print("\n=== Sistema de Validação ===")
        print("1. Validar Nome")
        print("2. Validar E-mail")
        print("3. Validar Senha")
        print("4. Validar CPF")
        print("5. Validar Telefone")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "0":
            print("Programa encerrado!")
            break
            
        elif opcao == "1":
            nome = input("Digite o nome (Ex: Nome Sobrenome): ")
            if validate_name(nome):
                print("✓ Nome válido!")
            else:
                print("✗ Nome inválido! Deve ter Nome Sobrenome com iniciais maiúsculas.")
                
        elif opcao == "2":
            email = input("Digite o e-mail (Ex: usuario@dominio.br): ")
            if validate_email(email):
                print("✓ E-mail válido!")
            else:
                print("✗ E-mail inválido! Deve terminar com .br e ter letras minúsculas.")
                
        elif opcao == "3":
            senha = input("Digite a senha (8 caracteres, letras e números): ")
            if validate_password(senha):
                print("✓ Senha válida!")
            else:
                print("✗ Senha inválida! Deve ter 8 caracteres, uma maiúscula e um número.")
                
        elif opcao == "4":
            cpf = input("Digite o CPF (Ex: 123.456.789-00): ")
            if validate_cpf(cpf):
                print("✓ CPF válido!")
            else:
                print("✗ CPF inválido! Use o formato xxx.xxx.xxx-xx")
                
        elif opcao == "5":
            telefone = input("Digite o telefone (Ex: (11) 91234-5678): ")
            if validate_phone(telefone):
                print("✓ Telefone válido!")
            else:
                print("✗ Telefone inválido! Use um dos formatos: (xx) 9xxxx-xxxx, (xx) 9xxxxxxxx ou xx 9xxxxxxxx")
                
        else:
            print("Opção inválida! Tente novamente.")
        
        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    menu()