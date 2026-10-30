from __future__ import annotations

from ..geometry import Scene


def _frame(s: Scene, x, y, w, h):
    s.rect(x,y,w,h,"normal")
    s.line(x,y+h-9,x+w,y+h-9,"light")
    s.slot(x+3,y+h-2,w-6)


def storyboard_eight_mixed(s: Scene, p: dict):
    half=(s.width-6)/2
    for i in range(2):
        _frame(s,s.left+i*(half+6),s.top+4,half,52)
    small=(s.width-3*4)/4
    for i in range(4):
        _frame(s,s.left+i*(small+4),s.top+66,small,45)
    for i in range(2):
        _frame(s,s.left+i*(half+6),s.top+121,half,55)


def main_sketch_side_notes(s: Scene, p: dict):
    sketch_w=s.width*0.66
    s.rect(s.left,s.top+5,sketch_w,s.height-10,"normal")
    s.slot(s.left+7,s.top+30,sketch_w-14)
    x=s.left+sketch_w+6; w=s.width-sketch_w-6
    s.rect(x,s.top+5,w,s.height-10,"normal")
    for n in range(1,13):
        y=s.top+5+n*(s.height-10)/13
        s.line(x+4,y,x+w-4,y,"light")
    s.slot(x+4,s.top+24,w-8)


def detail_sketch(s: Scene, p: dict):
    main_w=s.width*0.62
    s.rect(s.left,s.top+6,main_w,s.height-12,"normal")
    s.slot(s.left+7,s.top+27,main_w-14)
    x=s.left+main_w+6; w=s.width-main_w-6
    s.rect(x,s.top+6,w,64,"normal")
    s.slot(x+4,s.top+27,w-8)
    note_y=s.top+80
    s.rect(x,note_y,w,s.bottom-note_y-6,"normal")
    for n in range(1,8):
        y=note_y+n*(s.bottom-note_y-6)/8
        s.line(x+4,y,x+w-4,y,"light")
    s.slot(x+4,note_y+19,w-8)
    s.circle(s.left+main_w-16,s.top+39,10,"light")
    s.line(s.left+main_w-7,s.top+33,x,s.top+23,"light")


BUILDERS={
    "storyboard-eight-mixed":storyboard_eight_mixed,
    "main-sketch-side-notes":main_sketch_side_notes,
    "detail-sketch":detail_sketch,
}
