# Projeto em Python com Makefile

Este projeto utiliza `Makefile` para facilitar a execução de comandos comuns, como instalação de dependências, execução do servidor e gerenciamento de pacotes Python.

## Pré-requisitos

1. **Python 3.10 ou superior**  
   Certifique-se de que você tem a versão mínima do Python instalada. O Makefile verifica automaticamente a versão do Python.

2. **Dependências**  
   Antes de rodar o projeto, instale as dependências listadas em `requirements.txt`.

---

## Comandos Disponíveis

### 1. **Rodar o Projeto**
Inicie o servidor utilizando o Uvicorn:
```bash
make run
```

### 2. Instalar Dependências
```bash
make install
```

### 3. Adicionar um Novo Pacote
```bash
make install-package package=<nome_do_pacote>
# exemplo
make install-package package=fastapi
```
