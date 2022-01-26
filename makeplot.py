import numpy as np
import matplotlib.pyplot as plt

#Plot for 8-puzzle
index = np.arange(5)
bar_width = 0.35

fig, ax = plt.subplots()
sol_length = [23,23,23,23,44642]
memory_usage = [0.51,0.07,0.66,36,41.77]
sol_length_bars = ax.bar(index, sol_length, bar_width,
                label="Solution length")

memory_usage_graph = ax.bar(index+bar_width, memory_usage,
                 bar_width, label="Memory Usage")

ax.set_xlabel('Search Algorithms')
ax.set_ylim([0, 50])
ax.set_title('Performances of different algorithms on 8-puzzle')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(["MLS", "MLS2", "A*", "BFS", "DFS"])
ax.legend()

fig2, bx = plt.subplots()
expanded_nodes = [508,122,1133,91203,66496]
stored_nodes = [653,177,1735,106922,96796]

expanded_nodes_bars = bx.bar(index, expanded_nodes, bar_width,
                label="Expanded Nodes")

stored_nodes_graph = bx.bar(index+bar_width, stored_nodes,
                 bar_width, label="Stored Nodes")

bx.set_yscale('log')
bx.set_xlabel('Search Algorithms')
bx.set_title('Stored / Expanded Nodes on 8-puzzle')
bx.set_xticks(index + bar_width / 2)
bx.set_xticklabels(["MLS", "MLS2", "A*", "BFS", "DFS"])
bx.legend()

index = np.arange(3)
bar_width = 0.35

fig3, cx = plt.subplots()
sol_length = [32,33,33]
memory_usage = [23,90,7.6]
sol_length_bars = cx.bar(index, sol_length, bar_width,
                label="Solution length")

memory_usage_graph = cx.bar(index+bar_width, memory_usage,
                 bar_width, label="Memory Usage")

cx.set_xlabel('Search Algorithms')
cx.set_title('Performances of different algorithms on 15-puzzle')
cx.set_xticks(index + bar_width / 2)
cx.set_xticklabels([ "A*","MLS", "MLS2"])
cx.legend()

fig4, dx = plt.subplots()
expanded_nodes = [24751,246831,7632]
stored_nodes = [47891,473891,15798]

expanded_nodes_bars = dx.bar(index, expanded_nodes, bar_width,
                label="Expanded Nodes")

stored_nodes_graph = dx.bar(index+bar_width, stored_nodes,
                 bar_width, label="Stored Nodes")

dx.set_yscale('log')
dx.set_xlabel('Search Algorithms')
dx.set_title('Stored / Expanded Nodes on 15-puzzle')
dx.set_xticks(index + bar_width / 2)
dx.set_xticklabels([ "A*","MLS", "MLS2"])
dx.legend()

plt.show()