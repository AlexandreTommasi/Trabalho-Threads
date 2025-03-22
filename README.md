# ThreadedBankSimulator 🏦

## Sobre o Projeto
ThreadedBankSimulator é uma demonstração educativa sobre concorrência e race conditions em sistemas multithread. O projeto simula um sistema bancário simplificado onde múltiplos clientes tentam realizar saques simultaneamente da mesma conta, revelando problemas clássicos de sincronização.

## 🔍 O Problema da Race Condition
Race conditions ocorrem quando múltiplas threads acessam e manipulam dados compartilhados simultaneamente, podendo causar comportamentos imprevisíveis e erros lógicos no sistema.

Neste simulador:
- Uma conta bancária começa com saldo de R$1000
- Múltiplos clientes (executando em threads separadas) tentam realizar saques
- Sem mecanismos de proteção, os clientes conseguem sacar mais dinheiro do que realmente existe na conta

## 🧠 Conceitos Demonstrados
- **Threads**: Execução simultânea de múltiplos fluxos de código
- **Race conditions**: Falhas devido a acessos concorrentes não sincronizados
- **Seções críticas**: Partes do código que acessam recursos compartilhados
- **Janela de vulnerabilidade**: Intervalo entre verificação e atualização de um valor

## 💡 Como Funciona
A simulação cria uma conta bancária e múltiplos clientes que tentam sacar valores entre R$300 e R$500. O método de saque:

1. Verifica se há saldo disponível
2. Espera um pouco (simulando processamento)
3. Atualiza o saldo

Durante esta pausa, outras threads podem verificar o saldo e também iniciar saques, resultando em uma sobrecarrega do sistema onde o total sacado ultrapassa o saldo disponível.

## 📊 Resultados Esperados
Ao executar o script, você deverá observar:
- Múltiplos clientes realizando saques "bem-sucedidos"
- Um total sacado maior que R$1000 (o saldo inicial)
- Possivelmente um saldo final negativo

Estes resultados comprovam a existência da race condition e a necessidade de mecanismos de sincronização.

## 🚀 Como Executar
```bash
python ThreadedBankSimulator.py
```

## 📝 Licença
Este projeto é disponibilizado como recurso educacional de código aberto.