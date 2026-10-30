from __future__ import annotations

from ..geometry import Scene


def music_staff(s: Scene, p: dict):
    for group in range(6):
        y=s.top+18+group*30
        for i in range(5):
            s.line(s.left+3,y+i*2.7,s.right-3,y+i*2.7,"normal")
        if group==0:
            for x in (s.left+24,s.left+54,s.left+84):
                s.slot(x,y+6,14)


def guitar_tablature(s: Scene, p: dict):
    for group in range(5):
        y=s.top+16+group*35
        for i in range(6):
            s.line(s.left+3,y+i*2.7,s.right-3,y+i*2.7,"normal")
        for x in (s.left+39,s.left+78):
            s.line(x,y,x,y+13.5,"light")
        if group==0:
            for x in (s.left+20,s.left+58,s.left+97):
                s.slot(x,y+10,13)


def _hanzi(s: Scene, style: str):
    cell=21; gap=3; cols=5; rows=7
    total_w=cols*cell+(cols-1)*gap
    total_h=rows*cell+(rows-1)*gap
    x0=(s.left+s.right-total_w)/2
    y0=(s.top+s.bottom-total_h)/2
    for row in range(rows):
        for col in range(cols):
            x=x0+col*(cell+gap); y=y0+row*(cell+gap)
            s.rect(x,y,cell,cell,"normal")
            if style in ("tian","mi"):
                s.line(x+cell/2,y,x+cell/2,y+cell,"light")
                s.line(x,y+cell/2,x+cell,y+cell/2,"light")
            if style=="mi":
                s.line(x,y,x+cell,y+cell,"light")
                s.line(x+cell,y,x,y+cell,"light")
            if style=="nine":
                for n in (1,2):
                    s.line(x+cell*n/3,y,x+cell*n/3,y+cell,"light")
                    s.line(x,y+cell*n/3,x+cell,y+cell*n/3,"light")
            if row==0 and col<3:
                s.slot(x+3,y+13,cell-6)


def hanzi_tian(s: Scene, p: dict):
    _hanzi(s,"tian")


def hanzi_mi(s: Scene, p: dict):
    _hanzi(s,"mi")


def hanzi_nine(s: Scene, p: dict):
    _hanzi(s,"nine")


def seyes_ruled(s: Scene, p: dict):
    y=s.top+8
    n=0
    while y <= s.bottom-8:
        s.line(s.left+4,y,s.right-4,y,"normal" if n%4==0 else "light")
        y+=2
        n+=1
    s.line(s.left+13,s.top+5,s.left+13,s.bottom-5,"normal")
    for x in (s.left+19,s.left+49,s.left+79):
        s.slot(x,s.top+30,22)


def perspective_guides(s: Scene, p: dict):
    horizon=s.top+s.height*0.46
    left_vp=s.left+22; right_vp=s.right-22
    s.line(s.left,horizon,s.right,horizon,"normal")
    for x in (left_vp,right_vp):
        s.circle(x,horizon,2,"strong")
    for vp in (left_vp,right_vp):
        for x in (s.left+6,(s.left+s.right)/2,s.right-6):
            s.line(vp,horizon,x,s.bottom-8,"light")
        s.line(vp,horizon,(s.left+s.right)/2,s.top+16,"light")
    s.slot(s.left+7,s.top+21,s.width-14)


BUILDERS={
    "music-staff":music_staff,
    "guitar-tablature":guitar_tablature,
    "hanzi-tian":hanzi_tian,
    "hanzi-mi":hanzi_mi,
    "hanzi-nine":hanzi_nine,
    "seyes-ruled":seyes_ruled,
    "perspective-guides":perspective_guides,
}
