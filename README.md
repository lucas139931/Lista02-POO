# 🐍 Programação Orientada a Objetos em Python

> Coleção de sistemas educacionais implementados com **ABC**, **Protocol** e **Polimorfismo** — do contrato formal ao estrutural.

---

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Pré-requisitos](#pré-requisitos)
- [Como executar](#como-executar)
- [Sistema 01 — Mídias Educacionais](#sistema-01--mídias-educacionais)
- [Sistema 02 — Funcionários da Empresa](#sistema-02--funcionários-da-empresa)
- [Sistema 03 — Notificações com ABC](#sistema-03--notificações-com-abc)
- [Sistema 04 — Impressão com Protocol](#sistema-04--impressão-com-protocol)
- [Sistema 05 — Armazenamento ABC vs Protocol](#sistema-05--armazenamento-abc-vs-protocol)
- [Conceitos aplicados](#conceitos-aplicados)

---

## Visão Geral

Cada sistema é autocontido e demonstra um conceito progressivo de POO:

| # | Sistema | Conceito principal |
|---|---|---|
| 01 | Mídias Educacionais | ABC + polimorfismo básico |
| 02 | Funcionários | ABC + cálculo polimórfico |
| 03 | Notificações | ABC como contrato formal |
| 04 | Impressão | Protocol + duck typing |
| 05 | Armazenamento | ABC vs Protocol lado a lado |

---

## Pré-requisitos

- Python **3.10** ou superior
- Nenhuma dependência externa — apenas biblioteca padrão

Verifique sua versão:

```bash
python --version
```

---

## Como executar

Clone o repositório e entre na pasta do sistema desejado:

```bash
git clone https://github.com/seu-usuario/poo-python.git
cd poo-python
```

Cada sistema fica em sua própria pasta. Para rodar qualquer um:

```bash
cd sistema-XX
python main.py
```

---

## Sistema 01 — Mídias Educacionais

### Descrição

Plataforma educacional que organiza e reproduz diferentes tipos de conteúdo. Demonstra hierarquia de classes com `ABC` e polimorfismo via `reproduzir_todas()`.

### Estrutura

```
sistema-01/
├── main.py          ← ponto de entrada
├── midia.py         ← classe abstrata Midia
├── midias.py        ← Video, Podcast, TextoNarrado
└── plataforma.py    ← classe Plataforma
```

### Hierarquia

```
Midia  (ABC)
├── Video           + resolucao
├── Podcast         + apresentador
└── TextoNarrado    + idioma
```

### Executar

```bash
cd sistema-01
python main.py
```

### Saída esperada

```
📥 Adicionando mídias à plataforma...
  ✔ 'Introdução à POO' adicionado(a) com sucesso.
  ...

==================================================
  Plataforma: EduLearn +
  Total de mídias: 6
==================================================

  [1] [🎬 Vídeo]
  Título  : Introdução à Programação Orientada a Objetos
  Duração : 45.0 min
  Resolução: 1080p
  ...

▶  Reproduzindo vídeo 'Introdução à POO' em 1080p...
🎧 Reproduzindo podcast 'Boas Práticas em Python' com Ana Lima...
🔊 Reproduzindo texto narrado 'Conceitos de Algoritmos' no idioma Português...
```

### Conceitos

| Elemento | Onde aparece |
|---|---|
| Classe abstrata | `Midia` em `midia.py` |
| Herança | `Video(Midia)`, `Podcast(Midia)`, `TextoNarrado(Midia)` |
| Polimorfismo | `reproduzir_todas()` em `plataforma.py` |

---

## Sistema 02 — Funcionários da Empresa

### Descrição

Sistema de folha de pagamento com três regras de cálculo distintas. O método `mostrar_folha_pagamento()` percorre todos os funcionários e calcula o pagamento de cada um sem nenhum `if/elif`.

### Estrutura

```
sistema-02/
├── main.py           ← ponto de entrada
├── funcionario.py    ← classe abstrata Funcionario
├── funcionarios.py   ← FuncionarioAssalariado, FuncionarioHorista, FuncionarioComissionado
└── empresa.py        ← classe Empresa
```

### Hierarquia

```
Funcionario  (ABC)
├── FuncionarioAssalariado    pagamento = salario_mensal
├── FuncionarioHorista        pagamento = horas × valor_hora
└── FuncionarioComissionado   pagamento = vendas × (comissao / 100)
```

### Executar

```bash
cd sistema-02
python main.py
```

### Saída esperada

```
📋 Registrando funcionários na empresa...
  ✔ Ana Souza adicionado(a) com sucesso.
  ...

====================================================
  💰 FOLHA DE PAGAMENTO — TechSolve Ltda.
====================================================
  Ana Souza                      R$   6.500,00
  Bruno Lima                     R$   4.800,00
  Carla Neves                    R$   5.600,00
  Daniel Rocha                   R$   5.100,00
  Elena Costa                    R$   6.800,00
  Fábio Martins                  R$   5.500,00
────────────────────────────────────────────────────
  TOTAL A PAGAR                  R$  34.300,00
====================================================
```

### Conceitos

| Elemento | Onde aparece |
|---|---|
| Classe abstrata | `Funcionario` em `funcionario.py` |
| Sobrescrita | `calcular_pagamento()` em cada subclasse |
| Polimorfismo | `mostrar_folha_pagamento()` em `empresa.py` |

---

## Sistema 03 — Notificações com ABC

### Descrição

Central de notificações que dispara mensagens simultaneamente por e-mail, SMS e app. Demonstra ABC como contrato formal e polimorfismo via `enviar_para_todos()`.

### Estrutura

```
sistema-03/
├── main.py           ← ponto de entrada
├── notificador.py    ← classe abstrata Notificador
├── notificadores.py  ← NotificadorEmail, NotificadorSMS, NotificadorApp
└── central.py        ← classe CentralNotificacoes
```

### Hierarquia

```
Notificador  (ABC)
├── NotificadorEmail    + endereco_email
├── NotificadorSMS      + numero_telefone
└── NotificadorApp      + nome_usuario
```

### Executar

```bash
cd sistema-03
python main.py
```

### Saída esperada

```
📋 Registrando canais na central...
  ✔ NotificadorEmail registrado com sucesso.
  ✔ NotificadorSMS registrado com sucesso.
  ✔ NotificadorApp registrado com sucesso.

==================================================
  📣 Disparando para 3 canal(is)...
==================================================

  📧 [E-MAIL] → joao.silva@email.com
     Mensagem : Sua assinatura foi renovada com sucesso!

  📱 [SMS] → +55 92 91234-5678
     Mensagem : Sua assinatura foi renovada com sucesso!

  🔔 [APP] → @joao.silva
     Mensagem : Sua assinatura foi renovada com sucesso!

  ✅ Mensagem enviada para todos os 3 canal(is).
```

### Conceitos

| Elemento | Onde aparece |
|---|---|
| Classe abstrata | `Notificador` em `notificador.py` |
| Contrato formal | `@abstractmethod notificar()` |
| Polimorfismo | `enviar_para_todos()` em `central.py` |

---

## Sistema 04 — Impressão com Protocol

### Descrição

Fila de impressão que processa boletos, etiquetas e relatórios. Usa `Protocol` em vez de `ABC` — as classes **não precisam herdar nada** para serem compatíveis.

### Estrutura

```
sistema-04/
├── main.py          ← ponto de entrada e testes
├── imprimivel.py    ← Protocol Imprimivel
├── documentos.py    ← Boleto, Etiqueta, RelatorioSimples
└── impressao.py     ← função processar_impressao()
```

### Compatibilidade estrutural

```
Protocol Imprimivel  →  exige: imprimir()

Boleto           ✅  tem imprimir()  (sem herdar)
Etiqueta         ✅  tem imprimir()  (sem herdar)
RelatorioSimples ✅  tem imprimir()  (sem herdar)
ClasseQualquer   ✅  tem imprimir()  (duck typing puro)
```

### Executar

```bash
cd sistema-04
python main.py
```

### Saída esperada

```
  ── Documento 1 de 3 ─────────────────────────

  ┌─────────────────────────────────────────┐
  │           🧾 BOLETO BANCÁRIO            │
  ├─────────────────────────────────────────┤
  │  Código : 34191.09008 63521.560079 ...  │
  │  Valor  : R$ 250,00                     │
  └─────────────────────────────────────────┘
  ...

  ✅ 3 documento(s) processado(s) com sucesso.
```

### Conceitos

| Elemento | Onde aparece |
|---|---|
| Contrato estrutural | `Protocol Imprimivel` em `imprimivel.py` |
| Duck typing | Classes sem herança aceitas em `processar_impressao()` |
| Polimorfismo | `processar_impressao(item)` em `impressao.py` |

---

## Sistema 05 — Armazenamento ABC vs Protocol

### Descrição

O mesmo problema — salvar dados em destinos diferentes — resolvido de **duas formas** no mesmo projeto. Compara diretamente o que cada abordagem aceita ou rejeita.

### Estrutura

```
sistema-05/
├── main.py           ← comparação e testes lado a lado
├── armazenador.py    ← ABC: Armazenador, ArmazenadorArquivo, ArmazenadorBanco
├── salvavel.py       ← Protocol: Salvavel, ArmazenadorNuvem
└── funcoes.py        ← executar_salvamento_formal() e executar_salvamento_flexivel()
```

### Comparativo

```
                        Formal (ABC)    Flexível (Protocol)
ArmazenadorArquivo         ✅ aceita        ✅ aceita
ArmazenadorBanco           ✅ aceita        ✅ aceita
ArmazenadorNuvem           ❌ rejeita       ✅ aceita
LoggerExterno              ❌ rejeita       ✅ aceita
```

### Executar

```bash
cd sistema-05
python main.py
```

### Saída esperada

```
======================================================
  PARTE A — executar_salvamento_formal()  [ABC]
======================================================

  ── ArmazenadorArquivo (herda de Armazenador) ───────

  💾 [ARQUIVO]  → /var/log/app/eventos.log
     Salvando  : "{'usuario': 'ana.souza', ...}"
     Status    : gravado em disco com sucesso.
  ...
  ❌ Erro esperado : 'ArmazenadorNuvem' não pertence à hierarquia de Armazenador.

======================================================
  PARTE B — executar_salvamento_flexivel()  [Protocol]
======================================================

  ☁️  [NUVEM]    → bucket 'empresa-dados-prod' (sa-east-1)
     Salvando  : "{'usuario': 'ana.souza', ...}"
     Status    : upload concluído com sucesso.
  ✔  Aceito sem herdar nada — apenas por ter salvar().
```

### Conceitos

| Elemento | Onde aparece |
|---|---|
| Contrato por herança | `ABC Armazenador` em `armazenador.py` |
| Contrato estrutural | `Protocol Salvavel` em `salvavel.py` |
| Rigidez do ABC | `isinstance()` em `executar_salvamento_formal()` |
| Flexibilidade do Protocol | `executar_salvamento_flexivel()` aceita qualquer um |

---

## Conceitos aplicados

### ABC vs Protocol — quando usar cada um

| Critério | ABC | Protocol |
|---|---|---|
| Você controla as classes | ✅ ideal | funciona |
| Classes de libs externas | ❌ não se aplica | ✅ ideal |
| Erro detectado em | instanciação | chamada do método |
| Verificação | runtime | análise estática (mypy) |
| Acoplamento | alto | baixo |
| Herança necessária | sim | não |

### Glossário rápido

**ABC (Abstract Base Class)** — classe que não pode ser instanciada diretamente e exige que subclasses implementem métodos marcados com `@abstractmethod`.

**Protocol** — define um contrato estrutural: qualquer classe que possua os métodos esperados é compatível, independente de herança.

**Polimorfismo** — mesmo código chamando métodos em objetos de tipos diferentes, com comportamentos distintos para cada tipo.

**Duck typing** — "se anda como pato e grasna como pato, é um pato." O Python não verifica o tipo, verifica se o método existe.

**Sobrescrita (override)** — subclasse redefine um método da superclasse com sua própria implementação.

---

> Desenvolvido como material de estudo de Programação Orientada a Objetos em Python.
