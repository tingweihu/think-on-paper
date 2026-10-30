from __future__ import annotations

from ..geometry import Scene


def question_answer_triples(s: Scene, p: dict):
    gap=9; band=(s.height-2*gap)/3
    cue_w=30
    for i in range(3):
        y=s.top+i*(band+gap)
        s.rect(s.left,y,cue_w,band,"normal")
        s.slot(s.left+3,y+17,cue_w-6)
        s.rect(s.left+cue_w+5,y,s.width-cue_w-5,band,"normal")
        for j in range(1,4):
            yy=y+band*j/4
            s.line(s.left+cue_w+9,yy,s.right-4,yy,"light")
        s.slot(s.left+cue_w+9,y+17,s.width-cue_w-13)


def concept_text_diagram(s: Scene, p: dict):
    s.rect(s.left,s.top,s.width,29,"strong")
    s.slot(s.left+5,s.top+18,s.width-10)
    y=s.top+38; h=s.bottom-y
    text_w=s.width*0.53
    s.rect(s.left,y,text_w,h,"normal")
    s.slot(s.left+5,y+20,text_w-10)
    for n in range(1,int(h/8)):
        yy=y+n*8
        s.line(s.left+5,yy,s.left+text_w-5,yy,"light")
    s.rect(s.left+text_w+6,y,s.width-text_w-6,h,"normal")
    s.slot(s.left+text_w+10,y+20,s.width-text_w-14)


def outline_notes(s: Scene, p: dict):
    y=s.top+13
    for group in range(3):
        for level in range(3):
            x=s.left+5+level*10
            length=s.width-12-level*15
            yy=y+group*54+level*16
            s.circle(x+2,yy-1,1.6,"light")
            s.line(x+7,yy,x+length,yy,"normal" if level==0 else "light")
            s.slot(x+9,yy-1,length-10)


def concept_recall(s: Scene, p: dict):
    s.rect(s.left,s.top,s.width,32,"strong")
    s.slot(s.left+5,s.top+19,s.width-10)
    main_top=s.top+41; recall_top=s.bottom-43
    for y in range(int(main_top)+7,int(recall_top)-2,8):
        s.line(s.left+3,y,s.right-3,y,"light")
    s.slot(s.left+5,main_top+14,s.width-10)
    s.line(s.left,recall_top,s.right,recall_top,"strong")
    s.rect(s.left,recall_top+7,s.width,35,"normal")
    s.slot(s.left+5,recall_top+25,s.width-10)


BUILDERS={
    "question-answer-triples":question_answer_triples,
    "concept-text-diagram":concept_text_diagram,
    "outline-notes":outline_notes,
    "concept-recall":concept_recall,
}
