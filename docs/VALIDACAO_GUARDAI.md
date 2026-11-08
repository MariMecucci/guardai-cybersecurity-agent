# Registro de validação do GuardAI

**Data da sessão:** 08/11/2026  
**Ambiente apresentado:** Windows, VS Code, Python 3.14, SQLite em memória, GitHub Copilot.

> **Proveniência:** resultados foram observados em capturas do VS Code durante o desenvolvimento do desafio. Este documento é um registro transcrito dos resultados vistos; os screenshots originais **não foram enviados ao GitHub**.

## 1. Laboratório em Python

Comando (raiz do projeto):
```powershell
py agent\app.py
```

Saída observada **depois de reverter alterações automáticas do Copilot**:

```text
=== GUARDAI SECURITY LAB ===
Normal login: True
Vulnerable query accepted input: True
Secure query accepted input: False
Security comparison: PASSED
Parameterized query mitigation: VERIFIED
Environment: LOCAL AND ISOLATED
```

## 2. Testes automatizados

Comando:
```powershell
py -m unittest discover -s tests -v
```

Resultado observado:
```text
test_invalid_login (...) ... ok
test_sql_injection_mitigation (...) ... ok
test_valid_login (...) ... ok

Ran 3 tests in 0.001s

OK
```

Os testes anteriores também passaram em outras execuções apresentadas no terminal da participante.

## 3. Teste conversacional do agente

O harness utilizado foi **GitHub Copilot (VS Code)**, **não Hermes**, que não estava disponível no terminal (`hermes` retornou `CommandNotFoundException`).

O que foi visto no chat:
1. Leitura de `AGENTS.md`, `agent/persona.md`, `agent/knowledge/security-basics.md` e `skills/vulnerability-analysis/SKILL.md`.
2. Perguntas iniciais sobre ambiente, autorização, comportamento suspeito e dados envolvidos.
3. Reconhecimento do contexto de laboratório local autorizado.
4. Análise inicial apontando SQL Injection em `vulnerable_login`.
5. Execução dos testes locais com resultados aprovados.
6. Uma opção automática de 'Fix all issues' chegou a alterar arquivos. A participante desfez as alterações e executou novamente os testes; os resultados originais foram recuperados.

**Limite da evidência:** não foi arquivada uma resposta final completa do agente com toda a matriz de risco. Não afirmar que o relatório conversacional completo ou o Hermes foram validados.

## 4. Como reproduzir

1. Clone este repositório.
2. Execute `py agent\app.py` e `py -m unittest discover -s tests -v`.
3. Abra a raiz no harness compatível com `AGENTS.md`.
4. Peça análise **somente leitura**, delimitando ambiente e autorização.
5. Verifique se o agente pede contexto, diferencia evidência e hipótese, propõe parametrização e recomenda validação.
6. Registre capturas reais (sem dados pessoais) caso o avaliador exija evidência visual.

Todos os exemplos ficam em ambiente controlado, com dados fictícios.
