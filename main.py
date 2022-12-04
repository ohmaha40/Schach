import pygame as pg
def sz2xy(sz):
    return sz[0]*FELD, sz[1]*FELD
def zeichneBrett(BRETT):
    for sz, feld in BRETT.items():
        farbe ='#DFBF93' if feld else '#C5844E'
        pg.draw.rect(fenster, farbe, (*sz2xy(sz), FELD, FELD))
def fen2position(fen):
    position, s, z = {}, 0, 0
    figurenstellung, zugrecht, rochaderechte, enpassant, zug50, zugnr = fen.split()
    for char in figurenstellung:
        if char.isalpha():
            position[(s, z)] = char
            s += 1
        elif char.isnumeric():
            s += int(char)
        else:
            s, z = 0, z + 1
    return position, zugrecht
def ladeFiguren():
    bilder = {}
    fig2datei = dict(r='br', n='bn', b='bb', q='bq', k='bk', p='bp',
                     R='wr', N='wn', B='wb', Q='wq', K='wk', P='wp')
    for fig, datei in fig2datei.items():
        bild = pg.image.load(f'img/{datei}.png')
        bilder[fig] = pg.transform.smoothscale(bild, (FELD, FELD))
    return bilder
def zeichneFiguren(p):
    for sz, fig in p.items():
        fenster.blit(FIGUREN[fig], sz2xy(sz))

#todo: 48:30 min weiter

pg.init()
größe = breite, höhe = 800, 800
FELD = breite // 8
fenster = pg.display.set_mode(größe)
clock = pg.time.Clock()
FPS = 40
BRETT = {(s, z): s % 2 == z % 2 for s in range(8) for z in range(8)}
FIGUREN = ladeFiguren()
fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
position, zugrecht = fen2position(fen)

# Zeichenschleife mit FPS Bildern pro Sekunde
while True:
    clock.tick(FPS)
    for ereignis in pg.event.get():
        if ereignis.type == pg.QUIT or \
                ereignis.type == pg.KEYDOWN and ereignis.key == pg.K_ESCAPE:
            quit()

    fenster.fill('black')
    zeichneBrett(BRETT)
    zeichneFiguren(position)
    pg.display.flip()
pg.QUIT