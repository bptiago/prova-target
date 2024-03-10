'''
Supondo uma sala A, B e C. Supondo interruptores 1, 2, 3.
1) Ligue os interruptores 1 e 2
2) Va até a sala A

Caso a luz não esteja acesa:
    O interruptor 3 é da sala A
    3) Desligue os interruptores e ligue somente o interruptor 1
    4) Vá até a sala B
    5) Se a luz está ligada, então: A - 3, B - 1 e C - 2
    6) Se a luz não está ligada, então: A - 3, B - 2, C - 1

Caso a luz esteja acesa:
    A sala A pode ser o interruptor 1 ou 2
    3) Vá até a sala B.
    Se a luz estiver acesa:
        Interruptor 3 é da sala C
        Interruptor 1 e 2 pode ser da sala A ou B
    Se a luz não estiver acesa:
        Interruptor 3 é da sala B
        Interruptor 1 e 2 pode ser da sala A ou C
'''