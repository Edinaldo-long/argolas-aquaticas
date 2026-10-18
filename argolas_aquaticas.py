"""ARGOLAS AQUÁTICAS - o clássico brinquedo de água dos anos 90 (pip install pygame)

Controles
  Seta esquerda / Z   jato da ESQUERDA (botão azul)
  Seta direita / M    jato da DIREITA  (botão vermelho)
  ESPAÇO              os dois jatos ao mesmo tempo
  Mouse               clique e segure nos botões da tela
  P  pausa   |   R  recomeçar   |   ESC  sair

Como jogar
  Use os jatos para empurrar as argolas para cima e deixe elas caírem
  nos pinos. O pino do meio vale 300, os dos lados valem 100.
  Argolas seguidas rapidamente formam COMBO (até x5).
  A argola DOURADA vale o triplo! Encaixe todas antes do tempo acabar.
"""
import math
import os
import random
import sys
from array import array

import pygame

W, H = 800, 700
FPS = 60
SUB = 2

TX0, TX1 = 50, 750        # paredes do tanque
TY0 = 92                  # "teto" do tanque
FLOOR = 520               # topo da areia
TANK_BOTTOM = 566

R = 24                    # raio visual da argola
RC = 20                   # raio de colisão
THICK = 7
CAP = 5                   # argolas por pino
G = 0.08                  # gravidade na água
K = 0.06                  # arrasto: a argola acompanha a velocidade da água

SCORE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "argolas_recorde.txt")

RING_COLORS = [(235, 64, 52), (255, 140, 0), (250, 215, 40), (60, 190, 90),
               (40, 150, 240), (170, 90, 230), (255, 105, 180)]
GOLD = (255, 205, 40)


def shade(c, f):
    return tuple(max(0, min(255, int(v * f))) for v in c)


# ------------------------------------------------------------------ sons
def tone(f0, f1, ms, vol=0.3, noise=0.0, square=False):
    rate = 44100
    n = int(rate * ms / 1000)
    buf = array("h")
    ph = 0.0
    for i in range(n):
        t = i / n
        ph += 2 * math.pi * (f0 + (f1 - f0) * t) / rate
        s = math.sin(ph)
        if square:
            s = 1.0 if s > 0 else -1.0
        s = s * (1 - noise) + random.uniform(-1, 1) * noise
        buf.append(int(s * (1 - t) ** 1.3 * vol * 32767))
    return buf


def make(*parts):
    out = array("h")
    for p in parts:
        out.extend(p)
    return pygame.mixer.Sound(buffer=out.tobytes())


def load_sounds():
    try:
        if not pygame.mixer.get_init():
            pygame.mixer.init(44100, -16, 1, 512)
        # ruído de água para o jato (ruído filtrado, toca em loop)
        buf = array("h")
        prev = 0.0
        for _ in range(22050):
            prev = prev * 0.93 + random.uniform(-1, 1) * 0.07
            buf.append(int(prev * 3.2 * 0.20 * 32767))
        return {
            "jet": pygame.mixer.Sound(buffer=buf.tobytes()),
            "bloop": make(tone(380, 900, 90, 0.25)),
            "catch": make(tone(700, 700, 70, 0.22), tone(1000, 1000, 70, 0.22), tone(1400, 1400, 140, 0.22)),
            "gold": make(tone(800, 800, 70, 0.22, square=True), tone(1100, 1100, 70, 0.22, square=True),
                         tone(1500, 1500, 70, 0.22, square=True), tone(2000, 2000, 180, 0.22, square=True)),
            "clear": make(tone(523, 523, 120, 0.25), tone(659, 659, 120, 0.25), tone(784, 784, 120, 0.25),
                          tone(1046, 1046, 360, 0.25)),
            "tick": make(tone(1200, 1200, 40, 0.2, square=True)),
            "over": make(tone(500, 400, 200, 0.3), tone(400, 300, 200, 0.3), tone(300, 150, 500, 0.3)),
            "clack": make(tone(220, 120, 50, 0.3, noise=0.5)),
        }
    except Exception:
        return {}


# ------------------------------------------------------------- geometria
def closest_point(p, a, b):
    abx, aby = b[0] - a[0], b[1] - a[1]
    t = ((p[0] - a[0]) * abx + (p[1] - a[1]) * aby) / (abx * abx + aby * aby)
    t = max(0.0, min(1.0, t))
    return a[0] + abx * t, a[1] + aby * t


def ellipse_pts(cx, cy, rx, ry, a0, a1, n):
    return [(cx + rx * math.cos(a0 + (a1 - a0) * i / n), cy + ry * math.sin(a0 + (a1 - a0) * i / n))
            for i in range(n + 1)]


def draw_ring(surf, cx, cy, rx, ry, thick, color, part="full", sparkle=0.0):
    """Desenha uma argola (elipse oca). part: full | back (metade de trás) | front (metade da frente)."""
    rx_i = max(2.0, rx - thick)
    ry_i = max(1.0, ry - thick * max(0.5, ry / rx))
    a0, a1 = {"full": (0, math.tau), "back": (math.pi, math.tau), "front": (0, math.pi)}[part]
    n = 28 if part == "full" else 16
    outer = ellipse_pts(cx, cy, rx, ry, a0, a1, n)
    inner = ellipse_pts(cx, cy, rx_i, ry_i, a1, a0, n)
    pts = outer + inner
    pygame.draw.polygon(surf, color, pts)
    pygame.draw.polygon(surf, shade(color, 0.55), pts, 2)
    # brilho
    if part in ("full", "back"):
        hi = ellipse_pts(cx, cy, rx - thick * 0.45, ry - thick * 0.35 * max(0.5, ry / rx),
                         math.pi * 1.08, math.pi * 1.55, 8)
        if len(hi) > 1:
            pygame.draw.lines(surf, shade(color, 1.45), False, hi, 2)
    if sparkle > 0:
        sx = cx + rx * math.cos(sparkle)
        sy = cy + ry * math.sin(sparkle) * 0.6
        pygame.draw.circle(surf, (255, 255, 255), (int(sx), int(sy)), 3)


# ------------------------------------------------------------------ jato
class Jet:
    L = 640
    U0 = 14.0

    def __init__(self, x, y, angle_deg, key_name):
        self.x, self.y = x, y
        a = math.radians(angle_deg)
        self.dx, self.dy = math.cos(a), math.sin(a)
        self.p = 0.0
        self.on = False
        self.name = key_name

    def set(self, pressed):
        self.on = pressed
        self.p = min(1.0, self.p + 0.10) if pressed else max(0.0, self.p - 0.14)

    def flow(self, x, y):
        if self.p < 0.02:
            return 0.0, 0.0
        rx, ry = x - self.x, y - self.y
        along = rx * self.dx + ry * self.dy
        if along < 0 or along > self.L:
            return 0.0, 0.0
        perp = -rx * self.dy + ry * self.dx
        w = 38 + 0.20 * along
        if abs(perp) >= w:
            return 0.0, 0.0
        f = (1 - along / self.L) ** 0.7 * (1 - (perp / w) ** 2) * self.p * self.U0
        s = -perp / w * 0.45   # o jato "puxa" a argola para o centro do fluxo
        return (self.dx - self.dy * s) * f, (self.dy + self.dx * s) * f


# ----------------------------------------------------------------- pino
class Peg:
    def __init__(self, x, top, value, color):
        self.x, self.top, self.value, self.color = x, top, value, color
        self.base = top + 100
        self.stack = []
        self.tol = 12

    def slot_y(self, idx):
        return self.base - 10 - idx * 13


class Ring:
    def __init__(self, x, y, color, gold=False):
        self.x, self.y = float(x), float(y)
        self.vx = self.vy = 0.0
        self.color = color
        self.gold = gold
        self.phase = random.uniform(0, math.tau)
        self.spin = random.uniform(0.025, 0.05) * random.choice([-1, 1])
        self.peg = None
        self.slot = 0
        self.seed = random.uniform(0, 100)


# ------------------------------------------------------------------ jogo
class Game:
    def __init__(self, sounds=True):
        self.sfx = load_sounds() if sounds else {}
        self.jet_chan = [None, None]
        self.high = self.load_high()
        self.jets = [Jet(90, FLOOR - 4, -56, "left"), Jet(710, FLOOR - 4, -124, "right")]
        self.pegs = [Peg(300, 300, 100, (255, 90, 90)), Peg(400, 215, 300, (255, 215, 70)),
                     Peg(500, 300, 100, (90, 200, 255))]
        self.t = 0
        self.fx = []        # partículas
        self.texts = []
        self.bubbles = [{"x": random.uniform(TX0, TX1), "y": random.uniform(TY0, FLOOR),
                         "r": random.uniform(2, 6), "s": random.uniform(0.2, 0.7),
                         "ph": random.uniform(0, 6.28)} for _ in range(35)]
        self.fish = [self.new_fish(True) for _ in range(6)]
        self.state = "menu"
        self.paused = False
        self.reset()

    # ---- estado
    def reset(self):
        self.score = 0
        self.round = 0
        self.combo = 0
        self.combo_timer = 0
        self.caught_total = 0
        self.time_left = 0.0
        self.clear_timer = 0
        self.new_record = False
        self.rings = []
        self.start_round(1, idle=True)

    def start_round(self, n, idle=False):
        self.round = n
        count = min(12, 5 + n)
        self.time_left = 45.0 + 5 * n
        for p in self.pegs:
            p.stack = []
            p.tol = max(8, 13 - n)
        self.assist = max(0.004, 0.013 - 0.002 * n)
        self.rings = []
        gold_i = random.randrange(count)
        cols = RING_COLORS[:]
        random.shuffle(cols)
        for i in range(count):
            left = i % 2 == 0
            x = random.uniform(80, 235) if left else random.uniform(565, 720)
            y = FLOOR - RC - random.uniform(0, 110)
            self.rings.append(Ring(x, y, GOLD if i == gold_i else cols[i % len(cols)], i == gold_i))
        self.combo = 0
        self.combo_timer = 0
        if not idle:
            self.state = "play"
            self.texts.append({"t": f"RODADA {n}", "x": 400, "y": 300, "life": 100, "c": (255, 255, 255), "big": True})

    def start(self):
        self.reset()
        self.state = "play"
        self.texts.append({"t": "RODADA 1", "x": 400, "y": 300, "life": 100, "c": (255, 255, 255), "big": True})

    @staticmethod
    def load_high():
        try:
            with open(SCORE_FILE) as f:
                return int(f.read().strip())
        except Exception:
            return 0

    def save_high(self):
        try:
            with open(SCORE_FILE, "w") as f:
                f.write(str(self.high))
        except Exception:
            pass

    def play(self, name):
        s = self.sfx.get(name)
        if s:
            s.play()

    @staticmethod
    def new_fish(anywhere=False):
        d = random.choice([-1, 1])
        return {"x": random.uniform(TX0, TX1) if anywhere else (TX0 - 40 if d > 0 else TX1 + 40),
                "y": random.uniform(TY0 + 30, FLOOR - 60), "d": d, "s": random.uniform(0.3, 0.9),
                "size": random.uniform(10, 17), "c": random.choice([(255, 150, 60), (255, 220, 90),
                                                                    (120, 230, 190), (255, 120, 150)]),
                "ph": random.uniform(0, 6.28)}

    # ---- efeitos
    def burst(self, x, y, color, n=14):
        for _ in range(n):
            a = random.uniform(0, math.tau)
            s = random.uniform(1, 4)
            self.fx.append({"x": x, "y": y, "vx": math.cos(a) * s, "vy": math.sin(a) * s - 1,
                            "life": random.randint(20, 40), "c": color, "r": random.uniform(2, 4), "g": -0.03})

    def popup(self, text, x, y, color=(255, 255, 255), big=False, life=60):
        self.texts.append({"t": text, "x": x, "y": y, "life": life, "c": color, "big": big})

    # ---- atualização
    def update(self, left, right):
        self.t += 1
        self.update_ambient()
        if self.paused:
            return
        self.jets[0].set(left)
        self.jets[1].set(right)
        self.jet_sound()
        self.jet_particles()

        for _ in range(SUB):
            self.physics(1.0 / SUB)

        if self.state == "play":
            if self.combo_timer > 0:
                self.combo_timer -= 1
                if self.combo_timer == 0:
                    self.combo = 0
            prev = int(self.time_left)
            self.time_left -= 1 / FPS
            if int(self.time_left) < prev and self.time_left < 10:
                self.play("tick")
            if all(r.peg and abs(r.y - r.peg.slot_y(r.slot)) < 2 for r in self.rings):
                self.round_clear()
            elif self.time_left <= 0:
                self.game_over()
        elif self.state == "clear":
            self.clear_timer -= 1
            if self.clear_timer <= 0:
                self.start_round(self.round + 1)

    def round_clear(self):
        bonus = int(self.time_left) * 10
        self.score += bonus
        self.state = "clear"
        self.clear_timer = 170
        self.play("clear")
        self.popup("RODADA COMPLETA!", 400, 250, (120, 255, 200), True, 150)
        self.popup(f"Bônus de tempo: +{bonus}", 400, 300, (255, 240, 140), False, 150)
        for _ in range(5):
            self.burst(random.uniform(200, 600), random.uniform(150, 350),
                       random.choice(RING_COLORS), 14)
        self.check_high()

    def game_over(self):
        self.state = "over"
        self.play("over")
        self.check_high()
        for ch in self.jet_chan:
            if ch:
                ch.stop()

    def check_high(self):
        if self.score > self.high:
            self.high = self.score
            self.new_record = True
            self.save_high()

    def jet_sound(self):
        snd = self.sfx.get("jet")
        if not snd:
            return
        for i, j in enumerate(self.jets):
            ch = self.jet_chan[i]
            if j.on and self.state in ("play", "menu", "clear"):
                if ch is None or not ch.get_busy():
                    ch = snd.play(loops=-1, fade_ms=60)
                    self.jet_chan[i] = ch
                    if ch:
                        ch.set_volume(0.55)
            elif ch is not None:
                ch.fadeout(120)
                self.jet_chan[i] = None

    def jet_particles(self):
        for j in self.jets:
            if j.p > 0.1:
                for _ in range(int(2 + 4 * j.p)):
                    d = random.uniform(0, 70)
                    off = random.uniform(-10, 10)
                    sp = random.uniform(5, 11) * j.p
                    self.fx.append({"x": j.x + j.dx * d - j.dy * off, "y": j.y + j.dy * d + j.dx * off,
                                    "vx": j.dx * sp + random.uniform(-0.5, 0.5),
                                    "vy": j.dy * sp + random.uniform(-0.5, 0.5),
                                    "life": random.randint(18, 40), "c": (200, 235, 255),
                                    "r": random.uniform(1.5, 3.2), "g": -0.02, "bub": True})
                if random.random() < 0.15 * j.p:
                    self.play("bloop")

    def update_ambient(self):
        for b in self.bubbles:
            b["y"] -= b["s"]
            b["x"] += math.sin(self.t * 0.03 + b["ph"]) * 0.3
            if b["y"] < TY0:
                b["y"] = FLOOR + random.uniform(0, 20)
                b["x"] = random.uniform(TX0 + 10, TX1 - 10)
        for f in self.fish:
            f["x"] += f["d"] * f["s"]
            f["y"] += math.sin(self.t * 0.04 + f["ph"]) * 0.25
            if (f["d"] > 0 and f["x"] > TX1 + 50) or (f["d"] < 0 and f["x"] < TX0 - 50):
                f.update(self.new_fish())
        for p in self.fx[:]:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["vx"] *= 0.94
            p["vy"] = p["vy"] * 0.94 + p["g"]
            p["life"] -= 1
            if p["life"] <= 0 or p["y"] < TY0 - 5:
                self.fx.remove(p)
        for t in self.texts[:]:
            t["y"] -= 0.4
            t["life"] -= 1
            if t["life"] <= 0:
                self.texts.remove(t)

    # ---- física
    def physics(self, dt):
        free = [r for r in self.rings if r.peg is None]
        for r in free:
            ux = uy = 0.0
            for j in self.jets:
                fx, fy = j.flow(r.x, r.y)
                ux += fx
                uy += fy
            ax = K * (ux - r.vx) + 0.03 * math.sin(self.t * 0.021 + r.seed + r.y * 0.03)
            ay = G + K * (uy - r.vy) + 0.02 * math.cos(self.t * 0.017 + r.seed + r.x * 0.02)
            # chão inclinado: argolas no fundo deslizam para os lados
            if r.y > FLOOR - RC - 4:
                dxc = r.x - 400
                ax += 0.05 * max(-1, min(1, dxc / 120.0 if abs(dxc) > 4 else random.uniform(-1, 1)))
            # leve "ímã" para facilitar o encaixe nos pinos
            for p in self.pegs:
                dx = p.x - r.x
                if abs(dx) < 34 and p.top - 70 < r.y < p.top and r.vy > 0 and len(p.stack) < CAP:
                    ax += dx * self.assist
            r.vx += ax * dt
            r.vy += ay * dt
            r.x += r.vx * dt
            r.y += r.vy * dt
            r.phase += r.spin * dt

            # paredes do tanque
            if r.x < TX0 + RC:
                r.x = TX0 + RC
                r.vx = abs(r.vx) * 0.4
            if r.x > TX1 - RC:
                r.x = TX1 - RC
                r.vx = -abs(r.vx) * 0.4
            if r.y < TY0 + RC:
                r.y = TY0 + RC
                r.vy = abs(r.vy) * 0.3
            if r.y > FLOOR - RC:
                r.y = FLOOR - RC
                if r.vy > 1.5:
                    self.play("clack")
                r.vy = -r.vy * 0.2 if r.vy > 0 else r.vy
                r.vx *= 0.97

            # pinos
            for p in self.pegs:
                dx = r.x - p.x
                can_thread = abs(dx) < p.tol and len(p.stack) < CAP
                if can_thread and r.vy > 0.15 and p.top - 6 < r.y < p.top + 26:
                    self.catch(r, p)
                    break
                if can_thread and r.y < p.top + 30:
                    continue
                cx, cy = closest_point((r.x, r.y), (p.x, p.top), (p.x, p.base))
                ddx, ddy = r.x - cx, r.y - cy
                d = math.hypot(ddx, ddy)
                rad = RC + 4
                if d < rad:
                    if d < 1e-6:
                        nx, ny = (1.0 if dx >= 0 else -1.0), 0.0
                    else:
                        nx, ny = ddx / d, ddy / d
                    r.x = cx + nx * rad
                    r.y = cy + ny * rad
                    vn = r.vx * nx + r.vy * ny
                    if vn < 0:
                        r.vx -= 1.4 * vn * nx
                        r.vy -= 1.4 * vn * ny

        # argolas entre si
        for i in range(len(free)):
            for j in range(i + 1, len(free)):
                a, b = free[i], free[j]
                if a.peg or b.peg:
                    continue
                dx, dy = b.x - a.x, b.y - a.y
                d = math.hypot(dx, dy)
                lim = RC * 1.9
                if 0 < d < lim:
                    nx, ny = dx / d, dy / d
                    o = (lim - d) / 2
                    a.x -= nx * o
                    a.y -= ny * o
                    b.x += nx * o
                    b.y += ny * o
                    vn = (a.vx - b.vx) * nx + (a.vy - b.vy) * ny
                    if vn > 0:
                        a.vx -= vn * nx * 0.7
                        a.vy -= vn * ny * 0.7
                        b.vx += vn * nx * 0.7
                        b.vy += vn * ny * 0.7

        # argolas encaixadas: escorregam até a posição da pilha
        for r in self.rings:
            if r.peg:
                ty = r.peg.slot_y(r.slot)
                r.x += (r.peg.x - r.x) * 0.3 * dt
                if r.y < ty:
                    r.y = min(ty, r.y + (1.2 + (ty - r.y) * 0.08) * dt)
                r.phase += 0.0

    def catch(self, r, p):
        r.peg = p
        r.slot = len(p.stack)
        p.stack.append(r)
        r.vx = r.vy = 0.0
        self.caught_total += 1
        if self.combo_timer > 0:
            self.combo += 1
        else:
            self.combo = 1
        self.combo_timer = 240
        mult = min(5, self.combo)
        pts = p.value * (3 if r.gold else 1) * mult
        self.score += pts
        label = f"+{pts}"
        if mult > 1:
            label += f"  COMBO x{mult}"
        self.popup(label, p.x, p.top - 30, (255, 240, 120) if not r.gold else (255, 255, 255), False, 80)
        self.burst(p.x, p.top, p.color if not r.gold else GOLD, 16)
        self.play("gold" if r.gold else "catch")
        if r.gold:
            self.popup("ARGOLA DOURADA x3!", 400, 160, GOLD, True, 90)


# ----------------------------------------------------------------- desenho
class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.f_s = pygame.font.SysFont("arial", 15, bold=True)
        self.f_m = pygame.font.SysFont("arial", 22, bold=True)
        self.f_l = pygame.font.SysFont("arial", 34, bold=True)
        self.f_xl = pygame.font.SysFont("arial", 56, bold=True)
        self.bg = self.make_bg()
        self.rays = self.make_rays()
        self.weed = [(random.uniform(TX0 + 15, TX1 - 15), random.uniform(40, 90), random.uniform(0, 6.28),
                      random.choice([(40, 150, 80), (60, 175, 90), (30, 125, 85)])) for _ in range(14)]

    # fundo estático
    def make_bg(self):
        s = pygame.Surface((W, H))
        for y in range(H):
            k = y / H
            pygame.draw.line(s, (int(20 + 25 * k), int(30 + 20 * k), int(60 + 40 * k)), (0, y), (W, y))
        # água
        for y in range(TY0, TANK_BOTTOM):
            k = (y - TY0) / (TANK_BOTTOM - TY0)
            pygame.draw.line(s, (int(90 - 70 * k), int(200 - 90 * k), int(245 - 70 * k)), (TX0, y), (TX1, y))
        # areia
        pygame.draw.rect(s, (222, 190, 120), (TX0, FLOOR, TX1 - TX0, TANK_BOTTOM - FLOOR))
        rnd = random.Random(4)
        for _ in range(220):
            x, y = rnd.randint(TX0, TX1), rnd.randint(FLOOR, TANK_BOTTOM)
            pygame.draw.circle(s, (205 + rnd.randint(-15, 15), 172 + rnd.randint(-15, 15), 105), (x, y), rnd.randint(1, 2))
        for _ in range(7):  # conchas e pedrinhas
            x, y = rnd.randint(TX0 + 20, TX1 - 20), rnd.randint(FLOOR + 8, TANK_BOTTOM - 8)
            c = rnd.choice([(250, 180, 190), (240, 230, 210), (190, 150, 110)])
            pygame.draw.ellipse(s, c, (x, y, 14, 9))
            pygame.draw.ellipse(s, shade(c, 0.7), (x, y, 14, 9), 1)
        # moldura do tanque
        pygame.draw.rect(s, (250, 200, 50), (TX0 - 18, TY0 - 22, TX1 - TX0 + 36, TANK_BOTTOM - TY0 + 44), border_radius=26)
        pygame.draw.rect(s, (230, 70, 60), (TX0 - 18, TY0 - 22, TX1 - TX0 + 36, TANK_BOTTOM - TY0 + 44), 5, border_radius=26)
        for y in range(TY0, TANK_BOTTOM):
            k = (y - TY0) / (TANK_BOTTOM - TY0)
            pygame.draw.line(s, (int(90 - 70 * k), int(200 - 90 * k), int(245 - 70 * k)), (TX0, y), (TX1, y))
        pygame.draw.rect(s, (222, 190, 120), (TX0, FLOOR, TX1 - TX0, TANK_BOTTOM - FLOOR))
        for _ in range(220):
            x, y = rnd.randint(TX0, TX1), rnd.randint(FLOOR, TANK_BOTTOM - 1)
            pygame.draw.circle(s, (205 + rnd.randint(-15, 15), 172 + rnd.randint(-15, 15), 105), (x, y), rnd.randint(1, 2))
        pygame.draw.rect(s, (255, 255, 255), (TX0, TY0, TX1 - TX0, TANK_BOTTOM - TY0), 2)
        # painel de controle
        pygame.draw.rect(s, (30, 40, 80), (0, 600, W, H - 600))
        pygame.draw.line(s, (250, 200, 50), (0, 600), (W, 600), 4)
        return s

    @staticmethod
    def make_rays():
        s = pygame.Surface((W + 200, TANK_BOTTOM - TY0), pygame.SRCALPHA)
        for i in range(9):
            x = i * 100 + random.randint(-20, 20)
            w = random.randint(25, 60)
            pygame.draw.polygon(s, (255, 255, 255, 22), [(x, 0), (x + w, 0), (x + w - 150, s.get_height()), (x - 150, s.get_height())])
        return s

    def txt(self, font, text, color, center=None, topleft=None, topright=None, shadow=True, alpha=255):
        img = font.render(text, True, color)
        sh = font.render(text, True, (0, 0, 0))
        if alpha < 255:
            img.set_alpha(alpha)
            sh.set_alpha(alpha // 2)
        r = img.get_rect()
        if center:
            r.center = center
        elif topleft:
            r.topleft = topleft
        elif topright:
            r.topright = topright
        if shadow:
            self.screen.blit(sh, (r.x + 2, r.y + 2))
        self.screen.blit(img, r)

    # ---- cena
    def draw(self, g, left, right):
        sc = self.screen
        sc.blit(self.bg, (0, 0))
        clip = pygame.Rect(TX0, TY0, TX1 - TX0, TANK_BOTTOM - TY0)
        sc.set_clip(clip)

        # raios de luz
        off = int(math.sin(g.t * 0.008) * 60) + 100
        sc.blit(self.rays, (TX0 - off, TY0))

        # peixes (fundo)
        for f in g.fish:
            self.draw_fish(f, g.t)

        # algas
        for x, h, ph, c in self.weed:
            pts = []
            for i in range(9):
                yy = FLOOR + 6 - h * i / 8
                xx = x + math.sin(g.t * 0.04 + ph + i * 0.5) * (i * 1.6)
                pts.append((xx, yy))
            pygame.draw.lines(sc, c, False, pts, 6)

        # bolhas
        for b in g.bubbles:
            pygame.draw.circle(sc, (200, 235, 255), (int(b["x"]), int(b["y"])), int(b["r"]), 1)

        # postes dos pinos
        for p in g.pegs:
            pygame.draw.rect(sc, (140, 150, 170), (p.x - 4, p.top, 8, FLOOR - p.top + 6))
            pygame.draw.rect(sc, (200, 210, 230), (p.x - 4, p.top, 3, FLOOR - p.top + 6))
            pygame.draw.ellipse(sc, shade(p.color, 0.7), (p.x - 18, FLOOR - 6, 36, 16))
            pygame.draw.ellipse(sc, p.color, (p.x - 18, FLOOR - 10, 36, 16))

        # metade de trás das argolas encaixadas
        caught = [r for r in g.rings if r.peg]
        for r in caught:
            draw_ring(sc, r.x, r.y, R * 0.82, R * 0.30, 6, r.color, "back")
        # pinos (parte da frente do poste)
        for p in g.pegs:
            pygame.draw.rect(sc, shade(p.color, 0.8), (p.x - 4, p.top, 8, p.base - p.top))
            pygame.draw.rect(sc, shade(p.color, 1.3), (p.x - 4, p.top, 3, p.base - p.top))
            pygame.draw.circle(sc, p.color, (p.x, p.top), 6)
            pygame.draw.circle(sc, shade(p.color, 1.5), (p.x - 2, p.top - 2), 2)
            self.txt(self.f_s, str(p.value), (255, 255, 255), center=(p.x, p.top - 16), alpha=190)
        for r in caught:
            draw_ring(sc, r.x, r.y, R * 0.82, R * 0.30, 6, r.color, "front")

        # argolas livres
        for r in g.rings:
            if r.peg:
                continue
            ry = R * (0.42 + 0.58 * abs(math.cos(r.phase)))
            rx = R * (0.72 + 0.28 * abs(math.sin(r.phase * 0.7 + 1)))
            draw_ring(sc, r.x, r.y, rx, ry, THICK, r.color, "full",
                      sparkle=(g.t * 0.1) if r.gold else 0.0)

        # bocais dos jatos
        for j, pressed in zip(g.jets, (left, right)):
            ang = math.atan2(j.dy, j.dx)
            base = [(j.x - 16, FLOOR + 10), (j.x + 16, FLOOR + 10), (j.x + 9, FLOOR - 8), (j.x - 9, FLOOR - 8)]
            pygame.draw.polygon(sc, (110, 120, 140), base)
            tip = (j.x + j.dx * 22, j.y + j.dy * 22)
            pygame.draw.line(sc, (190, 200, 220), (j.x, j.y), tip, 14)
            pygame.draw.circle(sc, (230, 240, 255) if pressed else (150, 160, 180), (int(tip[0]), int(tip[1])), 8)

        # partículas
        for p in g.fx:
            col = p["c"]
            if p.get("bub"):
                pygame.draw.circle(sc, col, (int(p["x"]), int(p["y"])), int(p["r"]), 1)
            else:
                pygame.draw.circle(sc, col, (int(p["x"]), int(p["y"])), int(p["r"]))

        # superfície com ondas
        pts = [(TX0, TY0 - 6)]
        for x in range(TX0, TX1 + 1, 10):
            pts.append((x, TY0 - 2 + math.sin(g.t * 0.05 + x * 0.03) * 3))
        pts.append((TX1, TY0 - 6))
        pygame.draw.polygon(sc, (190, 235, 255), pts)

        sc.set_clip(None)
        # vidro (reflexo)
        glass = pygame.Surface((90, TANK_BOTTOM - TY0), pygame.SRCALPHA)
        pygame.draw.polygon(glass, (255, 255, 255, 28), [(0, 0), (40, 0), (10, glass.get_height()), (0, glass.get_height())])
        sc.blit(glass, (TX0 + 14, TY0))

        # textos flutuantes
        for t in g.texts:
            font = self.f_l if t["big"] else self.f_m
            self.txt(font, t["t"], t["c"], center=(t["x"], t["y"]), alpha=min(255, t["life"] * 10))

        self.draw_hud(g, left, right)
        if g.paused:
            self.veil(120)
            self.txt(self.f_xl, "PAUSA", (255, 255, 255), center=(W // 2, 300))
        if g.state == "menu":
            self.draw_menu(g)
        elif g.state == "over":
            self.draw_over(g)

    def draw_fish(self, f, t):
        x, y, d, s = f["x"], f["y"], f["d"], f["size"]
        c = f["c"]
        wag = math.sin(t * 0.2 + f["ph"]) * 4
        body = pygame.Rect(0, 0, s * 2.2, s * 1.3)
        body.center = (x, y)
        pygame.draw.ellipse(self.screen, c, body)
        tail = [(x - d * s * 1.0, y), (x - d * s * 1.9, y - s * 0.7 + wag), (x - d * s * 1.9, y + s * 0.7 + wag)]
        pygame.draw.polygon(self.screen, shade(c, 0.85), tail)
        pygame.draw.circle(self.screen, (255, 255, 255), (int(x + d * s * 0.6), int(y - s * 0.15)), max(2, int(s * 0.22)))
        pygame.draw.circle(self.screen, (20, 20, 40), (int(x + d * s * 0.65), int(y - s * 0.15)), max(1, int(s * 0.1)))

    def veil(self, a):
        v = pygame.Surface((W, H), pygame.SRCALPHA)
        v.fill((5, 15, 40, a))
        self.screen.blit(v, (0, 0))

    def draw_hud(self, g, left, right):
        sc = self.screen
        pygame.draw.rect(sc, (20, 30, 70), (0, 0, W, 64))
        pygame.draw.line(sc, (250, 200, 50), (0, 64), (W, 64), 3)
        fmt = lambda n: f"{n:,}".replace(",", ".")
        self.txt(self.f_s, "PONTOS", (150, 180, 255), topleft=(24, 8))
        self.txt(self.f_l, fmt(g.score), (255, 255, 255), topleft=(24, 22))
        self.txt(self.f_s, "RECORDE", (150, 180, 255), center=(400, 16))
        self.txt(self.f_m, fmt(max(g.high, g.score)), (255, 215, 90), center=(400, 42))
        # tempo
        low = g.state == "play" and g.time_left < 10
        tcol = (255, 90, 90) if low and int(g.time_left * 2) % 2 == 0 else (255, 255, 255)
        self.txt(self.f_s, f"RODADA {g.round}", (150, 180, 255), topright=(776, 8))
        self.txt(self.f_l, f"{max(0, int(math.ceil(g.time_left))):02d}s", tcol, topright=(776, 22))
        # argolas restantes
        total = len(g.rings)
        done = sum(1 for r in g.rings if r.peg)
        self.txt(self.f_s, f"ARGOLAS {done}/{total}", (150, 180, 255), topleft=(560, 8))
        for i, r in enumerate(g.rings):
            cx = 566 + i * 15
            pygame.draw.circle(sc, r.color if r.peg else (70, 85, 130), (cx, 46), 6, 0 if r.peg else 2)
        if g.combo >= 2 and g.combo_timer > 0:
            self.txt(self.f_m, f"COMBO x{min(5, g.combo)}", (120, 255, 200), center=(230, 42))
            pygame.draw.rect(sc, (120, 255, 200), (180, 56, int(100 * g.combo_timer / 240), 4))

        # painel dos botões
        self.draw_button(g, 200, 640, left, (50, 120, 240), "left", "Z")
        self.draw_button(g, 600, 640, right, (230, 60, 70), "right", "M")
        self.txt(self.f_s, "SETA ESQUERDA / Z", (150, 180, 255), center=(200, 688), shadow=False)
        self.txt(self.f_s, "SETA DIREITA / M", (150, 180, 255), center=(600, 688), shadow=False)
        self.txt(self.f_s, "ESPAÇO = os dois jatos", (200, 210, 255), center=(400, 628), shadow=False)
        self.txt(self.f_s, "P: pausa   R: recomeçar", (120, 140, 190), center=(400, 656), shadow=False)

    def draw_button(self, g, cx, cy, pressed, color, side, key):
        sc = self.screen
        pygame.draw.circle(sc, (15, 20, 45), (cx, cy + 5), 42)
        c = shade(color, 1.25) if pressed else color
        dy = 3 if pressed else 0
        pygame.draw.circle(sc, shade(color, 0.6), (cx, cy + dy), 40)
        pygame.draw.circle(sc, c, (cx, cy + dy + (1 if pressed else 0)), 36)
        pygame.draw.circle(sc, shade(c, 1.35), (cx - 11, cy - 12 + dy), 8)
        d = -1 if side == "left" else 1
        yy = cy + dy
        pygame.draw.polygon(sc, (255, 255, 255), [(cx + d * 17, yy), (cx - d * 5, yy - 14), (cx - d * 5, yy + 14)])
        self.txt(self.f_s, key, (255, 255, 255), center=(cx + d * 22, yy + 21), shadow=False)

    def draw_menu(self, g):
        self.veil(150)
        bob = math.sin(g.t * 0.05) * 6
        self.txt(self.f_xl, "ARGOLAS", (255, 215, 70), center=(W // 2, 190 + bob))
        self.txt(self.f_xl, "AQUÁTICAS", (110, 215, 255), center=(W // 2, 255 + bob))
        lines = ["Use os jatos para lançar as argolas e encaixe nas hastes!",
                 "Pino do meio vale 300, os dos lados 100. Argola dourada vale x3.",
                 "Encaixes seguidos fazem COMBO. Termine antes do tempo acabar!"]
        for i, l in enumerate(lines):
            self.txt(self.f_s, l, (230, 240, 255), center=(W // 2, 340 + i * 26))
        if (g.t // 30) % 2 == 0:
            self.txt(self.f_m, "Pressione ESPAÇO ou clique para começar", (255, 255, 255), center=(W // 2, 460))

    def draw_over(self, g):
        self.veil(170)
        self.txt(self.f_xl, "TEMPO ESGOTADO!", (255, 110, 120), center=(W // 2, 220))
        self.txt(self.f_l, f"Pontos: {g.score:,}".replace(",", "."), (255, 255, 255), center=(W // 2, 300))
        self.txt(self.f_m, f"Rodada alcançada: {g.round}", (200, 220, 255), center=(W // 2, 345))
        if g.new_record:
            self.txt(self.f_l, "NOVO RECORDE!", (255, 215, 70), center=(W // 2, 395))
        self.txt(self.f_m, "Pressione R ou clique para jogar de novo", (255, 255, 255), center=(W // 2, 470))


BUTTONS = {"left": (200, 650), "right": (600, 650)}


def mouse_buttons():
    l = r = False
    if pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()
        l = (mx - 200) ** 2 + (my - 640) ** 2 < 46 ** 2
        r = (mx - 600) ** 2 + (my - 640) ** 2 < 46 ** 2
    return l, r


def main():
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Argolas Aquáticas")
    clock = pygame.time.Clock()
    game = Game()
    rend = Renderer(screen)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE and game.state == "menu":
                    game.start()
                elif e.key == pygame.K_r:
                    game.start()
                elif e.key == pygame.K_p and game.state == "play":
                    game.paused = not game.paused
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                mx, my = e.pos
                on_button = my > 590
                if game.state in ("menu", "over") and not on_button:
                    game.start()

        k = pygame.key.get_pressed()
        ml, mr = mouse_buttons()
        both = k[pygame.K_SPACE]
        left = bool(k[pygame.K_LEFT] or k[pygame.K_z] or ml or both)
        right = bool(k[pygame.K_RIGHT] or k[pygame.K_m] or mr or both)
        if game.state == "over":
            left = right = False
        game.update(left, right)
        rend.draw(game, left, right)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()