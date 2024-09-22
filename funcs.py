from words import *
import random as r

def get_hostname_web(num):
    hostnames = []
    num = num+1
    for i in range(1, num):
        hostname = f"{r.choice(adjs)}-{r.choice(nouns)}"
        hostnames.append(f"{hostname}")
    return "<br>".join(hostnames)

def get_hostname(num):
    hostnames = []
    num = num+1
    for i in range(1, num):
        hostname = f"{r.choice(adjs)}-{r.choice(nouns)}"
        hostnames.append(f"{hostname}")
    return "\n".join(hostnames)