
# 🌊 Argolas Aquáticas (Waterful Ring Toss)

Uma recriação nostálgica em Python/Pygame do clássico brinquedo aquático dos anos 90, desenvolvida com física de fluidos simulada e síntese procedural de áudio em tempo real — sem necessidade de assets externos.

![Demonstração do Jogo](screenshots/gameplay.png)

---

## 🎯 Destaques Técnicos

- **Física e Dinâmica de Fluidos:** Simulação de arrasto hidrodinâmico, empuxo, correntes de jato vetoriais e amortecimento de colisão para reproduzir o comportamento de objetos flutuando na água.
- **Síntese de Áudio Procedural:** Sons sintetizados matematicamente via `array` de ondas (senoidais e quadradas com modulação de frequência e ruído branco) integrados diretamente ao `pygame.mixer`, dispensando arquivos `.wav` ou `.mp3`.
- **Renderização Gráfica Vetorial:** Toda a interface gráfica, tanque, peixes, bolhas e reflexos são gerados em tempo de execução via primitivas do Pygame e cálculos trigonométricos.
- **Mecânica de Jogo Completa:** Sistema de pontuação balanceado com combos temporizados, argolas especiais (ouro x3), tempo regressivo, fases progressivas e persistência de recorde local (`highscore`).

---

## 🎮 Controles

| Ação | Teclado | Mouse |
| :--- | :--- | :--- |
| **Jato Esquerdo** | `Seta Esquerda` ou `Z` | Clique no botão azul |
| **Jato Direito** | `Seta Direita` ou `M` | Clique no botão vermelho |
| **Ambos os Jatos** | `Barra de Espaço` | — |
| **Pausar** | `P` | — |
| **Reiniciar / Novo Jogo** | `R` | Clique na tela (telas de menu/fim) |
| **Sair** | `ESC` | Fechar janela |

---

## 🕹️ Regras do Jogo

- **Objetivo:** Acertar as argolas nos pinos antes do cronômetro zerar.
- **Pinos Laterais:** 100 pontos.
- **Pino Central:** 300 pontos.
- **Argola Dourada:** Multiplica o valor do encaixe por 3.
- **Combos:** Encaixes consecutivos dentro da janela de tempo concedem multiplicadores de até 5x.

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.10 ou superior instalado.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/argolas-aquaticas.git](https://github.com/SEU_USUARIO/argolas-aquaticas.git)
   cd argolas-aquaticas
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/macOS:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie o jogo:**
   ```bash
   python argolas_aquaticas.py
   ```

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Biblioteca Multimídia:** Pygame
- **Módulos Nativos:** `math`, `random`, `array`, `sys`, `os`

---

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais detalhes.
4. Dicas para Destacar no GitHub
Grave um GIF de gameplay: Use ferramentas leves como o ScreenToGif (Windows) para gravar 5 a 10 segundos de partida. Salve dentro da pasta screenshots/ e aponte no topo do README. O apelo visual aumenta significativamente as visitas.

Tags (Topics) do Repositório: No menu lateral do GitHub ("About"), adicione tags como: python, pygame, game-development, procedural-audio, 2d-physics, retro-games.

Seção de Projetos no Perfil: Fixe o repositório na tela inicial do seu perfil do GitHub marcando-o como Pinned.

ou colocar aqui no novo repositorio

Preencha os campos dessa tela da seguinte forma:   
PNG

1. Geral
Nome do repositório: argolas-aquaticas

   
PNG

Descrição:

Jogo retrô inspirado no clássico brinquedo aquático dos anos 90, desenvolvido em Python/Pygame com física de fluidos e áudio procedural.

   
PY
+ 1

2. Configuração
Escolha visibilidade: Mantenha marcado como Público (necessário para compor o portfólio visível a todos).   
PNG

Inicialização:

Add a README file: Deixe desmarcado (caso vá subir os arquivos direto do computador via terminal/Git, para evitar conflitos de branch). Se preferir criar os arquivos direto pelo navegador no GitHub, pode marcar.

Add .gitignore: Deixe como None (já temos o modelo pronto) ou escolha o template Python.

Choose a license: Selecione MIT License.

Clique no botão verde Criar repositório (ou Create repository) no final da página.

Subindo os arquivos pelo terminal (VS Code / Git Bash)
Na pasta onde está o arquivo argolas_aquaticas.py:   
PY

Bash
git init
git add .
git commit -m "feat: versão inicial do jogo Argolas Aquáticas"
git branch -M main
git remote add origin https://github.com/Edinaldo-long/argolas-aquaticas.git
git push -u origin main
   
PNG
+ 1
(Lembre-se também de habilitar a autenticação de dois fatores [2FA] na sua conta antes do prazo indicado no aviso amarelo no topo para evitar restrições de acesso).   
PNG

Sou uma IA baseada em texto, então não consigo ajudar com isso.

está certo o preencimento?

O preenchimento está quase todo correto, mas há um detalhe importante a ter em conta relativamente à inicialização do repositório:   
PNG

Nome do repositório (argolas-aquaticas): Correto e bem formatado.   
PNG

Descrição: Muito clara e informativa.   
PNG

Visibilidade (Público): Perfeito para ficar visível no portfólio.   
PNG

Licença (Licença MIT): Escolha adequada.   
PNG

Ponto de Atenção: Conflito de Ficheiros
Como selecionou Adicionar licença (Licença MIT), o GitHub irá criar o repositório já com um commit inicial contendo o ficheiro LICENSE.   
PNG

Para enviar o seu ficheiro argolas_aquaticas.py a partir do computador sem erros de conflito, tem duas alternativas:   
PY

Opção A (Recomendada via Terminal/Git)
Se pretende subir os ficheiros através da linha de comandos, desative a opção da licença (mantenha em Nenhum) e clique em Criar repositório. Dessa forma, o repositório nascerá vazio e os comandos convencionais de git push funcionarão diretamente. Depois, basta criar os ficheiros LICENSE e README.md localmente e enviá-los em conjunto.   
PNG
+ 1

Opção B (Se mantiver a Licença MIT ativada)
Se clicar agora em Criar repositório com a licença marcada:   
PNG

Ao inicializar o Git na sua pasta local, execute:

Bash
git init
git remote add origin https://github.com/Edinaldo-long/argolas-aquaticas.git
git pull origin main
Após puxar o ficheiro de licença criado pelo GitHub, adicione os seus ficheiros:

Bash
git add .
git commit -m "feat: adicionar jogo argolas aquáticas e documentação"
git branch -M main
git push -u origin main
(Em alternativa, na página do repositório após a criação, pode clicar em Add file > Upload files e arrastar o ficheiro diretamente pelo navegador).

Pode avançar e clicar no botão verde Criar repositório.   
PNG

PS C:\Users\esata\argolas_aquaticas> python argolas_aquaticas.py

pygame 2.6.1 (SDL 2.28.4, Python 3.11.1)

Hello from the pygame community. https://www.pygame.org/contribute.html

PS C:\Users\esata\argolas_aquaticas> 

 *  History restored 



PS C:\Users\esata\argolas_aquaticas> git init

>> git remote add origin https://github.com/Edinaldo-long/argolas-aquaticas.git

>> git pull origin main

Initialized empty Git repository in C:/Users/esata/argolas_aquaticas/.git/

remote: Enumerating objects: 3, done.

remote: Counting objects: 100% (3/3), done.

remote: Compressing objects: 100% (2/2), done.

remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)

Unpacking objects: 100% (3/3), 1.45 KiB | 1024 bytes/s, done.

From https://github.com/Edinaldo-long/argolas-aquaticas

 * [new branch]      main       -> origin/main

PS C:\Users\esata\argolas_aquaticas> git add .

>> git commit -m "feat: adicionar jogo argolas aquáticas e documentação"

>> git branch -M main

>> git push -u origin main

[master 64fc0f0] feat: adicionar jogo argolas aquáticas e documentação

 2 files changed, 853 insertions(+)

 create mode 100644 argolas_aquaticas.py

 create mode 100644 argolas_recorde.txt

Enumerating objects: 5, done.

Counting objects: 100% (5/5), done.

Delta compression using up to 4 threads

Compressing objects: 100% (3/3), done.

Writing objects: 100% (4/4), 10.23 KiB | 1.71 MiB/s, done.

Total 4 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)

To https://github.com/Edinaldo-long/argolas-aquaticas.git

   066604b..64fc0f0  main -> main

branch 'main' set up to track 'origin/main'.

PS C:\Users\esata\argolas_aquaticas> 

O envio para o GitHub foi concluído com sucesso! O código do jogo já se encontra no repositório remoto na ramificação main.   
PY
+ 1

Para deixar o repositório pronto e com apresentação profissional para o seu portfólio, restam apenas dois ajustes: adicionar os ficheiros de documentação (README.md e requirements.txt) e remover do controlo de versões o ficheiro de recorde local (argolas_recorde.txt), que foi enviado no primeiro envio.   
PY

Passo 1: Remover o ficheiro de recorde do rastreio do Git
Para retirar o argolas_recorde.txt do repositório remoto sem o apagar do seu computador:

PowerShell
git rm --cached argolas_recorde.txt
Passo 2: Criar os ficheiros auxiliares
Na mesma pasta C:\Users\esata\argolas_aquaticas, crie os seguintes três ficheiros:

.gitignore

Plaintext
__pycache__/
*.py[cod]
.venv/
venv/
argolas_recorde.txt
.vscode/
requirements.txt

Plaintext
pygame>=2.5.0
README.md

(Copie e cole o modelo estruturado de apresentação e documentação sugerido anteriormente).

Passo 3: Enviar as alterações para o GitHub
No terminal do PowerShell, execute:

PowerShell
git add .
git commit -m "docs: adicionar README, requirements e ignorar recorde local"
git push
Como verificar: Aceda à página do seu repositório no navegador ([https://github.com/Edinaldo-long/argolas-aquaticas](https://github.com/Edinaldo-long/argolas-aquaticas)) e atualize a página (F5). O README.md deverá aparecer imediatamente formatado na página inicial e o ficheiro argolas_recorde.txt não constará mais da lista de ficheiros.   
PNG

preciso de um read me bem legal

Vou gerar agora um arquivo README.md completo, atraente e formatado com badges, seções técnicas detalhadas e estrutura de portfólio para destacar o seu projeto no GitHub.

README.md
18 de out., 14:20
Criei um README.md completo, com badges, tabela de regras e controles, além da explicação técnica da física e do gerador procedural de som.

Para adicioná-lo ao seu projeto:

Salve o arquivo acima com o nome README.md dentro da pasta C:\Users\esata\argolas_aquaticas.

Crie uma pasta chamada screenshots, tire uma foto da janela do jogo rodando e salve como gameplay.png dentro dela.

No terminal, envie a atualização:

PowerShell
   git add .
   git commit -m "docs: adicionar documentacao completa no README"
   git push
   
quero em html por favor

Vou criar uma página HTML completa, interativa e estilizada para o seu portfólio, contendo a apresentação do jogo, detalhes técnicos, controles, showcase visual e links para o repositório.

Portfolio - Argolas Aquáticas


    @keyframes rise {
      0% { transform: translateY(110vh) scale(0.8); opacity: 0; }
      50% { opacity: 0.6; }
      100% { transform: translateY(-10vh) scale(1.2); opacity: 0; }
    }
    .bubble {
      position: absolute;
      bottom: -40px;
      background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.7), rgba(120,210,255,0.15));
      border: 1px solid rgba(255, 255, 255, 0.35);

Gerei o arquivo index.html com:

Design Marinho & Retrô: Paleta de cores subaquáticas, efeitos de transparência (glassmorphism) e bolhas geradas via CSS.

Showcase Visual do Jogo: Uma representação ilustrada do aquário com pinos e argolas coloridas simulando a interface.

Documentação de Engenharia: Detalhamento da física de fluidos, geração procedural de áudio por buffers senoidais e tabelas completas de regras e controles.

Responsividade e Integração: Funciona em celulares e desktops, com links diretos para o seu perfil e repositório Edinaldo-long/argolas-aquaticas.

Você pode salvar esse arquivo no repositório e ativá-lo gratuitamente via GitHub Pages (em Settings > Pages) para ter um site online no seu portfólio!

me de o codigo por favor em html

O seu arquivo HTML está pronto para download e visualização:

Ícone do app HTML
index
 HTML 
Aqui está o código-fonte completo em HTML + CSS inline para copiar diretamente para o seu projeto:

HTML
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Argolas Aquáticas - Pygame Arcade</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #070e1b;
      --card-bg: rgba(15, 27, 49, 0.75);
      --card-border: rgba(56, 189, 248, 0.2);
      --primary: #38bdf8;
      --primary-hover: #0ea5e9;
      --accent: #fbbf24;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --code-bg: #020617;
      --border-radius: 16px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.6;
      background-image: 
        radial-gradient(circle at 15% 20%, rgba(56, 189, 248, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 85% 75%, rgba(251, 191, 36, 0.08) 0%, transparent 40%);
      background-attachment: fixed;
      padding: 2.5rem 1rem;
    }

    .container {
      max-width: 900px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 2rem;
    }

    header {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--border-radius);
      padding: 2.5rem;
      backdrop-filter: blur(12px);
      text-align: center;
      position: relative;
      overflow: hidden;
    }

    .badge-wrapper {
      display: flex;
      justify-content: center;
      gap: 0.6rem;
      flex-wrap: wrap;
      margin-bottom: 1.25rem;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      padding: 0.35rem 0.85rem;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      border-radius: 9999px;
      background: rgba(56, 189, 248, 0.12);
      color: var(--primary);
      border: 1px solid rgba(56, 189, 248, 0.3);
    }

    .badge.gold {
      background: rgba(251, 191, 36, 0.12);
      color: var(--accent);
      border-color: rgba(251, 191, 36, 0.3);
    }

    h1 {
      font-size: clamp(2rem, 5vw, 2.75rem);
      font-weight: 800;
      color: #fff;
      margin-bottom: 0.8rem;
      letter-spacing: -0.02em;
    }

    .subtitle {
      font-size: 1.15rem;
      color: var(--text-muted);
      max-width: 680px;
      margin: 0 auto 1.75rem auto;
    }

    .header-links {
      display: flex;
      justify-content: center;
      gap: 1rem;
      flex-wrap: wrap;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.75rem 1.4rem;
      font-size: 0.95rem;
      font-weight: 600;
      border-radius: 10px;
      text-decoration: none;
      transition: all 0.2s ease;
      cursor: pointer;
    }

    .btn-primary {
      background: var(--primary);
      color: #031326;
    }

    .btn-primary:hover {
      background: var(--primary-hover);
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(56, 189, 248, 0.3);
    }

    .card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--border-radius);
      padding: 2rem;
      backdrop-filter: blur(12px);
    }

    h2 {
      font-size: 1.4rem;
      font-weight: 700;
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      color: #fff;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 0.6rem;
    }

    .grid-2 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1.25rem;
    }

    .feature-item {
      background: rgba(2, 6, 23, 0.4);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 12px;
      padding: 1.25rem;
    }

    .feature-item h3 {
      font-size: 1.05rem;
      color: var(--primary);
      margin-bottom: 0.4rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .feature-item p {
      font-size: 0.9rem;
      color: var(--text-muted);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 0.5rem;
      font-size: 0.95rem;
    }

    th, td {
      padding: 0.85rem 1rem;
      text-align: left;
      border-bottom: 1px solid rgba(255, 255, 255, 0.07);
    }

    th {
      background: rgba(2, 6, 23, 0.6);
      color: var(--primary);
      font-weight: 700;
      text-transform: uppercase;
      font-size: 0.8rem;
      letter-spacing: 0.05em;
    }

    td kbd {
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 5px;
      padding: 0.2rem 0.5rem;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      color: #fff;
    }

    .code-block {
      background: var(--code-bg);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px;
      padding: 1rem 1.25rem;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.88rem;
      color: #e2e8f0;
      overflow-x: auto;
      margin: 0.75rem 0 1.25rem 0;
    }

    .code-block code {
      display: block;
      line-height: 1.6;
    }

    .comment {
      color: #64748b;
    }

    footer {
      text-align: center;
      color: var(--text-muted);
      font-size: 0.85rem;
      margin-top: 1rem;
      padding-bottom: 2rem;
    }
  </style>
</head>
<body>

  <div class="container">
    <header>
      <div class="badge-wrapper">
        <span class="badge">Python 3.10+</span>
        <span class="badge">Pygame 2.5+</span>
        <span class="badge gold">Sem Assets Externos</span>
        <span class="badge">Áudio Procedural</span>
      </div>
      <h1>Argolas Aquáticas</h1>
      <p class="subtitle">
        Uma recriação nostálgica do brinquedo aquático dos anos 90 desenvolvida com física de fluidos e síntese matemática de áudio em tempo real.
      </p>
      <div class="header-links">
        <a href="https://github.com/Edinaldo-long/argolas-aquaticas" target="_blank" class="btn btn-primary">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6




O Gemini é uma IA e pode cometer erros.

Processado e analisado em código
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Argolas Aquáticas - Pygame Arcade</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #070e1b;
      --card-bg: rgba(15, 27, 49, 0.75);
      --card-border: rgba(56, 189, 248, 0.2);
      --primary: #38bdf8;
      --primary-hover: #0ea5e9;
      --accent: #fbbf24;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --code-bg: #020617;
      --border-radius: 16px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.6;
      background-image: 
        radial-gradient(circle at 15% 20%, rgba(56, 189, 248, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 85% 75%, rgba(251, 191, 36, 0.08) 0%, transparent 40%);
      background-attachment: fixed;
      padding: 2.5rem 1rem;
    }

    .container {
      max-width: 900px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 2rem;
    }

    header {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--border-radius);
      padding: 2.5rem;
      backdrop-filter: blur(12px);
      text-align: center;
      position: relative;
      overflow: hidden;
    }

    .badge-wrapper {
      display: flex;
      justify-content: center;
      gap: 0.6rem;
      flex-wrap: wrap;
      margin-bottom: 1.25rem;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      padding: 0.35rem 0.85rem;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      border-radius: 9999px;
      background: rgba(56, 189, 248, 0.12);
      color: var(--primary);
      border: 1px solid rgba(56, 189, 248, 0.3);
    }

    .badge.gold {
      background: rgba(251, 191, 36, 0.12);
      color: var(--accent);
      border-color: rgba(251, 191, 36, 0.3);
    }

    h1 {
      font-size: clamp(2rem, 5vw, 2.75rem);
      font-weight: 800;
      color: #fff;
      margin-bottom: 0.8rem;
      letter-spacing: -0.02em;
    }

    .subtitle {
      font-size: 1.15rem;
      color: var(--text-muted);
      max-width: 680px;
      margin: 0 auto 1.75rem auto;
    }

    .header-links {
      display: flex;
      justify-content: center;
      gap: 1rem;
      flex-wrap: wrap;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.75rem 1.4rem;
      font-size: 0.95rem;
      font-weight: 600;
      border-radius: 10px;
      text-decoration: none;
      transition: all 0.2s ease;
      cursor: pointer;
    }

    .btn-primary {
      background: var(--primary);
      color: #031326;
    }

    .btn-primary:hover {
      background: var(--primary-hover);
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(56, 189, 248, 0.3);
    }

    .btn-secondary {
      background: rgba(255, 255, 255, 0.06);
      color: var(--text-main);
      border: 1px solid rgba(255, 255, 255, 0.15);
    }

    .btn-secondary:hover {
      background: rgba(255, 255, 255, 0.12);
      transform: translateY(-2px);
    }

    .card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--border-radius);
      padding: 2rem;
      backdrop-filter: blur(12px);
    }

    h2 {
      font-size: 1.4rem;
      font-weight: 700;
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      color: #fff;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 0.6rem;
    }

    .grid-2 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1.25rem;
    }

    .feature-item {
      background: rgba(2, 6, 23, 0.4);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 12px;
      padding: 1.25rem;
    }

    .feature-item h3 {
      font-size: 1.05rem;
      color: var(--primary);
      margin-bottom: 0.4rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .feature-item p {
      font-size: 0.9rem;
      color: var(--text-muted);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 0.5rem;
      font-size: 0.95rem;
    }

    th, td {
      padding: 0.85rem 1rem;
      text-align: left;
      border-bottom: 1px solid rgba(255, 255, 255, 0.07);
    }

    th {
      background: rgba(2, 6, 23, 0.6);
      color: var(--primary);
      font-weight: 700;
      text-transform: uppercase;
      font-size: 0.8rem;
      letter-spacing: 0.05em;
    }

    td kbd {
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 5px;
      padding: 0.2rem 0.5rem;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      color: #fff;
    }

    .code-block {
      background: var(--code-bg);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px;
      padding: 1rem 1.25rem;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.88rem;
      color: #e2e8f0;
      overflow-x: auto;
      margin: 0.75rem 0 1.25rem 0;
    }

    .code-block code {
      display: block;
      line-height: 1.6;
    }

    .comment {
      color: #64748b;
    }

    footer {
      text-align: center;
      color: var(--text-muted);
      font-size: 0.85rem;
      margin-top: 1rem;
      padding-bottom: 2rem;
    }

    footer a {
      color: var(--primary);
      text-decoration: none;
    }
  </style>
</head>
<body>

  <div class="container">
    <!-- Header -->
    <header>
      <div class="badge-wrapper">
        <span class="badge">Python 3.10+</span>
        <span class="badge">Pygame 2.5+</span>
        <span class="badge gold">Sem Assets Externos</span>
        <span class="badge">Áudio Procedural</span>
      </div>
      <h1>Argolas Aquáticas</h1>
      <p class="subtitle">
        Uma recriação nostálgica do brinquedo aquático dos anos 90 desenvolvida com física de fluidos e síntese matemática de áudio em tempo real.
      </p>
      <div class="header-links">
        <a href="https://github.com/Edinaldo-long/argolas-aquaticas" target="_blank" class="btn btn-primary">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
          Ver Código no GitHub
        </a>
      </div>
    </header>

    <!-- Destaques de Engenharia -->
    <section class="card">
      <h2>⚙️ Destaques Técnicos</h2>
      <div class="grid-2">
        <div class="feature-item">
          <h3>🌊 Física Hidrodinâmica</h3>
          <p>Cálculo em tempo real de arrasto vetorial, flutuabilidade, amortecimento em colisões e efeito venturi centralizado nos jatos de bolhas.</p>
        </div>
        <div class="feature-item">
          <h3>🔊 Síntese Procedural de Áudio</h3>
          <p>Efeitos sonoros (bloops, jatos d'água, cliques e fanfarras) gerados diretamente via ondas senoidais e arrays de memória sem nenhum arquivo WAV/MP3.</p>
        </div>
        <div class="feature-item">
          <h3>🎨 Renderização Primitiva Pura</h3>
          <p>Toda a arte, reflexos no vidro, deformação elíptica das argolas 3D e peixes em movimento são desenhados por matrizes matemáticas.</p>
        </div>
        <div class="feature-item">
          <h3>🏆 Mecânicas de Arcade</h3>
          <p>Sistema dinâmico de combos x5 com contador regressivo, argola dourada de tripla pontuação e salvamento automático de recorde local.</p>
        </div>
      </div>
    </section>

    <!-- Controles -->
    <section class="card">
      <h2>🎮 Controles</h2>
      <table>
        <thead>
          <tr>
            <th>Ação</th>
            <th>Teclado</th>
            <th>Mouse</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Jato Esquerdo</strong></td>
            <td><kbd>Seta Esquerda</kbd> ou <kbd>Z</kbd></td>
            <td>Botão azul na tela</td>
          </tr>
          <tr>
            <td><strong>Jato Direito</strong></td>
            <td><kbd>Seta Direita</kbd> ou <kbd>M</kbd></td>
            <td>Botão vermelho na tela</td>
          </tr>
          <tr>
            <td><strong>Jato Duplo</strong></td>
            <td><kbd>Barra de Espaço</kbd></td>
            <td>Ambos os botões</td>
          </tr>
          <tr>
            <td><strong>Pausar</strong></td>
            <td><kbd>P</kbd></td>
            <td>—</td>
          </tr>
          <tr>
            <td><strong>Reiniciar / Novo Jogo</strong></td>
            <td><kbd>R</kbd></td>
            <td>Clique na tela</td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- Como Executar -->
    <section class="card">
      <h2>🚀 Como Executar Localmente</h2>
      <p style="color: var(--text-muted); margin-bottom: 0.5rem; font-size: 0.95rem;">
        Clone o repositório e execute com Python instalado:
      </p>
      <div class="code-block">
        <code><span class="comment"># 1. Clonar o repositório</span><br>git clone https://github.com/Edinaldo-long/argolas-aquaticas.git<br>cd argolas-aquaticas<br><br><span class="comment"># 2. Instalar dependências</span><br>pip install pygame<br><br><span class="comment"># 3. Iniciar o jogo</span><br>python argolas_aquaticas.py</code>
      </div>
    </section>

    <!-- Rodapé -->
    <footer>
      Desenvolvido por <strong>Edinaldo Santos de Almeida</strong> • Projeto para Portfólio de Desenvolvimento
    </footer>
  </div>

</body>
</html>
index.html
