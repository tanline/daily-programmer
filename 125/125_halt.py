#!/usr/bin/env python
import random
import sys
import linecache

# Global Variables
instr_ran = 0 # the number of instructions executed
ip = 0 # the instruction pointer
mem = [0] * 32 # processor registers
halt = 0 

def exec_instr(instr):
    global instr_ran, halt, ip, mem
    
    op_code = instr[0]

    if len(instr) == 1:
        # instruction is probably halt
        if op_code == "HALT":
            halt = 1
            return
    elif len(instr) == 2:
        a = int(instr[1])
        if op_code == "NOT":
            mem[a] = ~mem[a]
        elif op_code == "RANDOM":
            mem[a] = random.randint(0,1)
        elif op_code == "JMP":
            ip = a
    else: 
        a = int(instr[1])
        b = int(instr[2])
        if op_code == "AND":
            mem[a] = mem[a] & mem[b]
        elif op_code == "OR":
            mem[a] = mem[a] | mem[b]
        elif op_code == "XOR":
            mem[a] = mem[a] ^ mem[b]
        elif  op_code == "MOV":
            mem[a] = mem[b]
        elif  op_code == "SET":
            mem[a] = b
        elif op_code == "JZ":
            if mem[b] == 0:
                ip = a
    
    instr_ran += 1
    ip += 1

def main():
    global instr_ran, ip, halt
    fileloc = sys.argv[1]
    total_instr = int(linecache.getline(fileloc, 1))
    ip += 1
    while (halt == 0 and instr_ran < 100000 and ip <= total_instr): 
        instr = linecache.getline(fileloc, ip+1).split()
        exec_instr(instr)

    if halt == 1:
        print "Program Halts! " + str(instr_ran) + " instructions executed."
    else:
        print "Unable to determine if application halts."

if __name__ == "__main__":
    main()
