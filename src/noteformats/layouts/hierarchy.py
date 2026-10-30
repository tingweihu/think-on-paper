from __future__ import annotations

from ..geometry import Scene


def top_down_tree(s: Scene, p: dict):
    cx=(s.left+s.right)/2
    root_y=s.top+8
    s.rect(cx-22,root_y,44,27,"strong")
    s.slot(cx-19,root_y+16,38)
    branch_y=s.top+75
    children=[(cx-30,branch_y),(cx+30,branch_y)]
    s.line(cx,root_y+27,cx,root_y+46,"light")
    s.line(cx-30,root_y+46,cx+30,root_y+46,"light")
    for x,y in children:
        s.line(x,root_y+46,x,y,"light")
        s.rect(x-17,y,34,26,"normal")
        s.slot(x-14,y+16,28)
    leaf_y=s.bottom-36
    leaves=[s.left+14,s.left+43,s.right-43,s.right-14]
    for parent, group in zip(children,(leaves[:2],leaves[2:])):
        px,py=parent
        s.line(px,py+26,px,py+42,"light")
        s.line(group[0],py+42,group[1],py+42,"light")
        for x in group:
            s.line(x,py+42,x,leaf_y,"light")
            s.rect(x-12,leaf_y,24,26,"normal")
            s.slot(x-10,leaf_y+16,20)


def stepped_hierarchy(s: Scene, p: dict):
    top=s.top+16
    for i in range(4):
        inset=7+i*14
        x=s.left+inset; y=top+i*41
        w=s.width-inset-8
        s.rect(x,y,w,30,"normal" if i else "strong")
        s.slot(x+4,y+18,w-8)
        if i<3:
            s.line(x+7,y+31,x+7,y+40,"light")
            s.line(x+7,y+40,x+21,y+40,"light")


def brace_decomposition(s: Scene, p: dict):
    cy=(s.top+s.bottom)/2
    s.rect(s.left+2,cy-23,32,46,"strong")
    s.slot(s.left+5,cy+2,26)
    x0=s.left+38; x1=s.left+49
    s.line(x0,cy,x1,cy,"normal")
    s.polyline([(x1+6,cy-65),(x1,cy-65),(x1,cy+65),(x1+6,cy+65)],"normal")
    ys=[cy-58,cy,cy+58]
    for y in ys:
        s.line(x1+6,y,s.left+67,y,"light")
        s.rect(s.left+67,y-18,s.width-69,36,"normal")
        s.slot(s.left+71,y+2,s.width-77)


def pyramid_three(s: Scene, p: dict):
    cx=(s.left+s.right)/2
    top=s.top+11; bottom=s.bottom-13
    left=s.left+8; right=s.right-8
    s.polyline([(cx,top),(right,bottom),(left,bottom)],"normal",closed=True)
    for frac in (1/3,2/3):
        y=top+(bottom-top)*frac
        half=(right-left)*frac/2
        s.line(cx-half,y,cx+half,y,"normal")
    s.slot(cx-7,top+45,14)
    s.slot(cx-22,top+98,44)
    s.slot(cx-39,top+151,78)


def nested_rectangles(s: Scene, p: dict):
    for i in range(4):
        x=s.left+7+i*11
        y=s.top+11+i*19
        w=s.width-14-i*22
        h=s.height-22-i*38
        s.rect(x,y,w,h,"normal" if i else "light")
        s.slot(x+3,y+10,min(w-6,27))


def classification_wheel(s: Scene, p: dict):
    from math import cos, pi, sin
    cx=(s.left+s.right)/2; cy=(s.top+s.bottom)/2
    outer=58; inner=18
    s.circle(cx,cy,outer,"normal")
    s.circle(cx,cy,inner,"strong")
    s.slot(cx-13,cy+2,26)
    for i in range(8):
        a=-pi/2+i*pi/4
        s.line(cx+inner*cos(a),cy+inner*sin(a),cx+outer*cos(a),cy+outer*sin(a),"normal")
        mid=a+pi/8
        x=cx+38*cos(mid); y=cy+38*sin(mid)
        s.slot(x-8,y+2,16)


BUILDERS={
    "top-down-tree":top_down_tree,
    "stepped-hierarchy":stepped_hierarchy,
    "brace-decomposition":brace_decomposition,
    "pyramid-three":pyramid_three,
    "nested-rectangles":nested_rectangles,
    "classification-wheel":classification_wheel,
}
