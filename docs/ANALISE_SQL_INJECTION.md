# GuardAI — Análise defensiva do laboratório SQL Injection

**Escopo:** `agent/app.py`, banco SQLite **em memória**, usuários e credenciais **fictícios**. Teste local autorizado e exclusivamente educacional.

## Contexto e evidência

Em `vulnerable_login`, os parâmetros `username` e `password` são interpolados diretamente em uma string SQL. Isso permite que caracteres da entrada sejam interpretados como parte da sintaxe SQL.

O laboratório usa uma entrada fixa de treinamento para demonstrar a diferença:
- `vulnerable_login` retorna `True` com senha incorreta, evidenciando o desvio lógico;
- `secure_login` usa placeholders `?` do SQLite, retornando `False` para a mesma entrada;
- login legítimo continua funcionando na versão segura.

## Classificação contextual

| Aspecto | Avaliação |
| --- | --- |
| Achado | SQL Injection na função didática `vulnerable_login` |
| Evidência | Interpolação de strings e comparação de resultados no laboratório |
| Impacto potencial em aplicação real | Acesso não autorizado e comprometimento de confidencialidade/integridade, conforme privilégios e arquitetura |
| Probabilidade em aplicação real | Dependente da exposição do endpoint, controles, autenticação e permissões; não calculada para um sistema real |
| Severidade potencial em produção | Pode ser alta, dependendo do contexto e dados afetados |
| Risco atual deste laboratório | Baixo: execução local e isolada, banco em memória e dados fictícios |
| Disponibilidade | Sem impacto demonstrado no experimento |

A classificação é **qualitativa e contextual**; não foi calculado escore CVSS.

## Correção e validação

`secure_login` separa estrutura SQL de dados recebidos através da parametrização:
```python
result = connection.execute(
    "SELECT id FROM users WHERE username = ? AND password = ?",
    (username, password),
).fetchone()
```

Três testes automatizados verificam login legítimo, rejeição de senha incorreta e comparação do comportamento vulnerável versus parametrizado. O terminal da participante exibiu **3 testes, 3 aprovados (`OK`)** em 08/11/2026.

A mitigação do **caso demonstrado** está validada; isso **não** equivale a auditar um aplicativo real.

## Recomendações adicionais

- Eliminar a construção de SQL com entradas concatenadas.
- Usar usuário do banco com menor privilégio.
- Em aplicações reais, armazenar senhas com algoritmo de hash de senhas apropriado e sal; nunca em texto puro.
- Cobrir entradas não confiáveis com testes automatizados de regressão.
- Revisar autenticação, autorização, tratamento de erros e observabilidade.

## Limites

Nenhuma aplicação externa foi acessada, nenhum dado real foi utilizado e nenhuma exploração fora do laboratório foi realizada. A função vulnerável permanece **intencionalmente** no projeto para fins comparativos.
