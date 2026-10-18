<div align="center">

  <h1>🌊 Argolas Aquáticas (Waterful Ring Toss)</h1>
  <p><em>Uma recriação nostálgica em Python/Pygame do clássico brinquedo aquático dos anos 90, desenvolvida com física de fluidos simulada e síntese procedural de áudio em tempo real — sem necessidade de assets externos.</em></p>

  <p>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"></a>
    <a href="https://www.pygame.org/"><img src="https://img.shields.io/badge/Pygame-2.5+-FFE873?style=for-the-badge&logo=python&logoColor=3776AB" alt="Pygame 2.5+"></a>
    <a href="https://github.com/Edinaldo-long/argolas-aquaticas"><img src="https://img.shields.io/badge/Physics-Hydrodynamic_Drag-0284c7?style=for-the-badge&logo=target" alt="Hydrodynamic Drag Physics"></a>
    <a href="https://github.com/Edinaldo-long/argolas-aquaticas"><img src="https://img.shields.io/badge/Audio-Procedural_PCM-38bdf8?style=for-the-badge&logo=soundcloud" alt="Procedural PCM Audio"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-c084fc?style=for-the-badge" alt="MIT License"></a>
  </p>

  <br>

  <p align="center">
    <a href="argolas_aquaticas.png" target="_blank">
      <img src="argolas_aquaticas.png" alt="Demonstração do Jogo Argolas Aquáticas" width="520" style="border-radius: 14px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5); cursor: pointer; border: 1px solid rgba(56, 189, 248, 0.3);">
    </a>
    <br>
    <sub style="color: #94a3b8;">🔍 Clique na imagem para abrir em tamanho real</sub>
  </p>

  <hr>

</div>

<h2>🎯 Destaques Técnicos</h2>

<ul>
  <li><strong>Física e Dinâmica de Fluidos:</strong> Simulação de arrasto hidrodinâmico, empuxo, correntes de jato vetoriais e amortecimento de colisão para reproduzir o comportamento de objetos flutuando na água.</li>
  <li><strong>Síntese de Áudio Procedural:</strong> Sons sintetizados matematicamente via <code>array</code> de ondas (senoidais e quadradas com modulação de frequência e ruído branco) integrados diretamente ao <code>pygame.mixer</code>, dispensando arquivos <code>.wav</code> ou <code>.mp3</code>.</li>
  <li><strong>Renderização Gráfica Vetorial:</strong> Toda a interface gráfica, tanque, peixes, bolhas e reflexos são gerados em tempo de execução via primitivas do Pygame e cálculos trigonométricos.</li>
  <li><strong>Mecânica de Jogo Completa:</strong> Sistema de pontuação balanceado com combos temporizados, argolas especiais (ouro x3), tempo regressivo, fases progressivas e persistência de recorde local (<code>highscore</code>).</li>
</ul>

<hr>

<h2>🎮 Controles</h2>

<table>
  <thead>
    <tr>
      <th align="left">Ação</th>
      <th align="left">Teclado</th>
      <th align="left">Mouse</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Jato Esquerdo</strong></td>
      <td><kbd>Seta Esquerda</kbd> ou <kbd>Z</kbd></td>
      <td>Clique no botão azul</td>
    </tr>
    <tr>
      <td><strong>Jato Direito</strong></td>
      <td><kbd>Seta Direita</kbd> ou <kbd>M</kbd></td>
      <td>Clique no botão vermelho</td>
    </tr>
    <tr>
      <td><strong>Ambos os Jatos</strong></td>
      <td><kbd>Barra de Espaço</kbd></td>
      <td>—</td>
    </tr>
    <tr>
      <td><strong>Pausar</strong></td>
      <td><kbd>P</kbd></td>
      <td>—</td>
    </tr>
    <tr>
      <td><strong>Reiniciar / Novo Jogo</strong></td>
      <td><kbd>R</kbd></td>
      <td>Clique na tela (telas de menu/fim)</td>
    </tr>
    <tr>
      <td><strong>Sair</strong></td>
      <td><kbd>ESC</kbd></td>
      <td>Fechar janela</td>
    </tr>
  </tbody>
</table>

<hr>

<h2>🕹️ Regras do Jogo</h2>

<ul>
  <li><strong>Objetivo:</strong> Acertar as argolas nos pinos antes do cronômetro zerar.</li>
  <li><strong>Pinos Laterais:</strong> 100 pontos.</li>
  <li><strong>Pino Central:</strong> 300 pontos.</li>
  <li><strong>Argola Dourada:</strong> Multiplica o valor do encaixe por 3.</li>
  <li><strong>Combos:</strong> Encaixes consecutivos dentro da janela de tempo concedem multiplicadores de até 5x.</li>
</ul>

<hr>

<h2>🚀 Como Executar</h2>

<h3>Pré-requisitos</h3>
<ul>
  <li>Python 3.10 ou superior instalado.</li>
</ul>

<h3>Passo a Passo</h3>
<pre><code># 1. Clone o repositório
git clone https://github.com/Edinaldo-long/argolas-aquaticas.git
cd argolas-aquaticas

# 2. Crie e ative um ambiente virtual (opcional)
python -m venv venv
# No Windows:
venv\Scripts\activate

# 3. Instale a dependência
pip install pygame

# 4. Inicie o jogo
python argolas_aquaticas.py</code></pre>

<hr>

<h2>🛠️ Tecnologias Utilizadas</h2>

<ul>
  <li><strong>Linguagem:</strong> Python</li>
  <li><strong>Biblioteca Multimídia:</strong> Pygame</li>
  <li><strong>Módulos Nativos:</strong> <code>math</code>, <code>random</code>, <code>array</code>, <code>sys</code>, <code>os</code></li>
</ul>

<hr>

<h2>👤 Autor</h2>

<p>
  Desenvolvido por <strong>Edinaldo Santos de Almeida</strong><br>
  <a href="https://github.com/Edinaldo-long"><img src="https://img.shields.io/badge/GitHub-Edinaldo--long-181717?style=flat-square&logo=github" alt="GitHub"></a>
</p>

<hr>

<div align="center">
  <sub>Licenciado sob a Licença MIT. Desenvolvido para fins de estudo de física hidrodinâmica 2D, síntese sonora e computação gráfica.</sub>
</div>
