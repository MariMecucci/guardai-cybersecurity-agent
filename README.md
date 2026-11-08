# 🤖 DIO Agent

> Seu mentor com Inteligência Artificial para aprender mais e melhor na [DIO](https://dio.me).

O **DIO Agent** é um agente de IA que acompanha você na sua jornada de estudos. Ele conhece as experiências da DIO (Bootcamps, Formações, Cursos, Desafios e muito mais) e ajuda você a estudar, praticar e planejar a sua carreira.

Você não precisa saber programar nem instalar nada complicado. Em **3 passos**, o seu mentor está pronto para usar.

---

## ✨ Três palavras para começar

- 🧠 **Agente de IA:** um chatbot responde perguntas. Um *agente* vai além: lê, planeja e executa passos para ajudar você a alcançar um objetivo. É a diferença entre alguém que explica o caminho e alguém que caminha junto com você.
- 🖥️ **Harness:** é o programa onde o agente roda. O agente é o mentor, e o harness é a sala onde vocês se encontram. O mesmo mentor atende em salas diferentes, por isso o DIO Agent funciona em vários harnesses.
- 🧩 **Skill:** é uma habilidade do agente, descrita em um guia passo a passo. Você não precisa chamar a skill: o agente percebe o que você precisa e usa a certa sozinho.

Esses e outros termos estão no [Glossário](docs/glossary.md).

---

## 🚀 Comece em 3 passos

### 1️⃣ Instale um harness

Recomendamos o **Google Antigravity**, que tem limites de uso generosos para quem está começando. Mas qualquer harness da lista funciona: escolha um e siga a instalação da documentação oficial dele.

| Harness | Documentação oficial |
|---------|----------------------|
| Google Antigravity (recomendado) | https://antigravity.google/docs |
| Claude Code | https://code.claude.com/docs |
| Codex | https://developers.openai.com/codex |
| OpenCode | https://opencode.ai/docs |
| Hermes | https://hermes-agent.nousresearch.com/docs |

### 2️⃣ Baixe o DIO Agent e abra no harness

Baixe este repositório do jeito mais simples para você:

- **Com Git:** no terminal, rode `git clone https://github.com/digitalinnovationone/dio-agent.git`
- **Sem Git:** no topo desta página, clique no botão verde **Code**, depois em **Download ZIP**, e extraia a pasta.

Depois, abra no harness a pasta do projeto, a que tem o arquivo `AGENTS.md` (pelo Git, ela se chama `dio-agent`; pelo .zip, `dio-agent-main`). O harness lê esse arquivo sozinho, e o agente já sabe quem é: o seu mentor de estudos da DIO.

### 3️⃣ Converse

Fale naturalmente, com as suas palavras. Nas primeiras vezes, vale usar um dos [modelos de prompt](#-modelos-de-prompt) abaixo: quanto mais contexto você dá, melhor o agente ajuda.

---

## 🧩 As skills do agente

| Skill | Para que serve | Experimente pedir |
|-------|----------------|-------------------|
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo | "Quero concluir este Bootcamp em 2 meses, me ajuda?" |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz você até a solução de um desafio, sem dar a resposta pronta | "Travei nesse desafio, me ajuda?" |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma simples, com analogias e exemplos | "Não entendi o que é uma API." |
| [Pesquisa na web](skills/web-search/SKILL.md) | Responde dúvidas atuais (versões, lançamentos, mercado) com fontes citadas | "Qual a versão estável do Node hoje?" |
| [Revisão de portfólio](skills/portfolio-review/SKILL.md) | Dá feedback sobre o seu portfólio e GitHub antes de buscar vagas | "O que falta no meu GitHub para uma vaga júnior?" |
| [Caminho AI Builder](skills/ai-builder-path/SKILL.md) | Ajuda você a escolher o próximo passo na Carreira AI Builder | "Qual Formação AI Builder combina comigo?" |
| [Análise de Vulnerabilidades](skills/vulnerability-analysis/SKILL.md) | Analisa vulnerabilidades, avalia riscos e orienta correções defensivas | "Pode analisar a segurança deste código Python?" |

A pesquisa na web usa a busca do seu harness. Se ele não tiver busca própria, veja [como conectar o You.com](docs/youcom-mcp.md), que tem uma opção gratuita.

---

## 📝 Modelos de prompt

Copie, preencha o que está entre colchetes e envie. Não precisa de formato perfeito: o agente pede mais detalhes se precisar.

**🗺️ Plano de estudos**

```
Quero montar um plano de estudos.
- Meu objetivo: [ex: ser dev back-end, concluir um Bootcamp]
- O que quero fazer na DIO: [link ou nome do Bootcamp, Formação, Aceleração ou Carreira]
- O que já tenho: [um plano de ação ou de estudos, se tiver]
- Meu nível hoje: [iniciante, intermediário, avançado]
- Tempo disponível: [ex: 1 hora por dia, de segunda a sexta]
```

**🔓 Destravar desafio**

```
Estou travado em um Desafio de [Código, Projeto ou Criativo] da DIO.
- O que o desafio pede: [cole o enunciado ou, no Desafio de Projeto, o link do repositório do desafio]
- Onde eu travei: [explique o ponto da dificuldade]
- Meu código ou repositório: [cole o código ou o link, se tiver]
Me ajuda a destravar sem dar a resposta pronta.
```

**💡 Explicar conceito**

```
Me explica o conceito de [ex: API, laço de repetição, herança].
- Meu nível: [nunca vi, já ouvi falar, quero aprofundar]
```

**🧭 Caminho AI Builder**

```
Quero escolher meu próximo passo na Carreira AI Builder.
- O que quero construir com IA: [ex: um produto para o meu negócio, um software, agentes que automatizam processos, ainda não sei]
- Minha experiência com programação: [nenhuma, o básico, trabalho com desenvolvimento]
- Meu objetivo: [ex: mudar de carreira, tirar uma ideia do papel]
```

---

## 🔄 Mantenha o DIO Agent atualizado

O DIO Agent evolui com o tempo. Se você usou Git, rode `git pull` no terminal, dentro da pasta (ou peça para o próprio agente rodar). Se baixou o .zip, baixe de novo.

---

## 🗂️ Estrutura do repositório

```
dio-agent/
├── README.md                Este guia
├── AGENTS.md                Definição do agente (lida pelo harness)
├── CLAUDE.md                Atalho para o Claude Code
├── agent/
│   ├── persona.md           A personalidade e o tom do agente
│   └── knowledge/           O que o agente sabe sobre a DIO
├── skills/                  Uma pasta por skill, cada uma com o seu SKILL.md
└── docs/
    ├── glossary.md          Glossário de termos
    └── youcom-mcp.md        Como conectar a busca do You.com
```

---

## 🤝 Contribua

Tem uma ideia de skill? Veja [como criar uma skill](skills/README.md) e abra um pull request.

---

## 💬 Sobre este projeto

O DIO Agent foi criado para acompanhar você nos Bootcamps e Formações da DIO. A ideia é simples: aprender na era da IA fica mais fácil quando você tem um mentor disponível a qualquer hora.

Bons estudos, e vem com a gente. 🚀


---

# GuardAI — Cybersecurity & Vulnerability Analysis Agent

**Projeto educacional DIO / Santander Cybersecurity** · Extensão do [DIO Agent original](https://github.com/digitalinnovationone/dio-agent).

## Visão geral

GuardAI é uma especialização defensiva do DIO Agent, baseada em instruções Markdown, base de conhecimento e uma nova skill de análise de vulnerabilidades. O objetivo é conduzir uma investigação com **contexto, evidências, impacto, probabilidade, severidade, correção e validação**, sem confundir uma hipótese com uma vulnerabilidade confirmada.

Este projeto **não treina um novo modelo**. O comportamento do agente depende de um *harness* de IA que leia o `AGENTS.md` e os arquivos associados.

### Entregáveis

| Componente | Caminho |
| --- | --- |
| Registro da skill | [AGENTS.md](AGENTS.md) |
| Persona especializada | [agent/persona.md](agent/persona.md) |
| Fundamentos de segurança | [security-basics.md](agent/knowledge/security-basics.md) |
| Metodologia de análise | [SKILL.md](skills/vulnerability-analysis/SKILL.md) |
| Laboratório SQLite | [app.py](agent/app.py) |
| Testes automatizados | [test_app.py](tests/test_app.py) |
| Evidências de testes | [docs/VALIDACAO_GUARDAI.md](docs/VALIDACAO_GUARDAI.md) |
| Relatório defensivo | [docs/ANALISE_SQL_INJECTION.md](docs/ANALISE_SQL_INJECTION.md) |
| Submissão DIO | [docs/ENTREGA_DIO.md](docs/ENTREGA_DIO.md) |

## Laboratório educacional de SQL Injection

Executado **somente em memória** com `sqlite3` e usuários fictícios. A implementação apresenta, no mesmo arquivo, uma consulta com concatenação insegura e uma consulta corrigida com parâmetros (`?`). Uma entrada fixa de demonstração é usada apenas no banco de teste local. Nenhuma aplicação externa é acessada.

> **Não utilize o código vulnerável em produção.** As senhas simples são fixtures fictícias; aplicações reais exigem hash de senhas e controles adicionais.

### Pré-requisitos

Python 3.10+; não há dependências Python externas para o laboratório.

Execute na raiz do repositório:

```powershell
py agent\app.py
py -m unittest discover -s tests -v
```

Em Linux/macOS, use `python3 agent/app.py` e `python3 -m unittest discover -s tests -v`.

### Resultado observado na sessão DIO (08/11/2026)

```text
=== GUARDAI SECURITY LAB ===
Normal login: True
Vulnerable query accepted input: True
Secure query accepted input: False
Security comparison: PASSED
Parameterized query mitigation: VERIFIED
Environment: LOCAL AND ISOLATED
```

Os **três testes automatizados** também retornaram `ok` (3/3, `OK`) no VS Code. Os dados foram **observados em capturas de tela**, não provenientes de logs originais arquivados no GitHub. Veja [Validação](docs/VALIDACAO_GUARDAI.md).

## Como usar a especialização no agente

Abra a **pasta raiz do repositório** em um harness compatível com `AGENTS.md` (por exemplo, o modo Agent do GitHub Copilot no VS Code, conforme disponibilidade de sua conta). Solicite:

> Analise a SQL Injection demonstrada em `agent/app.py`. Antes de sugerir alterações, pergunte sobre ambiente e autorização. Use `skills/vulnerability-analysis/SKILL.md` e `agent/knowledge/security-basics.md`. Avalie impacto, probabilidade, severidade, correção e validação. Não modifique arquivos.

O teste apresentado utilizou **GitHub Copilot no VS Code**, não o Hermes. Foi observada a leitura dos quatro arquivos de instrução, perguntas de contexto e autorização, identificação inicial de SQL Injection e a execução de testes locais. Não foi arquivado um relatório conversacional final completo; consulte [limitações da validação](docs/VALIDACAO_GUARDAI.md).

## Segurança e limitações

- Ambiente local, banco SQLite em memória, usuários e credenciais sintéticos.
- Nenhum teste realizado contra serviços públicos ou ambientes de produção.
- A demonstração compara **um caso específico** e não constitui auditoria completa de segurança.
- O uso com agentes deve exigir confirmação humana antes de qualquer edição de arquivo ou comando.
- O código vulnerável é intencional para fins didáticos.

## Origem e créditos

Este trabalho deriva do projeto [DIO Agent, da Digital Innovation One](https://github.com/digitalinnovationone/dio-agent). Os materiais originais, a estrutura e suas skills foram preservados; as seções GuardAI, a skill de AppSec, a base de segurança e o laboratório foram adicionados como extensão educacional. Este repositório é uma adaptação de estudante, **não o projeto oficial da DIO**.

**English summary:** GuardAI extends the DIO Agent with an AppSec-focused vulnerability-analysis skill, a cybersecurity knowledge base, an isolated SQLite SQL injection lab, and three documented passing automated tests.
