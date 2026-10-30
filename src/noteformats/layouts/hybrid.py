from __future__ import annotations

from math import cos, pi, sin

from ..geometry import Scene
from .flow import arrow


def dot_and_blank(s: Scene, p: dict):
    split=s.top+s.height*0.52
    s.line(s.left,split,s.right,split,"normal")
    pitch=5
    for row in range(int((split-s.top-12)/pitch)):
        for col in range(int((s.width-12)/pitch)):
            s.dot(s.left+6+col*pitch,s.top+6+row*pitch,p["dot_diameter_mm"],"light")
    s.slot(s.left+8,s.top+22,s.width-16)
    s.slot(s.left+8,split+24,s.width-16)


def mindmap_and_ruled(s: Scene, p: dict):
    cx=(s.left+s.right)/2; cy=s.top+56
    s.circle(cx,cy,14,"strong"); s.slot(cx-11,cy+2,22)
    for i in range(4):
        a=-pi/2+i*pi/2
        x=cx+45*cos(a); y=cy+35*sin(a)
        s.line(cx+15*cos(a),cy+15*sin(a),x-11*cos(a),y-11*sin(a),"light")
        s.circle(x,y,10,"normal"); s.slot(x-8,y+2,16)
    split=s.top+106
    s.line(s.left,split,s.right,split,"strong")
    for y in range(int(split)+9,int(s.bottom)-2,8):
        s.line(s.left+4,y,s.right-4,y,"light")
    s.slot(s.left+6,split+18,s.width-12)


def center_with_notes(s: Scene, p: dict):
    cx=(s.left+s.right)/2; cy=(s.top+s.bottom)/2
    s.circle(cx,cy,24,"strong"); s.slot(cx-17,cy+2,34)
    regions=[(s.left+2,s.top+9),(s.right-48,s.top+9),(s.left+2,s.bottom-65),(s.right-48,s.bottom-65)]
    for x,y in regions:
        s.rect(x,y,46,56,"normal")
        for n in range(1,5):
            yy=y+n*10
            s.line(x+4,yy,x+42,yy,"light")
        s.slot(x+4,y+17,38)
    for x1,y1,x2,y2 in ((cx-17,cy-17,cx-28,cy-28),(cx+17,cy-17,cx+28,cy-28),
                         (cx-17,cy+17,cx-28,cy+28),(cx+17,cy+17,cx+28,cy+28)):
        s.line(x1,y1,x2,y2,"light")


def three_cards_and_ruled(s: Scene, p: dict):
    gap=5; w=(s.width-2*gap)/3
    for i in range(3):
        x=s.left+i*(w+gap)
        s.rect(x,s.top+6,w,62,"normal")
        s.slot(x+4,s.top+25,w-8)
    split=s.top+80
    s.line(s.left,split,s.right,split,"strong")
    for y in range(int(split)+9,int(s.bottom)-3,8):
        s.line(s.left+4,y,s.right-4,y,"light")
    s.slot(s.left+6,split+18,s.width-12)


def flow_and_free(s: Scene, p: dict):
    top=s.top+22; w=24; h=30; gap=(s.width-4*w)/3
    for i in range(4):
        x=s.left+i*(w+gap)
        s.rect(x,top,w,h,"normal")
        s.slot(x+3,top+17,w-6)
        if i<3:
            arrow(s,x+w+1,top+h/2,x+w+gap-1,top+h/2,"light")
    split=s.top+83
    s.line(s.left,split,s.right,split,"strong")
    s.slot(s.left+7,split+24,s.width-14)


def mixed_quadrant(s: Scene, p: dict):
    cx=(s.left+s.right)/2; cy=(s.top+s.bottom)/2
    s.line(cx,s.top,cx,s.bottom,"strong")
    s.line(s.left,cy,s.right,cy,"strong")
    for y in range(int(s.top)+13,int(cy)-3,8):
        s.line(s.left+5,y,cx-5,y,"light")
    for y in range(int(cy)+12,int(s.bottom)-3,8):
        s.line(cx+5,y,s.right-5,y,"light")
    for row in range(8):
        for col in range(8):
            s.dot(cx+6+col*6,s.top+8+row*7,p["dot_diameter_mm"],"light")
    for x,y in ((s.left+6,s.top+25),(cx+5,s.top+25),(s.left+6,cy+25),(cx+5,cy+25)):
        s.slot(x,y,s.width/2-12)


def hybrid_multi_zone(s: Scene, p: dict):
    gap=5; card_w=(s.width-2*gap)/3
    for i in range(3):
        x=s.left+i*(card_w+gap)
        s.rect(x,s.top+4,card_w,34,"normal")
        s.slot(x+3,s.top+22,card_w-6)
    sketch_y=s.top+48
    s.rect(s.left,sketch_y,s.width,78,"normal")
    s.slot(s.left+7,sketch_y+20,s.width-14)
    rule_y=s.top+139
    s.line(s.left,rule_y,s.right,rule_y,"strong")
    for y in range(int(rule_y)+8,int(s.bottom)-3,8):
        s.line(s.left+4,y,s.right-4,y,"light")
    s.slot(s.left+6,rule_y+18,s.width-12)


BUILDERS={
    "dot-and-blank":dot_and_blank,
    "mindmap-and-ruled":mindmap_and_ruled,
    "center-with-notes":center_with_notes,
    "three-cards-and-ruled":three_cards_and_ruled,
    "flow-and-free":flow_and_free,
    "mixed-quadrant":mixed_quadrant,
    "hybrid-multi-zone":hybrid_multi_zone,
}
