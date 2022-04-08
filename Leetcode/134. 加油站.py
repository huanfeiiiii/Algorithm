# _*_ coding:utf-8 _*_

gas = [2]

cost = [2]
if len(gas) == 1:
    if gas[0] - cost[0] >= 0:

status = -1
for i in range(len(gas)):
    if gas[i] > cost[i]:
        line = [j for j in range(i, len(gas))] + [k for k in range(i)]
        total_gas = 0
        for k in line:
            total_gas += gas[k] - cost[k]
            print(i, k, gas[k] - cost[k], total_gas)
            if total_gas < 0:
                break
        if total_gas >= 0:
            status = i
            break
print(status)
