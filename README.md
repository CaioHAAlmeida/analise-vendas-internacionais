# 📊 Análise de Vendas Internacionais

## 🎯 Contexto e Objetivo
Este projeto foi desenvolvido a partir de um dataset contendo **541.909 registros de vendas globais** de uma **loja online internacional**.  
O objetivo principal foi **transformar a base bruta** em **insights estratégicos** para apoiar decisões sobre:

- Produtos mais relevantes para o negócio.
- Comportamento e perfil dos clientes.
- Padrões de sazonalidade e tendências de compra.
- Identificação de mercados promissores para **expansão internacional**.

---

## 📂 Estrutura do Repositório

```
analise-vendas-internacionais/
├── data/           → Dataset de exemplo para teste
├── scripts/        → Códigos Python para análise e tratamento
├── dashboard/      → Prints e arquivos do Power BI
├── docs/           → Relatórios e documentação técnica
└── README.md       → Documentação do projeto
```

---

## 🛠️ Metodologia

### **1. Tratamento e Limpeza de Dados (Python 🐍)**
- Padronização e renomeação de colunas.
- Conversão e ajuste de tipos de dados.
- Exclusão de nulos em nomes de produtos.
- Substituição de IDs de clientes ausentes por **cliente_desconhecido**.
- Criação da coluna **tipo_transacao** (Compra/Devolução).
- Remoção de duplicatas.
- Tratamento de **outliers** via método IQR.

### **2. Modelagem e KPIs (Power BI + DAX)**
- **KPIs principais:**
  - Receita Bruta
  - Receita Líquida
  - Volume Total de Vendas
  - Ticket Médio
- Criação de **rankings**:
  - Top 5 produtos por receita.
  - Top 5 produtos por volume.

### **3. Visualizações e Dashboard**
- KPIs principais.
- Evolução mensal da Receita Líquida.
- Comparativo Compras vs Devoluções.
- Top 5 Produtos por Receita e Volume.
- Receita Líquida por País.

---

## 📊 Principais Resultados

- **Receita Bruta:** R$ 926 Mi  
- **Receita Líquida:** R$ 905,25 Mi  
- **Devoluções:** apenas **2,17%** do volume total.  
- **Evolução Temporal:** crescimento expressivo entre setembro e novembro.  
- **Produtos:** receita concentrada em **itens premium** e volume em produtos de **alto giro**.  
- **Mercados:** Europa domina a receita, com **Reino Unido** em destaque.

---

## 📂 Dataset

Para manter o repositório leve, disponibilizei **uma amostra do dataset** na pasta `data/`.

O **dataset completo**, com **541.909 registros**, está hospedado no OneDrive:

🔗 [Clique aqui para acessar o dataset completo](https://1drv.ms/x/c/d972abcb724b4029/EfDnWJ1GAFCvZm82yjL5_oBE-aNjZ3h2TQnyYrY59OJtA?e=yG2064)

---

## 🖼️ Dashboard Interativo

![Dashboard Preview](dashboard/dashboard_preview.png)

> **[Acesse o dashboard completo aqui](link-do-power-bi-service)** *(se publicado no Power BI Service)*

---

## 🧠 Competências Demonstradas
- **Python** → tratamento, limpeza e análise de dados.
- **Power BI + DAX** → modelagem de indicadores e KPIs.
- **Storytelling com dados** → transformar números em **insights acionáveis**.
- **Produção de relatório executivo** para suporte à decisão.

---

## 👨‍💻 Autor
**Caio Henrique**  
📌 [LinkedIn](https://linkedin.com/in/seu-perfil) • [Portfólio no GitHub](https://github.com/seu-usuario)
