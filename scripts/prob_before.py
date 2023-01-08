import numpy as np
from matplotlib import pyplot as plt

class prob_graph:
    def __init__(self):
        # tを101個の数字に離散化
        self.t = np.arange(0.00, 1.01, 0.01)

        self.t_ = {}

        # 事前分布p(t)を作成
        self.pt = 1/len(self.t)

        # 離散化した値ごとに確率を格納        
        for i in self.t:
            self.t_[str(round(i, 2))] = self.pt

        # plot用       
        self.fig = plt.figure(figsize=(6, 4))
        self.draw_count = 1

        # 事前分布p(t)を描画
        self.plot()

        # debug
        # for i in range(5):
        #     self.plot()
        
        # self.draw_graph()

    def plot(self):
        self.ax = self.fig.add_subplot(2, 3, self.draw_count)
        plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
        self.draw_count += 1

        x = self.t
        y = []

        for i in self.t_.values():
            y.append(i)

        plt.plot(x, y)
        plt.ylim(0, 0.08)

    def draw_graph(self):
        plt.show()

if __name__ == "__main__":
    node = prob_graph()
    node.draw_graph()
