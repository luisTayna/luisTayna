# -*- coding: utf-8 -*-
"""Generates the profile SVG assets (dark and light variants)."""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets')
os.makedirs(OUT, exist_ok=True)
SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', 'Cascadia Code', Consolas, 'SFMono-Regular', Menlo, monospace"

THEMES = {
    'dark': dict(bg='#0d1117', panel='#161b22', line='#30363d', ink='#e6edf3', muted='#8b949e',
                 accent='#58a6ff', ok='#3fb950', grid='#1c2330', amber='#d29922', red='#f85149'),
    'light': dict(bg='#ffffff', panel='#f6f8fa', line='#d0d7de', ink='#1f2328', muted='#59636e',
                  accent='#0969da', ok='#1a7f37', grid='#eef1f4', amber='#9a6700', red='#cf222e'),
}


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def banner(t):
    W, H = 1200, 330
    grid = ''.join('<line x1="%d" y1="0" x2="%d" y2="%d" stroke="%s" stroke-width="1"/>' % (x, x, H, t['grid'])
                   for x in range(0, W, 40))
    grid += ''.join('<line x1="0" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1"/>' % (y, W, y, t['grid'])
                    for y in range(0, H, 40))
    metrics = [('48% → 100%', 'cobranza automática'), ('601 → 3', 'consultas SQL'),
               ('173 → 230', 'pruebas automatizadas'), ('302', 'commits · Centro Electoral')]
    tiles = ''
    for i, (v, l) in enumerate(metrics):
        x = 742 + (i % 2) * 222
        y = 54 + (i // 2) * 116
        tiles += (
            '<g class="tile" style="animation-delay:%.1fs">'
            '<rect x="%d" y="%d" width="206" height="100" rx="10" fill="%s" stroke="%s"/>'
            '<text x="%d" y="%d" font-family="%s" font-size="26" font-weight="700" fill="%s">%s</text>'
            '<text x="%d" y="%d" font-family="%s" font-size="13.5" fill="%s">%s</text></g>'
        ) % (0.15 * i, x, y, t['panel'], t['line'], x + 18, y + 48, SANS, t['accent'], esc(v),
             x + 18, y + 76, SANS, t['muted'], esc(l))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Jose Luis Quispe Tayña — Backend / Full-Stack Developer">
<style>
  @keyframes blink {{ 0%,49% {{opacity:1}} 50%,100% {{opacity:0}} }}
  @keyframes rise {{ from {{opacity:0; transform:translateY(8px)}} to {{opacity:1; transform:none}} }}
  @keyframes type {{ from {{width:0}} to {{width:330px}} }}
  .cursor {{ animation: blink 1.1s steps(1) infinite; }}
  .tile {{ opacity:0; animation: rise .6s ease-out forwards; }}
  .pass {{ opacity:0; animation: rise .5s ease-out 1.4s forwards; }}
  @media (prefers-reduced-motion: reduce) {{ .cursor, .tile, .pass {{ animation:none; opacity:1; }} }}
</style>
<rect width="{W}" height="{H}" rx="14" fill="{t['bg']}"/>
<g opacity=".7">{grid}</g>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{t['line']}"/>
<text x="56" y="92" font-family="{MONO}" font-size="15" fill="{t['muted']}">~/luisTayna</text>
<text x="56" y="146" font-family="{SANS}" font-size="46" font-weight="800" fill="{t['ink']}">Jose Luis Quispe Tayña</text>
<text x="56" y="184" font-family="{SANS}" font-size="20" fill="{t['muted']}">Backend / Full-Stack Developer · Cusco, Perú</text>
<rect x="56" y="214" width="610" height="74" rx="10" fill="{t['panel']}" stroke="{t['line']}"/>
<text x="76" y="244" font-family="{MONO}" font-size="16" fill="{t['ink']}"><tspan fill="{t['ok']}">$</tspan> php artisan test</text>
<g class="pass"><text x="76" y="272" font-family="{MONO}" font-size="16" fill="{t['ok']}">✓ Tests: 230 passed</text>
<text x="292" y="272" font-family="{MONO}" font-size="16" fill="{t['muted']}">· software que se puede demostrar</text></g>
<rect class="cursor" x="642" y="257" width="10" height="20" fill="{t['accent']}"/>
{tiles}
</svg>'''


def card(t, accent, kicker, title, lines, stack, footer):
    W, H = 580, 330
    body = ''
    for i, ln in enumerate(lines):
        y = 152 + i * 30
        body += ('<circle cx="40" cy="%d" r="3.5" fill="%s"/><text x="54" y="%d" font-family="%s" font-size="15.5" fill="%s">%s</text>'
                 % (y - 5, accent, y, SANS, t['ink'], esc(ln)))
    chips, x = '', 32
    for s in stack:
        w = 16 + len(s) * 7.4
        chips += ('<rect x="%d" y="268" width="%d" height="28" rx="14" fill="%s" stroke="%s"/>'
                  '<text x="%d" y="287" font-family="%s" font-size="12.5" fill="%s">%s</text>'
                  % (x, w, t['panel'], t['line'], x + 8, MONO, t['muted'], esc(s)))
        x += w + 8
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(title)}">
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="{t['bg']}" stroke="{t['line']}"/>
<rect x="0" y="0" width="{W}" height="6" rx="3" fill="{accent}"/>
<text x="32" y="50" font-family="{MONO}" font-size="13" fill="{accent}">{esc(kicker)}</text>
<text x="32" y="88" font-family="{SANS}" font-size="28" font-weight="800" fill="{t['ink']}">{esc(title)}</text>
<text x="32" y="116" font-family="{SANS}" font-size="14.5" fill="{t['muted']}">{esc(footer)}</text>
{body}
{chips}
</svg>'''


for name, t in THEMES.items():
    open(os.path.join(OUT, 'banner-%s.svg' % name), 'w', encoding='utf8').write(banner(t))
    open(os.path.join(OUT, 'card-electoral-%s.svg' % name), 'w', encoding='utf8').write(card(
        t, t['amber'], '// autor principal · 2026', 'Centro Electoral Cusco',
        ['Personeros, actas y resultados por territorio', 'JWT en cookie HttpOnly · acceso fail-closed',
         'Historial inmutable de actas y asignaciones', '20+ suites de pruebas de integración'],
        ['Next.js 15', 'TypeScript', 'PostgreSQL', 'Prisma', 'Docker'],
        'Plataforma de control electoral para Cusco'))
    open(os.path.join(OUT, 'card-noretel-%s.svg' % name), 'w', encoding='utf8').write(card(
        t, t['accent'], '// en producción · ISP', 'NoreTel CRM',
        ['Cobranza Yape por WhatsApp + OCR: 48% → 100%', 'Guarda transaccional contra doble cobro',
         'Auditoría OWASP · 601 → 3 consultas SQL', 'Suite de pruebas de 173 a 230'],
        ['Laravel 10', 'MySQL', 'NestJS', 'Python', 'PHPUnit'],
        'CRM modular para un proveedor de internet'))
print('assets ok:', sorted(os.listdir(OUT)))
