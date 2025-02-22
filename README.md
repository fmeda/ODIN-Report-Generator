# ODIN Report Generator

**ODIN Report Generator** é uma ferramenta de geração de relatórios personalizada, voltada para profissionais de TI, que visa simplificar a coleta, análise e exportação de dados de ferramentas de monitoramento e segurança open source como **Zabbix**, **Grafana**, **Wazuh**, **Graylog** e **Suricata**.

Esta ferramenta permite a geração de relatórios dinâmicos, onde o usuário pode definir parâmetros como IPs de servidores, períodos de tempo e formatos de exportação (CSV ou Power BI). Os relatórios podem ser gerados diretamente da interface gráfica do frontend ou por meio de requisições à API.

## Funcionalidades

- Geração automatizada de relatórios a partir de dados extraídos de ferramentas de monitoramento (Zabbix, Grafana) e segurança (Wazuh, Graylog, Suricata).
- Suporte a dois formatos de exportação: **CSV** e **Power BI**.
- Interface gráfica intuitiva construída com **React**.
- Backend robusto com **FastAPI**, garantindo uma comunicação eficiente com as ferramentas de monitoramento.
- Exportação de relatórios para fácil integração com ferramentas de análise de dados como **Power BI**.
- Agendamento de relatórios via **APScheduler**.
- Sistema de log para registro de falhas e informações importantes sobre a execução dos relatórios.

## Estrutura do Projeto

- **Backend**:
  - **FastAPI**: Responsável pelo gerenciamento de requisições, autenticação e geração de relatórios.
  - **APScheduler**: Para agendamento de tarefas e execução periódica de relatórios.
  - **Serviços**: Conecta-se aos sistemas de monitoramento (Zabbix, Grafana, Wazuh, Graylog, Suricata) para extração de dados.
  - **Exportação**: Suporte para exportação de relatórios nos formatos CSV e Power BI.

- **Frontend**:
  - **React**: Interface gráfica para interação com o usuário e geração de relatórios.
  - **Material UI**: Framework de componentes para criar uma interface visualmente agradável e intuitiva.

## Requisitos

### Backend:
- Python 3.x
- FastAPI
- Uvicorn
- APScheduler
- Pandas

### Frontend:
- Node.js (para React)
- npm (ou yarn)

## Instalação

### Backend

1. Clone o repositório do projeto:
   ```bash
   git clone https://github.com/seu-usuario/odin-report-generator.git
   cd odin-report-generator
