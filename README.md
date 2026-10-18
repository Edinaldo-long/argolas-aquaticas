
# 🌊 Argolas Aquáticas ("Waterful Ring Toss")

Uma recriação nostálgica em Python/Pygame do clássico brinquedo aquático dos anos 90, desenvolvida com física de fluidos simulada e síntese procedural de áudio em tempo real — sem necessidade de assets externos.



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
