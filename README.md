# UTUBE Application - README

## Descrição
Este é um projeto de uma aplicação web para criar, visualizar e gerenciar uma playlist de vídeos do YouTube. Os usuários podem adicionar URLs de vídeos, visualizar e remover os vídeos da lista. A aplicação utiliza **React** no frontend e se conecta a uma **API** construída em **Flask** (python) para gerenciar a lista de URLs.

---

## Funcionalidades

- **Adicionar vídeos**: Insira uma URL do YouTube e adicione vídeos à playlist.
- **Visualizar vídeos**: Na Página inicial Exibe a lista de urls caso exista alguma url salva.
- **Remover vídeos**: Opção de excluir vídeos da playlist.
- **Modal de vídeo**: Ao selecionar um vídeo, ele é exibido em um modal, com a possibilidade de fechá-lo.
- **Notificações**: Feedback para ações como adicionar, excluir ou falha ao processar URLs, usando `react-toastify`.
- **Video Player**: Ao Selecionar uma url é possivel assistir o video sem precisar ser redirecionado para o YOUTUBE.
  
---

## Tecnologias utilizadas

### Frontend

- **React.js**: Biblioteca principal para construção da interface.
- **React Toastify**: Para exibir notificações de feedback.
- **Axios ou Fetch API**: Para realizar chamadas à API e gerenciar as URLs.
- **CSS**: Estilização responsiva com base no tema Dracula.
- **Font Awesome**: Ícones de ações.

### Backend (API)
- **Flask**: Microframework Python para construção da API.
- **SQLAlchemy**: ORM para banco de dados relacional.
- **Pytube**: Biblioteca para manipulação e extração de informações de vídeos do YouTube.
- **Flask-Migrate**: Para gerenciar migrações de banco de dados.

---

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

---

## Instruções para rodar o projeto localmente

### Usando React.js (para o frontend) e Python/Flask (para a API)

#### Pré-requisitos

- Node.js (v14 ou superior)
- NPM (gerenciador de pacotes do Node.js)
- Python 3.10+
- Flask
- Git (opcional, caso deseje clonar o projeto)

### Passo a passo

1. **Clone o repositório:**

   Se você deseja clonar o projeto usando Git, rode o seguinte comando no terminal:

   ```bash
   git clone https://github.com/fernandomeddev/utube.git
   ```

2. **Instale as dependências do frontend (React):**

   Acesse o diretório do projeto frontend e execute o seguinte comando para instalar as dependências:

   ```bash
   cd client
   npm install
   ```

3. **Iniciando o frontend Localmente:**

   Após a instalação das dependências, execute o seguinte comando para iniciar o frontend em ambiente de desenvolvimento:

   ```bash
   npm start
   ```

   A aplicação estará acessível no navegador pelo endereço: `http://localhost:3000`.

4. **Instale as dependências do backend (Flask):**
   Agora, volte para o diretório principal do projeto e entre no diretório da API:

   ```bash
   cd ../api
   ```

   Instale as dependências do Python com o `pip`:

   ```bash
   pip install -r requirements.txt
   ```

5. **Inicie a API Flask:**

   Execute o seguinte comando para iniciar a API:

   ```bash
   flask run
   ```

   A API estará disponível em `http://localhost:5000`.

---

## Usando Docker

Se você preferir usar Docker para executar o projeto, siga as instruções abaixo:

### Pré-requisitos

- Docker instalado na sua máquina.

### Passo a passo para rodar com Docker

1. **Clone o repositório (opcional):**

   Se você deseja clonar o projeto usando Git, rode o seguinte comando no terminal:

   ```bash
   git clone https://github.com/fernandomeddev/utube.git
   ```

2. **Construir a imagem Docker da API Flask:**

   No diretório da API, execute o seguinte comando para construir a imagem:

   ```bash
   cd api
   docker build -t video-playlist-api .
   ```

3. **Rodar o contêiner da API Flask:**

   Execute o comando para rodar o contêiner e expor a porta `5000`:

   ```bash
   docker run -d -p 5000:5000 video-playlist-api
   ```

   Agora, a API estará disponível em `http://localhost:5000`.

4. **Rodar o frontend com Docker (opcional):**

   Caso queira rodar o frontend também com Docker, você pode criar um `Dockerfile` ou usar o ambiente local conforme as instruções anteriores. Para o frontend, o Dockerfile não foi incluído neste exemplo, mas você pode configurá-lo facilmente.

---

## Sugestões de melhorias

### 1. Melhorias técnicas

- **Autenticação e Autorização**: Implementar autenticação para que os usuários possam fazer login e salvar suas playlists de forma personalizada (OAuth ou JWT).
- **Cache**: Adicionar cache local (`localStorage` ou `sessionStorage`) para evitar chamadas desnecessárias à API.
- **Segurança**: Implementar validação mais robusta para URLs e usar HTTPS e headers de segurança.
- **Teste de Performance**: Adicionar otimizações como `Lazy Loading` para vídeos.
- **Melhoria da API**: Implementar paginação na API para listas grandes de vídeos.

### 2. Melhorias no produto

- **Criação de categorias**: Implementar categorias ou tags para os vídeos.
- **Sistema de Favoritos**: Permitir que os usuários marquem vídeos como favoritos.
- **Compartilhamento de playlist**: Implementar uma funcionalidade de compartilhamento de playlists via link.
- **Melhorias na interface de usuário (UI)**: Implementar temas personalizados (modo claro/escuro) e animações sutis.

---

Essas sugestões de melhorias visam aumentar a usabilidade, segurança, performance e a experiência geral dos usuários com o aplicativo.

--- 

Com essas instruções, o usuário poderá rodar o projeto tanto localmente quanto utilizando Docker.

---

### Passo a passo para o Frontend (Client)

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

#### 4. Build para produção (opcional):

Para gerar os arquivos otimizados para produção, execute:

```bash
npm run build
```

---

## Funcionalidades da API

### Principais Endpoints

- `GET /urls`: Lista todas as URLs salvas.
- `POST /urls`: Adiciona uma nova URL do YouTube.
- `DELETE /urls/<id>`: Remove uma URL pelo ID.

### Exemplo de Resposta da API

**Adicionar uma URL:**

- **POST** `/urls`

```json
{
  "success": true,
  "data": {
    "id": 1,
    "title": "Título do Vídeo",
    "description": "Descrição do Vídeo",
    "views": 12345,
    "publish_date": "2021-08-01",
    "author": "Nome do Autor",
    "length": 600,
    "watch_url": "https://youtube.com/watch?v=abc123"
  }
}
```

**Listar URLs:**

- **GET** `/urls`

```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "title": "Título do Vídeo",
      "description": "Descrição do Vídeo",
      "views": 12345,
      "publish_date": "2021-08-01",
      "author": "Nome do Autor",
      "length": 600,
      "watch_url": "https://youtube.com/watch?v=abc123"
    }
  ]
}
```

---

## Sugestões de melhorias

### Melhorias técnicas

1. **Autenticação e Autorização**:
   - Implementar login e autenticação JWT para proteger os endpoints.
   - Adicionar autenticação OAuth para login com Google/YouTube.

2. **Cache**:
   - Utilizar `localStorage` ou `sessionStorage` para armazenar vídeos localmente.
   - Implementar cache de respostas da API.

3. **Segurança**:
   - Implementar validação robusta para as URLs.
   - Utilizar HTTPS e cabeçalhos de segurança.

4. **Paginação**:
   - Adicionar paginação na listagem de vídeos para melhorar a performance.

---

### Melhorias no Produto

1. **Categorias e Tags**:
   - Adicionar a funcionalidade de categorizar vídeos.

2. **Sistema de Favoritos**:
   - Permitir aos usuários favoritar vídeos.

3. **Compartilhamento de Playlist**:
   - Permitir que os usuários compartilhem suas playlists.

4. **Melhorias na Interface (UI)**:
   - Implementar modo claro/escuro.
   - Adicionar animações e transições visuais.

---

## Licença

Este projeto está sob a licença MIT.

## Contato

Se tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato:

- **E-mail**: fernandohenrique520@live.com
- **GitHub**: [github.com/seu-usuario](https://github.com/fernandomeddev)

---

Documentação unificada com a descrição, funcionalidades, tecnologias e melhorias tanto da API quanto do front-end, guia completo para configuração, execução e entendimento do projeto.