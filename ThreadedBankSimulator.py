"""
Demonstração de Race Condition em um Sistema Bancário
====================================================

Este script demonstra o problema de race condition em operações concorrentes,
utilizando o cenário de um sistema bancário simplificado onde múltiplos
clientes tentam realizar saques simultaneamente da mesma conta.
"""

# =============================================================================
# Bloco 1: Importando as bibliotecas necessárias
# =============================================================================
import threading  # Biblioteca para criar e gerenciar threads
import random     # Biblioteca para geração de números aleatórios

"""
Bibliotecas Utilizadas:
- threading: Permite criar e gerenciar threads, possibilitando a execução de múltiplas tarefas concorrentemente
- random: Oferece métodos para gerar números aleatórios, útil para simular comportamentos variados
"""

# =============================================================================
# Bloco 2: Criando nossa conta bancária
# =============================================================================
class ContaSemProtecao:
    def __init__(self, saldo_inicial=1000):
        self.saldo = saldo_inicial
        self.total_sacado = 0
        
    def consultar_saldo(self):
        return self.saldo
    
    def sacar(self, valor):
        # Primeiro verificamos se tem saldo disponível
        if self.saldo >= valor:
            print(f"Thread {threading.current_thread().name}: Verificou saldo de R${self.saldo} para saque de R${valor}")
            
            # Leitura do saldo atual
            saldo_atual = self.saldo
            
            # Atualização do saldo
            self.saldo = saldo_atual - valor
            self.total_sacado += valor
            
            print(f"Thread {threading.current_thread().name}: Saque de R${valor} realizado. Novo saldo: R${self.saldo}")
            return True
        else:
            print(f"Thread {threading.current_thread().name}: Tentou sacar R${valor}, mas saldo insuficiente: R${self.saldo}")
            return False

"""
Classe ContaSemProtecao:

Esta classe simula uma conta bancária sem mecanismos de proteção contra acessos concorrentes. Principais características:

- Inicializa com um saldo padrão de R$1000
- Mantém registro do total sacado através do atributo `total_sacado`
- O método `sacar()` é vulnerável a race conditions porque:
  - Verifica o saldo
  - Só então atualiza o saldo
"""

# =============================================================================
# Bloco 3: Função que simula um cliente do banco
# =============================================================================
def cliente_sem_protecao(conta, nome, saques):
    """Função que simula as operações de um cliente no banco sem proteção"""
    print(f"Cliente {nome} entrou no banco")
    
    for i in range(saques):
        # Valores maiores para forçar sobrecarga
        valor = random.randint(300, 500)
        conta.sacar(valor)

"""
Simulação de Cliente Bancário:

A função `cliente_sem_protecao` simula o comportamento de um cliente realizando saques:

- Cada cliente é identificado por um nome
- O cliente realiza um número específico de saques (definido pelo parâmetro `saques`)
- Os valores de saque são gerados aleatoriamente entre R$300 e R$500

Quando executada em múltiplas threads, esta função representa diversos clientes tentando acessar a 
mesma conta bancária simultaneamente, cenário perfeito para demonstrar race conditions.
"""

# =============================================================================
# Bloco 4: Função que roda a simulação do banco
# =============================================================================
def demonstrar_sobrecarga():
    # Criar uma conta com saldo inicial
    conta = ContaSemProtecao(saldo_inicial=1000)
    print(f"Saldo inicial da conta: R${conta.consultar_saldo()}")
    
    # Lista para armazenar as threads
    threads = []
    
    # Criar várias threads simulando clientes tentando sacar dinheiro simultaneamente
    num_clientes = 5
    saques_por_cliente = 2
    
    for i in range(num_clientes):
        t = threading.Thread(target=cliente_sem_protecao, args=(conta, f"Cliente-{i+1}", saques_por_cliente), name=f"Cliente-{i+1}")
        threads.append(t)
    
    # Iniciar todas as threads
    for t in threads:
        t.start()
    
    # Aguardar todas as threads terminarem
    for t in threads:
        t.join()
    
    # Verificar o saldo final
    print("\n" + "="*60)
    print(f"Saldo inicial: R$1000")
    print(f"Total sacado: R${conta.total_sacado}")
    print(f"Saldo final: R${conta.consultar_saldo()}")
    
    # Análise dos resultados
    if conta.saldo < 0:
        print("\n SOBRECARGA DETECTADA: Saldo negativo!")
        print(f"O banco permitiu saques além do disponível devido à falta de sincronização.")
    elif conta.total_sacado > 1000:
        print("\n SOBRECARGA DETECTADA: Total sacado maior que o saldo inicial!")
        print(f"Os clientes conseguiram sacar R${conta.total_sacado} de uma conta com apenas R$1000.")
    print("="*60)

"""
Demonstração da Sobrecarga (Race Condition):

Esta função coordena a demonstração completa do problema de concorrência:

1. Cria uma conta bancária com saldo inicial de R$1000
2. Configura 5 clientes (threads), cada um realizando 2 saques
3. Inicia todas as threads simultaneamente com `t.start()`
4. Aguarda a conclusão de todas as operações com `t.join()`
5. Analisa os resultados finais

A função detecta duas condições de erro:
- Saldo negativo: Indica que o banco permitiu saques maiores que o disponível
- Total sacado > saldo inicial: Mostra que foi possível sacar mais dinheiro do que existia inicialmente

Qualquer uma dessas condições comprova a existência de uma race condition no sistema.
"""

# =============================================================================
# Bloco 5: Código principal que inicia tudo
# =============================================================================
if __name__ == "__main__":
    print("DEMONSTRAÇÃO DE SISTEMA BANCÁRIO COM SOBRECARGA\n")
    demonstrar_sobrecarga()

"""
Execução da Demonstração:

Este é o ponto de entrada do programa que:

1. Exibe um cabeçalho informativo
2. Chama a função `demonstrar_sobrecarga()` para iniciar a simulação

Quando executado, este código deve demonstrar claramente o problema da race condition,
onde o acesso concorrente à conta bancária resulta em um estado inconsistente do sistema.
"""