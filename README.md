# 📊 Análise de Vendas Internacionais

## 🎯 Contexto e Objetivo
Este projeto foi desenvolvido a partir de um dataset contendo **541.909 registros de vendas globais** de uma **loja online internacional**.  
O objetivo principal foi **transformar a base bruta de dados** em **insights estratégicos** para apoiar decisões sobre:

- Produtos mais relevantes para o negócio.
- Comportamento e perfil dos clientes.
- Padrões de sazonalidade e tendências de compra.
- Identificação de mercados promissores para **expansão internacional**.

---

## 🛠️ Metodologia

### **1. Tratamento e Limpeza dos Dados (Python 🐍)**
- Padronização e renomeação de colunas.
- Conversão e ajuste de tipos de dados.
- Exclusão de nulos em nomes de produtos.
- Substituição de IDs de clientes ausentes por **cliente_desconhecido**.
- Criação da coluna **tipo_transacao** (Compra/Devolução).
- Remoção de duplicatas.
- Tratamento de **outliers** via método IQR.

### **2. Modelagem e Criação de KPIs (Power BI + DAX)**
- **KPIs principais:**
  - Receita Bruta
  - Receita Líquida
  - Volume Total de Vendas
  - Ticket Médio
- Criação de **rankings**:
  - Top 5 produtos por receita.
  - Top 5 produtos por volume de vendas.

### **3. Visualizações e Dashboard**
- **KPIs principais**: Receita Bruta, Receita Líquida, Devoluções e Ticket Médio.
- **Evolução mensal da Receita Líquida** (linha temporal).
- **Comparativo Compras vs Devoluções** (pizza).
- **Top 5 Produtos** por Receita e Volume (barras).
- **Receita Líquida por País** (mapa global).

---

## 📊 Principais Resultados

- **Receita Bruta:** R$ 926 Mi  
- **Receita Líquida:** R$ 905,25 Mi  
- **Devoluções:** apenas **2,17%** do volume total.  
- **Evolução Temporal:** queda em fevereiro, com crescimento expressivo entre **setembro e novembro** (pico de **R$ 98,83 Mi**).  
- **Produtos:**  
  - Receita concentrada em **itens premium** (ex.: *Regency Cakestand 3 T*).  
  - Volume puxado por **produtos de baixo valor e alto giro** (ex.: *World War 2 Gliders*, *Popcorn Holder*).  
- **Clientes/Pedidos:**  
  - Ticket médio por cliente: **R$ 207,34 mil**.  
  - Ticket médio por pedido: **R$ 38,58 mil**.  
- **Mercados:**  
  - **Europa concentra a maior receita** — destaque para o **Reino Unido**.  
  - **EUA** e **Austrália** aparecem como mercados secundários.  
  - **Ásia, América do Sul e África** são pouco explorados.

---

## 🧩 Recomendações Estratégicas

1. **Consolidar mercados maduros**: fidelização e retenção na Europa/Reino Unido.
2. **Expandir em mercados secundários**: campanhas segmentadas para EUA e Austrália.
3. **Explorar mercados emergentes**: produtos de baixo valor e alto volume como porta de entrada.
4. **Gestão de portfólio**:  
   - **Itens premium** → foco em exclusividade e branding.  
   - **Produtos de giro** → promoções e estratégias de **cross-sell**.
5. **Monitoramento contínuo**: incluir métricas de margem e acompanhamento de devoluções.

---

## 📂 Estrutura do Repositório

```
analise-vendas-internacionais/
├── data/          → Dataset tratado (.csv)
├── scripts/       → Códigos Python (.py, .ipynb)
├── dashboard/     → Arquivo .pbix e prints do Power BI
├── docs/          → Relatório executivo (.pdf)
└── README.md
```

---

## 🖼️ Dashboard Interativo

![Dashboard Preview](dashboard/dashboard_preview.png)

> **[Acesse o dashboard completo aqui](link-do-power-bi-service)** *(se publicado no Power BI Service)*

---

## 🧠 Competências Demonstradas
- **Python** → tratamento, limpeza e análise de dados.
- **Power BI + DAX** → modelagem de indicadores e criação de KPIs.
- **Storytelling com dados** → tradução de métricas em **insights acionáveis**.
- **Produção de relatório executivo** para **tomada de decisão**.

---

## 👨‍💻 Autor
**Caio Henrique**  
📌 [LinkedIn](https://linkedin.com/in/seu-perfil) • [Portfólio no GitHub](https://github.com/seu-usuario)
