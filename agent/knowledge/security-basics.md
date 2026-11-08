# GuardAI — Security Knowledge Base

## Objetivo

Fornecer fundamentos de cibersegurança para o agente analisar vulnerabilidades, avaliar riscos e orientar correções e testes em ambientes autorizados.

## Conceitos fundamentais

- **Vulnerabilidade:** fraqueza técnica ou de processo que pode ser explorada.
- **Ameaça:** evento, ação ou agente com potencial de causar dano.
- **Risco:** combinação do impacto potencial com a probabilidade do cenário.
- **Exploração:** uso de uma falha para obter comportamento não autorizado.
- **Evidência:** observação reproduzível que sustenta um achado; uma hipótese, sozinha, não confirma uma vulnerabilidade.

## Tríade CIA

- **Confidencialidade:** acesso à informação restrito a pessoas ou sistemas autorizados.
- **Integridade:** proteção contra alterações indevidas.
- **Disponibilidade:** acesso aos sistemas e dados quando necessário.

## Vulnerabilidades frequentes

### SQL Injection

Inserção não confiável incorporada diretamente a consultas SQL, permitindo alterar a lógica da consulta.

**Riscos:** leitura indevida de dados, modificações ou autenticação burlada, conforme o contexto.

**Mitigação:** consultas parametrizadas, menor privilégio no banco e testes de regressão. Não confundir filtragem simples com parametrização.

### Cross-Site Scripting (XSS)

Conteúdo não confiável interpretado no navegador como código executável.

**Mitigação:** codificação de saída contextual, tratamento apropriado do conteúdo e CSP como camada adicional.

### Broken Access Control

Ausência de validação de autorização no servidor para operações e recursos.

**Mitigação:** autorização em todas as operações relevantes, menor privilégio, testes com papéis distintos e políticas explícitas.

### Security Misconfiguration

Configurações inseguras, recursos desnecessários ou credenciais padrão ampliam a superfície de ataque.

**Mitigação:** hardening, atualização, segregação de ambientes e revisão contínua.

### Authentication Failures

Mecanismos fracos de autenticação, sessões ou recuperação de acesso.

**Mitigação:** hash de senhas adequado, MFA, gerenciamento seguro de sessões e proteção contra abuso.

## Avaliação de riscos

Para cada cenário, documente:
1. Ativo e componente afetados.
2. Causa raiz e evidência.
3. Possível impacto sobre confidencialidade, integridade e disponibilidade.
4. Probabilidade contextual (baixa, média, alta).
5. Severidade contextual (baixa, média, alta, crítica).
6. Mitigação e evidências de verificação.

Atribua pontuações CVSS somente com métricas suficientes. **Risco em laboratório isolado** é diferente do risco de uma falha semelhante em produção.

## Boas práticas de AppSec e DevSecOps

- Secure coding e revisão de código.
- Menor privilégio e defesa em profundidade.
- Análise de dependências e atualização de software.
- Testes automatizados e verificações de regressão.
- Gestão de vulnerabilidades, logs e resposta a incidentes.
- Separação entre hipóteses, testes executados e resultados comprovados.
- Aprovação humana antes de modificações automatizadas em arquivos ou sistemas.

## Fluxo recomendado do GuardAI

Entender o contexto → confirmar autorização → reunir evidências → classificar o risco → orientar a correção → validar em laboratório → documentar resultados e limitações.

## Referências reconhecidas

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP Web Security Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
- MITRE CWE: https://cwe.mitre.org/
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- FIRST CVSS: https://www.first.org/cvss/

## Limitações e ética

Não realizar testes fora do escopo autorizado, não solicitar dados reais e não declarar achados como confirmados sem evidências.
