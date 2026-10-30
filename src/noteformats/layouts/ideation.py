from __future__ import annotations

from ..geometry import Scene


def many_to_one_funnel(s: Scene, p: dict):
    cx=(s.left+s.right)/2
    top_y=s.top+25
    xs=[s.left+10+i*(s.width-20)/5 for i in range(6)]
    for x in xs:
        s.circle(x,top_y,8,"normal")
        s.slot(x-6,top_y+2,12)
    mid_y=s.top+92
    mids=[cx-28,cx+28]
    for i,x in enumerate(mids):
        s.rect(x-18,mid_y-18,36,36,"normal")
        s.slot(x-15,mid_y+3,30)
        for top_x in xs[i*3:i*3+3]:
            s.line(top_x,top_y+9,x,mid_y-20,"light")
    bottom_y=s.bottom-47
    s.rect(cx-39,bottom_y,78,40,"strong")
    s.slot(cx-35,bottom_y+22,70)
    for x in mids:
        s.line(x,mid_y+19,cx,bottom_y-2,"light")


def three_sketch_proposals(s: Scene, p: dict):
    gap=6; h=(s.height-2*gap)/3
    sketch_w=s.width*0.67
    for i in range(3):
        y=s.top+i*(h+gap)
        s.rect(s.left,y,sketch_w,h,"normal")
        s.slot(s.left+6,y+18,sketch_w-12)
        x=s.left+sketch_w+5; w=s.width-sketch_w-5
        s.rect(x,y,w,h,"normal")
        for n in range(1,4):
            yy=y+n*h/4
            s.line(x+3,yy,x+w-3,yy,"light")
        s.slot(x+3,y+17,w-6)


def abstraction_ladder(s: Scene, p: dict):
    left=s.left+18; right=s.right-18
    top=s.top+12; bottom=s.bottom-12
    s.line(left,top,left,bottom,"normal")
    s.line(right,top,right,bottom,"normal")
    for i in range(5):
        y=top+12+i*(bottom-top-24)/4
        s.line(left,y,right,y,"normal")
        s.slot(left+5,y-5,right-left-10)
    s.polyline([(left-8,top+9),(left-12,top),(left-16,top+9)],"light")
    s.line(left-12,top,left-12,bottom,"light")


BUILDERS={
    "many-to-one-funnel":many_to_one_funnel,
    "three-sketch-proposals":three_sketch_proposals,
    "abstraction-ladder":abstraction_ladder,
}
