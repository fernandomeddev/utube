# Utube API & Client

Este repositório contém a **API** construída com **Flask** para processar URLs do YouTube, além de um **cliente front-end** para gerenciar e visualizar vídeos. O projeto foi desenvolvido para armazenar informações de vídeos do YouTube usando o framework **pytube**, e a API gerencia URLs enquanto o front-end permite a interação com esses dados.

## Estrutura do Projeto

```
root
│
├── api/          # Diretório contendo a API Flask (backend)
│   ├── app/      # Arquivos do aplicativo Flask
│   ├── migrations/ # Migrações de banco de dados
│   ├── venv/     # Ambiente virtual (não incluído no repositório)
│   └── ...       # Outros arquivos relacionados à API
│
└── client/       # Diretório contendo o front-end (React)
    ├── src/      # Código-fonte do front-end
    └── public/   # Arquivos estáticos e index.html
```

### Pré-requisitos

Certifique-se de ter as seguintes dependências instaladas:

- **Python 3.8+**
- **Node.js & npm** (para o cliente)
- **Git**

### Passos para clonar o repositório e configurar

#### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/utube.git
```

#### 2. Acesse o diretório da API:

```bash
cd utube/api
```

#### 3. Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

#### 4. Instale as dependências:

```bash
pip install -r requirements.txt
```

#### 5. Configure o banco de dados:

Se você estiver usando o **Flask-Migrate** para gerenciar migrações, execute os seguintes comandos para configurar o banco de dados:

```bash
flask db init
flask db migrate
flask db upgrade
```

#### 6. Execute o servidor da API:

```bash
flask run
```

A API será iniciada em: `http://127.0.0.1:5000`

---

## Configuração do Front-end (Client)

#### 1. Acesse o diretório do cliente:

```bash
cd ../client
```

#### 2. Instale as dependências:

```bash
npm install
```

#### 3. Execute o aplicativo React:

```bash
npm start
```

O front-end será iniciado em: `http://localhost:3000`

---

## Funcionalidades da API

A API permite:

- **Adicionar URLs do YouTube**: Ao fornecer uma URL válida do YouTube, a API armazena informações detalhadas sobre o vídeo.
- **Listar URLs**: Recupera todas as URLs cadastradas com informações sobre os vídeos.
- **Deletar URLs**: Remove um vídeo do sistema pelo seu ID.
- **Visualizar informações detalhadas**: Retorna dados de um vídeo específico a partir de seu ID.

### Exemplo de Endpoints

- `GET /urls`: Lista todas as URLs.
- `POST /urls`: Adiciona uma nova URL do YouTube.
- `DELETE /urls/<id>`: Remove uma URL pelo ID.

---

## Possíveis Melhorias Futuras

Aqui estão algumas sugestões para aprimoramentos futuros:

### Técnicas

1. **Autenticação e Autorização**:
   - Implementar login e autenticação JWT para proteger os endpoints.
   - Adicionar autenticação OAuth para login com Google/YouTube.

2. **Tratamento de Erros**:
   - Melhorar o tratamento de exceções e criar mensagens de erro mais detalhadas.
   - Implementar uma camada de logging para monitoramento da aplicação.

3. **Testes Automatizados**:
   - Adicionar testes unitários e de integração para a API (utilizando `pytest` ou outra ferramenta).
   - Implementar testes end-to-end no front-end para verificar a interação entre o cliente e a API.

4. **Otimizações de Banco de Dados**:
   - Melhorar o design do banco de dados para suportar grandes volumes de vídeos.
   - Implementar cache para reduzir o tempo de resposta de consultas frequentes.

### Produto

1. **Sistema de Categorias**:
   - Adicionar categorias para os vídeos, permitindo filtragem por tema.

2. **Playlists**:
   - Criar funcionalidades para que os usuários possam organizar vídeos em playlists.

3. **Comentários e Likes**:
   - Implementar a possibilidade de os usuários comentarem e curtirem os vídeos, simulando uma experiência parecida com o YouTube.

4. **Interface de Pesquisa**:
   - Adicionar uma barra de pesquisa para buscar vídeos salvos com base em títulos, autores ou descrições.

5. **Dashboard de Analytics**:
   - Criar uma área para visualizar métricas, como os vídeos mais populares, views totais, e outras estatísticas.

---

## Contribuindo

Se você quiser contribuir com este projeto, por favor siga estas instruções:

1. Faça um fork do projeto.
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4. Envie para o repositório remoto (`git push origin feature/nova-funcionalidade`).
5. Abra um pull request.

---

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Contato

Se tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato:

- **E-mail**: seu-email@exemplo.com
- **GitHub**: [github.com/seu-usuario](https://github.com/seu-usuario)

--- 

### Observação:
Lembre-se de ajustar os links e o nome do projeto para refletirem o nome real do seu repositório e as suas informações de contato.