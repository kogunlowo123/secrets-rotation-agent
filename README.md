# Secrets Rotation Agent

[![CI](https://github.com/kogunlowo123/secrets-rotation-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/secrets-rotation-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: DevOps & Platform Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Automated secrets lifecycle agent that manages credential rotation schedules, detects leaked secrets in code and logs, enforces secret hygiene policies, integrates with vault systems, and provides emergency rotation capabilities for compromised credentials.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `rotate_secret` | Rotate a secret according to its rotation policy |
| `scan_for_leaks` | Scan repositories and logs for exposed secrets |
| `audit_secret_age` | Audit secrets approaching or exceeding rotation deadline |
| `emergency_rotate` | Emergency rotation of potentially compromised credentials |
| `check_rotation_status` | Check rotation status and history for a secret |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/secrets/rotate` | Rotate a secret |
| `POST` | `/api/v1/secrets/scan` | Scan for leaked secrets |
| `GET` | `/api/v1/secrets/audit` | Audit secret ages |
| `POST` | `/api/v1/secrets/emergency-rotate` | Emergency rotation |
| `GET` | `/api/v1/secrets/{secret_id}/status` | Check rotation status |

## Features

- Automated Rotation
- Leak Detection
- Policy Enforcement
- Vault Integration
- Emergency Rotation

## Integrations

- Hashicorp Vault
- Aws Secrets Manager
- Azure Key Vault
- Gcp Secret Manager
- Gitleaks

## Architecture

```
secrets-rotation-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── secrets_rotation_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**HashiCorp Vault + AWS Secrets Manager + Azure Key Vault**

---

Built as part of the Enterprise AI Agent Platform.
