#!/usr/bin/env python3
"""
    turtle-example-suite:
    
    xtx_lindenmayer_indian.py

Situation:
    Each morning women in Tamil Nadu, in southern
    India, place designs, created by using rice
    flour and known as kolam on the thresholds of
    their homes.

Task:
    These can be described by Lindenmayer systems,
    which can easily be implemented with turtle 
    graphics and Python.

Action:
    Two designs:
    (1) the snake kolam
    (2) anklets of krishna

Result:
    Taken from Marcia Ascher: Methematics
    Elsewhere, An Exploration of Ideas Across
    cultures
"""
#####################################
#####   Mini Lindenmayer tool  ######
#####################################

from turtle import *

def replace( seq, replacementsRules, n):
    for i in range(n):
        newseq =""
        for element in seq:
            newseq = newseq + replacementRules.get(element,element)
        seq = newseq 
    return seq 

def draw( commands, rules) 
    for b in commands:
        try: 
            rules[b]()
        except TypeError: 
            try: 
                draw(rules[b], rules)
            except:
                pass 

def main():
    ############################
    ## Design 1: snake kolam ###
    ############################

    def r():
        right(45)
    def l():
        left(45)
    def f():
        forward(7.5)

    snake_rules = {"-":r, "+":l, "f":f, "b":"f+f+f--f--f+f+f"}
    snake_replacementsRules = {"b": "b+f+b--f--b+f+b"}
    snake_start = "b--f--b--f"

    drawing = replace(snake_start, snake_repelecementRules, 3) 

    reset()
    speed(3)
    tracer(1,0)
    ht()
    backward(195) 
    down()
    draw(drawing, snake_rules)

    from time import sleep 
    sleep(3)

    ###################################
    ### Design 2: Anklets ofkrishna ###
    ################################### 

    def A():
        color("red")
        circle(10,90)

    def B(): 
        from math import sqrt 
        color("black")
        l = 5/sqrt(2)
        forward(l) 
        circle(l, 270)
        forward(l)

    def F():
        color("green")
        forward(10)
    
    krishna_rules = {"a":A, "b":B, "f":F}
    krishna_replacementRules = {"a" : "afbfa", "b" : "afbfbfbfa"}
    krishna_start = "fbfbfbfb"
   
    reset()
    speed(0)
    tracer(3,0)
    ht()
    left(45)
    drawing = replace(krishna_start, krishna_replacementRules,3) 
    draw(drawing, krishna_rules)
    tracer(1) 
    return "Done!"

if __name__ == '__main__':
    msg = main() 
    print(msg) 
    mainloop()





