# Projeto-Agil-TechFlow-Solutions
# Sistema de Gerenciamento de Tarefas

## Descrição do Projeto

Este projeto foi desenvolvido como atividade da disciplina de Engenharia de Software do curso de Análise e Desenvolvimento de Sistemas. A proposta consiste na criação de um sistema web básico de gerenciamento de tarefas, aplicando conceitos de desenvolvimento ágil, versionamento de código, testes automatizados e integração contínua.

O sistema simula uma solução desenvolvida pela empresa fictícia **TechFlow Solutions** para atender uma startup do setor de logística, permitindo o gerenciamento e acompanhamento das atividades da equipe de forma organizada e eficiente.

---

## Objetivo

O principal objetivo deste projeto é aplicar, na prática, os conceitos estudados durante a disciplina, utilizando ferramentas e metodologias empregadas no desenvolvimento profissional de software.

Além da implementação do sistema, o projeto busca demonstrar a utilização de controle de versões, organização das tarefas, testes automatizados e integração contínua, seguindo boas práticas da Engenharia de Software.

---

## Escopo

O sistema possui como funcionalidade principal o gerenciamento de tarefas por meio de operações básicas de CRUD (Create, Read, Update e Delete), permitindo cadastrar, visualizar, editar e excluir tarefas.

O escopo deste projeto contempla apenas as funcionalidades essenciais para demonstrar a aplicação dos conceitos da disciplina, não incluindo recursos avançados como autenticação de usuários, banco de dados em nuvem ou controle de permissões.

---

## Mudança de Escopo

Durante o desenvolvimento foi identificada a necessidade de adicionar uma nova funcionalidade ao sistema: a marcação de tarefas como concluídas.

A funcionalidade foi implementada após o planejamento inicial do projeto, simulando uma alteração de requisito durante o ciclo de desenvolvimento, situação comum em projetos reais de software.


## Metodologia Utilizada

Este projeto foi desenvolvido utilizando os princípios das metodologias ágeis, adotando o **Kanban** como método de gerenciamento das atividades.

As tarefas foram organizadas no GitHub Projects utilizando três etapas principais:

* **To Do** – tarefas planejadas;
* **In Progress** – tarefas em desenvolvimento;
* **Done** – tarefas concluídas.

O versionamento do projeto foi realizado utilizando **Git**, enquanto o repositório foi hospedado no **GitHub**. Todas as alterações foram registradas por meio de commits descritivos, permitindo acompanhar toda a evolução do desenvolvimento.

Também foram implementados testes automatizados e um pipeline de Integração Contínua (CI) utilizando **GitHub Actions**, garantindo a validação automática do sistema sempre que novas alterações são enviadas ao repositório.

---

## Tecnologias Utilizadas

* Python
* Flask
* Git
* GitHub
* GitHub Projects (Kanban)
* GitHub Actions
* Pytest

---

## Estrutura do Projeto

```text
Projeto/
│
├── src/
│   ├── app.py
│   └── ...
│
├── tests/
│   └── test_app.py
│
├── docs/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Como Executar o Projeto

1. Clone este repositório.
2. Instale as dependências do projeto.
3. Execute a aplicação.
4. Acesse o sistema pelo navegador utilizando o endereço informado pelo servidor local.

---

## Mudança de Escopo

Durante o desenvolvimento foi simulada uma alteração no escopo do projeto, representando uma situação comum em metodologias ágeis.

Inicialmente, o sistema possuía apenas as funcionalidades básicas de gerenciamento de tarefas. Posteriormente, foi adicionada uma nova funcionalidade para melhorar a experiência do usuário, atendendo a uma necessidade identificada durante o desenvolvimento.

Essa alteração foi registrada no quadro Kanban, implementada em um novo commit e documentada neste README, demonstrando a capacidade de adaptação às mudanças ao longo do ciclo de desenvolvimento.

---

## Controle de Qualidade

Para garantir maior confiabilidade ao sistema, foram implementados testes automatizados responsáveis por validar funcionalidades essenciais da aplicação.

Além disso, foi configurado um pipeline de Integração Contínua utilizando GitHub Actions, que executa automaticamente os testes sempre que uma alteração é enviada ao repositório, contribuindo para a manutenção da qualidade do código.

---

## Autor

**Reinaldo Rocha**

Trabalho desenvolvido para a disciplina de Engenharia de Software – Curso de Análise e Desenvolvimento de Sistemas.
