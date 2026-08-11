# Bot Agregador de Notícias IA/TI

## Objetivo

Construir uma aplicação backend completa (API + worker + entrega via Telegram) que sirva como projeto-vitrine para vagas de backend júnior e DevOps júnior, cobrindo desde arquitetura de API até pipeline de CI/CD e deploy.

---

## Escopo funcional (MVP)

|Funcionalidade|Descrição|
|---|---|
|Fetch de RSS|Job agendado busca notícias de feeds de IA/TI configuráveis|
|Deduplicação|Evita reprocessar notícias já enviadas (hash da URL/título no banco)|
|Sumarização via LLM|Usa Groq para gerar resumo curto de cada notícia|
|Persistência|Salva notícia + resumo + status de envio no PostgreSQL|
|Entrega|Envia resumo formatado para um canal/grupo do Telegram|
|API de consulta|Endpoints REST para listar notícias, filtrar por data/fonte, buscar por palavra-chave|
|Autenticação|JWT para proteger endpoints administrativos (ex: adicionar/remover feed)|

### Fora do MVP (backlog futuro, não travar o lançamento nisso)

- Múltiplos canais de entrega (Slack, e-mail)
- Interface web
- Classificação por relevância/score

---

## Arquitetura

```
[APScheduler job] → busca RSS → [Groq API] → resumo
        ↓
   [PostgreSQL] ← persiste notícia
        ↓
   [Telegram Bot API] → entrega ao usuário

[FastAPI app] → endpoints REST → [PostgreSQL]
```

Dois processos lógicos separados:
- **Worker** — scheduler, fetch RSS, sumarização e entrega via Telegram
- **API** — FastAPI expondo os dados já persistidos via endpoints REST

## Stack técnica

|Camada|Tecnologia|
|---|---|
|API|FastAPI + Pydantic v2|
|ORM|SQLAlchemy 2.0 (async, asyncpg)|
|Banco|PostgreSQL|
|Scheduler|APScheduler|
|LLM|Groq API|
|Entrega|python-telegram-bot ou requests direto na Bot API|
|Testes|pytest + pytest-asyncio|
|Qualidade|SonarCloud|
|Segurança|Trivy (scan de imagem Docker)|
|Container|Docker + Docker Compose|
|CI/CD|GitHub Actions|
|Deploy|Railway ou Fly.io (free tier) — ou VPS com Compose, se quiser praticar infra manual|

---

## Fases de execução

### Fase 1 — Core funcional (backend puro)

- [ ] Modelagem do banco (tabela feeds, noticias, envios)
- [ ] Migrations com Alembic
- [ ] Job de fetch RSS + parsing
- [ ] Integração com Groq para sumarização
- [ ] Integração com Telegram Bot API
- [ ] Deduplicação funcionando ponta a ponta

### Fase 2 — API REST

- [ ] Endpoints CRUD de feeds (protegidos por JWT)
- [ ] Endpoints de consulta de notícias (públicos, com paginação e filtros)
- [ ] Testes automatizados (unitários + pelo menos 1 teste de integração com banco de teste)
- [ ] Documentação OpenAPI caprichada (descrições, exemplos de resposta)

### Fase 3 — Containerização

- [ ] Dockerfile multi-stage para a API
- [ ] Dockerfile para o worker
- [ ] docker-compose.yml orquestrando API + worker + PostgreSQL
- [ ] Variáveis sensíveis via .env (nunca commitado — .env.example no repo)

### Fase 4 — Pipeline CI/CD (o diferencial DevOps)

- [ ] Workflow GitHub Actions: lint (ruff/flake8) → testes (pytest) → SonarCloud
- [ ] Etapa de build das imagens Docker
- [ ] Scan de vulnerabilidade com Trivy nas imagens buildadas
- [ ] Push das imagens para um registry (GitHub Container Registry é o mais simples)
- [ ] Deploy automático no merge para main (Railway/Fly.io via CLI, ou webhook)

### Fase 5 — Observabilidade (opcional, mas forte diferencial)

- [ ] Endpoint /health e /ready
- [ ] Logging estruturado (JSON logs)
- [ ] Métricas básicas expostas para Prometheus (contagem de envios, erros de fetch)

---

## Ordem de prioridade recomendada

Fase 1 → Fase 2 → Fase 3 → Fase 4 → (Fase 5 se sobrar fôlego).

Não pule para o CI/CD antes de ter o core funcional estável — pipeline testando código que ainda muda toda hora é retrabalho.