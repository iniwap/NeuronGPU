import neuralgpu as ngpu

neuron = ngpu.CreateNeuron("aeif_cond_beta", 1, 1)
poiss_gen = ngpu.CreatePoissonGenerator(1, 12000.0);

conn_dict={"rule": "one_to_one"}
syn_dict={"weight": 0.05, "delay": 2.0, "receptor":0}

ngpu.Connect(poiss_gen, neuron, conn_dict, syn_dict)
record = ngpu.CreateRecord("", ["V_m"], [neuron[0]], [0])

ngpu.Simulate()

data_list = ngpu.GetRecordData(record)
t=[row[0] for row in data_list]
V_m=[row[1] for row in data_list]

import matplotlib.pyplot as plt

plt.figure(1)
plt.plot(t, V_m)

plt.draw()
plt.pause(1)
raw_input("<Hit Enter To Close>")
plt.close()