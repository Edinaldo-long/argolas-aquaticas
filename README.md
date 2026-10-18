<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Argolas Aquáticas — Jogo Retrô & Portfólio</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
    }
    code, pre {
      font-family: 'JetBrains Mono', monospace;
    }
    .water-gradient {
      background: linear-gradient(180deg, #091326 0%, #0d2b45 50%, #031221 100%);
    }
    .glass-card {
      background: rgba(15, 30, 58, 0.7);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(80, 150, 240, 0.2);
    }
    .accent-glow {
      box-shadow: 0 0 35px rgba(45, 170, 255, 0.25);
    }
    /* Efeito de bolhas subindo suavemente no fundo */
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
      border-radius: 50%;
      pointer-events: none;
      animation: rise linear infinite;
    }
  </style>
</head>
<body class="water-gradient text-slate-100 min-h-screen relative overflow-x-hidden">

  <!-- Bolhas de fundo em tempo de execução -->
  <div class="fixed inset-0 overflow-hidden pointer-events-none z-0">
    <div class="bubble w-8 h-8 left-[10%]" style="animation-duration: 9s; animation-delay: 0s;"></div>
    <div class="bubble w-4 h-4 left-[25%]" style="animation-duration: 12s; animation-delay: 2s;"></div>
    <div class="bubble w-12 h-12 left-[45%]" style="animation-duration: 15s; animation-delay: 1s;"></div>
    <div class="bubble w-6 h-6 left-[70%]" style="animation-duration: 11s; animation-delay: 4s;"></div>
    <div class="bubble w-9 h-9 left-[85%]" style="animation-duration: 14s; animation-delay: 3s;"></div>
  </div>

  <!-- Navbar -->
  <header class="sticky top-0 z-50 glass-card border-b border-sky-500/20 px-6 py-4">
    <div class="max-w-6xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-3">
        <span class="text-2xl">🌊</span>
        <span class="text-xl font-bold tracking-tight bg-gradient-to-r from-sky-300 via-amber-200 to-amber-400 bg-clip-text text-transparent">
          Argolas Aquáticas
        </span>
      </div>
      <nav class="flex items-center gap-4 text-sm font-semibold">
        <a href="#destaques" class="hover:text-sky-300 transition-colors">Engenharia</a>
        <a href="#controles" class="hover:text-sky-300 transition-colors">Controles</a>
        <a href="#regras" class="hover:text-sky-300 transition-colors">Regras</a>
        <a href="https://github.com/Edinaldo-long/argolas-aquaticas" target="_blank" rel="noopener noreferrer" 
           class="px-4 py-2 rounded-xl bg-sky-500 hover:bg-sky-400 text-slate-950 font-bold flex items-center gap-2 shadow-lg shadow-sky-500/30 transition-all hover:scale-105">
          <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
          Ver no GitHub
        </a>
      </nav>
    </div>
  </header>

  <!-- Hero Section -->
  <main class="max-w-6xl mx-auto px-6 pt-16 pb-20 relative z-10">
    <div class="text-center max-w-3xl mx-auto">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-sky-500/10 border border-sky-400/30 text-sky-300 text-xs font-semibold mb-6">
        <span>🎮</span> Retro Game Dev • Python & Pygame
      </div>
      <h1 class="text-4xl sm:text-6xl font-extrabold tracking-tight text-white mb-6 leading-tight">
        O clássico dos anos 90, <br>
        <span class="bg-gradient-to-r from-sky-400 via-teal-300 to-amber-300 bg-clip-text text-transparent">
          totalmente procedural.
        </span>
      </h1>
      <p class="text-lg text-slate-300 leading-relaxed mb-8">
        Uma recriação fiel e dinâmica com simulação física de arrasto hidrodinâmico, jatos de água vetoriais e sintetizador sonoro matemático em tempo real — construído sem qualquer imagem ou áudio externo gravado.
      </p>

      <div class="flex flex-wrap items-center justify-center gap-4">
        <a href="#como-jogar" class="px-6 py-3.5 rounded-xl bg-gradient-to-r from-amber-400 to-amber-500 hover:from-amber-300 hover:to-amber-400 text-slate-950 font-bold transition-all shadow-lg shadow-amber-500/25 hover:scale-105">
          Como Rodar & Jogar
        </a>
        <a href="https://github.com/Edinaldo-long/argolas-aquaticas" target="_blank" rel="noopener noreferrer" 
           class="px-6 py-3.5 rounded-xl glass-card border border-sky-400/30 hover:border-sky-300 text-white font-semibold transition-all hover:scale-105 flex items-center gap-2">
          Código-Fonte Completo
        </a>
      </div>
    </div>

    <!-- Simulação Visual do Jogo (Canvas Animado) -->
    <div class="mt-14 glass-card p-4 sm:p-6 rounded-3xl accent-glow border border-sky-400/30">
      <div class="relative w-full aspect-[4/3] max-w-2xl mx-auto rounded-2xl overflow-hidden border-4 border-amber-400/70 shadow-2xl bg-slate-950 flex flex-col items-center justify-center p-6 text-center">
        <!-- Água / Fundo do Tanque -->
        <div class="absolute inset-0 bg-gradient-to-b from-[#147a96] via-[#094d69] to-[#042838]"></div>
        
        <!-- Pinos Centrais Ilustrados -->
        <div class="absolute bottom-16 left-1/4 w-3 h-32 bg-rose-500 rounded-t-full shadow-lg flex flex-col items-center justify-start pt-1">
          <span class="text-[10px] font-bold text-white">100</span>
        </div>
        <div class="absolute bottom-16 left-1/2 -translate-x-1/2 w-3.5 h-44 bg-amber-400 rounded-t-full shadow-lg flex flex-col items-center justify-start pt-1">
          <span class="text-[10px] font-bold text-slate-950">300</span>
        </div>
        <div class="absolute bottom-16 right-1/4 w-3 h-32 bg-sky-400 rounded-t-full shadow-lg flex flex-col items-center justify-start pt-1">
          <span class="text-[10px] font-bold text-white">100</span>
        </div>

        <!-- Argolas Estilizadas em Posições Dinâmicas -->
        <div class="absolute bottom-20 left-1/4 -translate-x-1/2 w-12 h-6 border-4 border-pink-500 rounded-full rotate-6 shadow-md"></div>
        <div class="absolute bottom-24 left-1/2 -translate-x-1/2 w-12 h-6 border-4 border-amber-300 rounded-full -rotate-3 shadow-md animate-pulse"></div>
        <div class="absolute bottom-40 right-1/4 translate-x-4 w-12 h-6 border-4 border-emerald-400 rounded-full rotate-12 shadow-md"></div>

        <!-- Chão de Areia -->
        <div class="absolute bottom-0 inset-x-0 h-16 bg-[#caa66a] border-t-2 border-amber-200/40"></div>

        <!-- Textos Overlay -->
        <div class="relative z-10 bg-slate-950/80 p-5 rounded-2xl border border-sky-400/40 max-w-md">
          <span class="text-amber-400 text-xs font-bold uppercase tracking-wider">Gameplay Interativa</span>
          <h3 class="text-xl font-bold mt-1 mb-2 text-white">800 × 700 @ 60 FPS</h3>
          <p class="text-xs text-slate-300 mb-4">
            Execute localmente para interagir com a física em tempo real ou explore a arquitetura do motor abaixo.
          </p>
          <div class="flex justify-center gap-2 text-xs font-mono">
            <span class="px-2.5 py-1 rounded bg-sky-500/20 text-sky-300 border border-sky-400/30">Z / ← Jato Azul</span>
            <span class="px-2.5 py-1 rounded bg-rose-500/20 text-rose-300 border border-rose-400/30">M / → Jato Vermelho</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Destaques Técnicos -->
    <section id="destaques" class="mt-24">
      <div class="text-center mb-12">
        <h2 class="text-3xl font-bold tracking-tight text-white">Engenharia do Projeto</h2>
        <p class="text-slate-400 mt-2">Destaques da implementação matemática e arquitetural</p>
      </div>

      <div class="grid md:grid-cols-3 gap-6">
        <!-- Card 1: Física de Fluidos -->
        <div class="glass-card p-6 rounded-2xl hover:border-sky-400/50 transition-colors">
          <div class="w-12 h-12 rounded-xl bg-sky-500/20 border border-sky-400/30 flex items-center justify-center text-2xl mb-4">
            🌪️
          </div>
          <h3 class="text-lg font-bold text-white mb-2">Física Hidrodinâmica</h3>
          <p class="text-sm text-slate-300 leading-relaxed">
            Sub-stepping com 2 iterações por frame calculando forças de arrasto proporcional à velocidade (<code class="text-sky-300">$K \cdot (\vec{u} - \vec{v})$</code>), gravidade reduzida, flutuabilidade e forças cônicas centrípetas nos jatos.
          </p>
        </div>

        <!-- Card 2: Áudio Procedural -->
        <div class="glass-card p-6 rounded-2xl hover:border-amber-400/50 transition-colors">
          <div class="w-12 h-12 rounded-xl bg-amber-500/20 border border-amber-400/30 flex items-center justify-center text-2xl mb-4">
            🔊
          </div>
          <h3 class="text-lg font-bold text-white mb-2">Síntese de Som Matemática</h3>
          <p class="text-sm text-slate-300 leading-relaxed">
            Geração de som em tempo de execução via <code class="text-amber-300">array('h')</code> a 44.1kHz. Ondas senoidais, ruído filtrado de baixa frequência para simular água e transições quadradas para pontuações retrô.
          </p>
        </div>

        <!-- Card 3: Gráficos Vetoriais -->
        <div class="glass-card p-6 rounded-2xl hover:border-teal-400/50 transition-colors">
          <div class="w-12 h-12 rounded-xl bg-teal-500/20 border border-teal-400/30 flex items-center justify-center text-2xl mb-4">
            🎨
          </div>
          <h3 class="text-lg font-bold text-white mb-2">Renderização Zero-Asset</h3>
          <p class="text-sm text-slate-300 leading-relaxed">
            Toda a cena é desenhada por primitivas geométricas e curvas trigonométricas: elipses oclusas para renderizar as argolas contornando as hastes, raios de luz alfa e cardumes animados.
          </p>
        </div>
      </div>
    </section>

    <!-- Controles & Regras em Grid -->
    <div class="grid md:grid-cols-2 gap-8 mt-16" id="controles">
      
      <!-- Controles -->
      <section class="glass-card p-6 rounded-2xl">
        <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
          <span>🕹️</span> Controles do Jogo
        </h3>
        <div class="space-y-3 text-sm">
          <div class="flex items-center justify-between p-3 rounded-xl bg-slate-900/50 border border-slate-700/50">
            <span class="text-slate-300">Jato da Esquerda</span>
            <span class="px-2 py-1 rounded bg-sky-500/20 text-sky-300 font-mono text-xs">Seta Esquerda / Z / Clique</span>
          </div>
          <div class="flex items-center justify-between p-3 rounded-xl bg-slate-900/50 border border-slate-700/50">
            <span class="text-slate-300">Jato da Direita</span>
            <span class="px-2 py-1 rounded bg-rose-500/20 text-rose-300 font-mono text-xs">Seta Direita / M / Clique</span>
          </div>
          <div class="flex items-center justify-between p-3 rounded-xl bg-slate-900/50 border border-slate-700/50">
            <span class="text-slate-300">Ambos os Jatos</span>
            <span class="px-2 py-1 rounded bg-amber-500/20 text-amber-300 font-mono text-xs">Barra de Espaço</span>
          </div>
          <div class="flex items-center justify-between p-3 rounded-xl bg-slate-900/50 border border-slate-700/50">
            <span class="text-slate-300">Pausar / Retomar</span>
            <span class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-mono text-xs">Tecla P</span>
          </div>
          <div class="flex items-center justify-between p-3 rounded-xl bg-slate-900/50 border border-slate-700/50">
            <span class="text-slate-300">Reiniciar / Novo Jogo</span>
            <span class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-mono text-xs">Tecla R</span>
          </div>
        </div>
      </section>

      <!-- Regras e Pontuação -->
      <section class="glass-card p-6 rounded-2xl" id="regras">
        <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
          <span>🎯</span> Sistema de Pontuação
        </h3>
        <ul class="space-y-3.5 text-sm text-slate-300">
          <li class="flex items-start gap-3">
            <span class="text-rose-400 text-base font-bold">100</span>
            <div><strong>Pinos Laterais:</strong> Encaixes padrão nas extremidades do aquário.</div>
          </li>
          <li class="flex items-start gap-3">
            <span class="text-amber-400 text-base font-bold">300</span>
            <div><strong>Pino Dourado Central:</strong> Maior elevação e desafio hidrodinâmico.</div>
          </li>
          <li class="flex items-start gap-3">
            <span class="text-yellow-300 text-base font-bold">×3</span>
            <div><strong>Argola de Ouro:</strong> Uma argola especial por rodada triplica a pontuação.</div>
          </li>
          <li class="flex items-start gap-3">
            <span class="text-emerald-400 text-base font-bold">×5</span>
            <div><strong>Multiplicador de Combo:</strong> Encaixes seguidos aumentam progressivamente os pontos.</div>
          </li>
          <li class="flex items-start gap-3">
            <span class="text-sky-300 text-base font-bold">+⏳</span>
            <div><strong>Bônus de Tempo:</strong> O tempo restante é convertido em pontuação ao zerar a rodada.</div>
          </li>
        </ul>
      </section>

    </div>

    <!-- Como Executar Localmente -->
    <section class="mt-16 glass-card p-8 rounded-3xl" id="como-jogar">
      <h3 class="text-2xl font-bold text-white mb-4">Como rodar na sua máquina</h3>
      <p class="text-slate-300 text-sm mb-6">
        O projeto requer apenas Python 3 instalado e o pacote Pygame.
      </p>

      <div class="bg-slate-950 p-5 rounded-2xl border border-slate-800 text-xs sm:text-sm text-slate-300 overflow-x-auto space-y-3">
        <div class="text-slate-500"># 1. Clone o repositório</div>
        <div class="text-sky-300">git clone https://github.com/Edinaldo-long/argolas-aquaticas.git</div>
        <div class="text-sky-300">cd argolas-aquaticas</div>
        <div class="text-slate-500 pt-2"># 2. Instale as dependências</div>
        <div class="text-sky-300">pip install pygame</div>
        <div class="text-slate-500 pt-2"># 3. Inicie o jogo</div>
        <div class="text-emerald-400 font-semibold">python argolas_aquaticas.py</div>
      </div>
    </section>

  </main>

  <!-- Rodapé -->
  <footer class="border-t border-sky-500/20 py-8 px-6 text-center text-xs text-slate-400 relative z-10 glass-card">
    <p>Projeto de código aberto desenvolvido com 💛 e Python por <strong>Edinaldo</strong>.</p>
    <p class="mt-2">
      Disponível no 
      <a href="https://github.com/Edinaldo-long/argolas-aquaticas" class="text-sky-400 hover:underline">GitHub</a> sob a licença MIT.
    </p>
  </footer>

</body>
</html>
