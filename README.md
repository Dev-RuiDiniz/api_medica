# 🏥 API de Agendamento Médico (medical-appointment-api)

## 🎯 Descrição do Projeto

Esta API RESTful é o *backend* de um sistema de agendamento de consultas médicas. Construída com **Django 6.0** e **Django REST Framework (DRF)**, a aplicação utiliza **PostgreSQL** como banco de dados principal e é empacotada com **Docker Compose** para garantir um ambiente de desenvolvimento isolado e replicável.

### 🔑 Tecnologias Principais

* **Backend:** Python 3.12, Django 6.0, Django REST Framework.
* **Gerenciamento de Dependências:** Poetry.
* **Banco de Dados:** PostgreSQL 16 (via Docker).
* **Contêineres:** Docker e Docker Compose.

## 🔐 Segurança e Autenticação

A API utiliza **Token-Based Authentication**. Todos os endpoints (exceto o de login) exigem um token válido no cabeçalho das requisições.

### 1. Como obter um Token de Acesso
Envie uma requisição `POST` para `/api-token-auth/` com suas credenciais de usuário:

**Endpoint:** `POST /api-token-auth/`  
**Body (JSON):**
```json
{
    "username": "seu_usuario",
    "password": "sua_senha"
}