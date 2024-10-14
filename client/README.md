# Video Playlist Application - README

## Descrição

Este é um projeto de uma aplicação web para criar, visualizar e gerenciar uma playlist de vídeos do YouTube. Os usuários podem adicionar URLs de vídeos, visualizar informações sobre os vídeos e remover vídeos da lista. A aplicação utiliza React para o frontend e se conecta a uma API para gerenciar a lista de URLs.

## Funcionalidades

- **Adicionar vídeos**: Insira uma URL do YouTube e adicione vídeos à playlist.
- **Visualizar vídeos**: Exibe o título, autor e outras informações dos vídeos.
- **Remover vídeos**: Opção de excluir vídeos da playlist.
- **Modal de vídeo**: Ao selecionar um vídeo, ele é exibido em um modal, com a possibilidade de fechá-lo.
- **Notificações**: Feedback para ações como adicionar, excluir ou falha ao processar URLs, usando `react-toastify`.

## Tecnologias utilizadas

- **React.js**: Biblioteca principal para construção da interface.
- **React Toastify**: Para exibir notificações de feedback.
- **Axios ou Fetch API**: Para realizar chamadas à API e gerenciar as URLs.
- **CSS**: Estilização responsiva com base na paleta de cores do Nest.js.
- **Font Awesome**: Ícones de ações.

---

## Instruções para rodar o projeto localmente

### Pré-requisitos

- Node.js (v14 ou superior)
- NPM (gerenciador de pacotes do Node.js)
- Git (opcional, caso deseje clonar o projeto)

### Passo a passo

1. **Clone o repositório (opcional):**

   Se você deseja clonar o projeto usando Git, rode o seguinte comando no terminal:

   ```bash
   git clone https://github.com/seu-usuario/video-playlist-app.git
   ```

2. **Instale as dependências:**

   Acesse o diretório do projeto e execute o seguinte comando para instalar as dependências necessárias:

   ```bash
   npm install
   ```

3. **Inicie o servidor de desenvolvimento:**

   Após a instalação das dependências, execute o seguinte comando para iniciar a aplicação em ambiente de desenvolvimento:

   ```bash
   npm start
   ```

   A aplicação estará acessível no navegador pelo endereço: `http://localhost:3000`

4. **Build para produção (opcional):**

   Se quiser gerar os arquivos otimizados para produção, execute o comando:

   ```bash
   npm run build
   ```

   Isso irá gerar os arquivos na pasta `build`, que podem ser servidos em um servidor estático.

---

## Sugestões de melhorias

### 1. Melhorias técnicas

- **Autenticação e Autorização**:
  - Implementar autenticação para que os usuários possam fazer login e salvar suas playlists de forma personalizada.
  - Sugestão: Uso de OAuth para integração com Google ou Facebook, ou JWT para autenticação própria.

- **Cache**:
  - Adicionar cache local (por exemplo, com `localStorage` ou `sessionStorage`) para evitar chamadas desnecessárias à API ao recarregar a página.
  - Sugestão: Utilizar o `SW` (Service Worker) para cachear respostas da API e otimizar o tempo de carregamento.

- **Segurança**:
  - Implementar validação mais robusta para URLs inseridas pelos usuários para evitar ataques de injeção de código.
  - Usar HTTPS sempre e garantir que a aplicação utilize headers de segurança como `Content-Security-Policy` e `X-Content-Type-Options`.
  - Rate-limiting para prevenir abuso de endpoints, caso o projeto escale.

- **Teste de Performance**:
  - Adicionar métricas de desempenho e otimizações para carregamento de vídeos, como a integração com uma CDN para servir arquivos estáticos.
  - Melhorar a performance com `Lazy Loading` para vídeos e outros componentes.

- **Melhoria da API**:
  - Implementar paginação na API para listas grandes de vídeos, caso o número de URLs cresça de maneira significativa.
  - Adicionar suporte a métodos `PATCH` na API, para atualizar as informações dos vídeos de forma granular.

### 2. Melhorias no produto

- **Criação de categorias**:
  - Implementar categorias ou tags para os vídeos, permitindo que os usuários classifiquem suas playlists por gênero (por exemplo: música, tecnologia, tutoriais).
  - Criar filtros de pesquisa por categorias.

- **Sistema de Favoritos**:
  - Permitir que os usuários marquem vídeos como "favoritos" e criem várias listas personalizadas.
  - Exibir uma playlist especial com os vídeos favoritos.

- **Compartilhamento de playlist**:
  - Implementar uma funcionalidade de compartilhamento de playlists via link, permitindo que outros usuários acessem e vejam as playlists de vídeos.

- **Melhorias na interface de usuário (UI)**:
  - Implementar temas personalizados (modo claro/escuro).
  - Adicionar animações sutis ao adicionar e remover vídeos para melhorar a experiência do usuário.

- **Comentários e avaliações**:
  - Permitir que os usuários comentem em vídeos ou deem avaliações, criando uma experiência mais interativa e comunitária.

- **Integração com YouTube API**:
  - Utilizar a API oficial do YouTube para obter automaticamente informações detalhadas dos vídeos, como miniaturas, número de curtidas e tempo de duração.

---

Essas sugestões de melhorias visam aumentar a usabilidade, segurança, performance e a experiência geral dos usuários com o aplicativo.