import csv
import matplotlib.pyplot as plt

cnn_tsv = open('out_cnn.tsv')

train_cost = []
train_ler = []
num_epoch = []

a = 0
for line in cnn_tsv:
    if a > 0:
        line_result = line.split(' ', 4)
        train_cost.append(float(line_result[1]))
        train_ler.append(float(line_result[2]))
        num_epoch.append(a)
    a = a + 1


figure, ax = plt.subplots()
plots_1 = ax.plot(num_epoch, train_cost, color = 'b', linewidth = 1.0, linestyle = '-' ,label = 'train_cost')
plots_2 = ax.plot(num_epoch, train_ler, color = 'r',  linewidth = 1.0, linestyle = '-' ,label = 'train_ler')
figure.set_size_inches(8, 8)
ax.legend()
ax.set_xlim(xmin=0)
ax.set_ylim(ymin=0)
ax.set_title('Result ler')
ax.set_xlabel('num epoch')
ax.set_ylabel('train ler')

ax.grid(True) # 使用格子
#figure.text(0.995, 0.01, 'zmtech CopyRight', ha='right', va='bottom')
#figure.tight_layout()
plt.show()