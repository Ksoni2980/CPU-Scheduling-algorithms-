import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt' , 'r')

processes = {}
n = int(input())
for _ in range(n):
    s = input().split()
    del s[-1]

    processes[s[0]] = s[1:]


process_info = {}
process_state = {}
input_seq = []
output_seq = []
cpu_seq = []

cpu_free = 100
ip_free = 100
op_free = 100
current_time = 0

cpu = []
inp = []
out = []

cpu_busy = False
ip_busy = False
op_busy = False

while True:
    for process in list(processes.items()):
        if int(process[1][0]) <= current_time:
            
            process_info[process[0]] = process[1]
            process_state[process[0]] = 2

            cpu.append( (process[0],int(list(process[1][1])[1])) )
            del processes[process[0]]



    if cpu_free == current_time:
        cpu_busy = False
        
        temp = process_info[cpu_seq[-3]]
        state = process_state[cpu_seq[-3]]
        if state < len(temp):
            if list(temp[state])[0] == 'I':
                inp.append((cpu_seq[-3],int(list(temp[state])[1])))
            else:
                out.append((cpu_seq[-3],int(list(temp[state])[1])))
            process_state[cpu_seq[-3]] += 1

    if not cpu_busy and len(cpu):
        cpu_busy = True
        cpu_seq += [cpu[0][0] , current_time , current_time + cpu[0][1]]
        cpu_free = current_time + cpu[0][1]
        del cpu[0]

    


    if ip_free == current_time:
        ip_busy = False
        
        temp = process_info[input_seq[-3]]
        state = process_state[input_seq[-3]]
        if state < len(temp):
            if list(temp[state])[0] == 'C':
                cpu.append((input_seq[-3],int(list(temp[state])[1])))
            else:
                out.append((input_seq[-3],int(list(temp[state])[1])))
            process_state[input_seq[-3]] += 1

    if not ip_busy and len(inp):
        ip_busy = True
        input_seq += [inp[0][0] , current_time , current_time + inp[0][1]]
        ip_free = current_time + inp[0][1]
        del inp[0]




    if op_free == current_time:
        op_busy = False
        
        temp = process_info[output_seq[-3]]
        state = process_state[output_seq[-3]]
        if state < len(temp):
            if list(temp[state])[0] == 'C':
                cpu.append((output_seq[-3],int(list(temp[state])[1])))
            else:
                inp.append((output_seq[-3],int(list(temp[state])[1])))
        process_state[output_seq[-3]] += 1

    if not op_busy and len(out):
        op_busy = True
        output_seq += [out[0][0] , current_time , current_time + out[0][1]]
        op_free = current_time + out[0][1]
        del out[0]




    current_time += 1
    if current_time == 50:
        break 

print("CPU Sequence is:")
for i in range(0,len(cpu_seq),3):
    print("{} - From {} to {}".format(cpu_seq[i],cpu_seq[i+1],cpu_seq[i+2]))
print("")

print("INPUT Sequence is:")
for i in range(0,len(input_seq),3):
    print("{} - From {} to {}".format(input_seq[i],input_seq[i+1],input_seq[i+2]))
print("")

print("OUTPUT Sequence is:")
for i in range(0,len(output_seq),3):
    print("{} - From {} to {}".format(output_seq[i],output_seq[i+1],output_seq[i+2]))
print("")

