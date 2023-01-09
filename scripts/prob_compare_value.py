import numpy as np
from matplotlib import pyplot as plt
import math

# 改良前の成否
SUCCESS_b = [True, False, False, True, True]
# 改良後の成否
SUCCESS_a = [True, True, True, True, True]

class prob_graph:
    def __init__(self, init_fig = True):
        # tを101個の数字に離散化
        self.t = np.arange(0.00, 1.01, 0.01)

        self.pt_ = {}
        self.pat_ = {}
        self.pta_ = {}

        # 事前分布p(t)を作成
        self.pt = 1/len(self.t)

        # 離散化した値ごとに確率を格納        
        for i in self.t:
            self.pt_[str(round(i, 2))] = self.pt

        # plot用       
        if init_fig:
            self.fig = plt.figure(figsize=(10, 3))
            self.draw_count = 1

    def plot(self):
        self.ax = self.fig.add_subplot(1, 3, self.draw_count)
        
        plt.subplots_adjust(wspace = 0.7, bottom = 0.2)
        
        y = []

        for i in self.pt_.values():
            y.append(i)

        exec("self.store{} = self.pt_.copy()".format(self.draw_count))
        self.draw_count += 1

        plt.plot(self.t, y)

        plt.ylim(0, 0.08)
        plt.ylabel("probability")
        plt.xlabel("t")
        self.ax.grid(which = "major", axis = "x", color = "gray", alpha = 0.8, linestyle = "-", linewidth = 1)
        self.ax.grid(which = "major", axis = "y", color = "gray", alpha = 0.8, linestyle = "-", linewidth = 1)
        # self.ax.spines['left'].set_position(('data', 0))
        # self.ax.spines['right'].set_position(('data', 1.0))

    def plots(self):
        self.ax = self.fig.add_subplot(1, 3, self.draw_count)
        
        plt.subplots_adjust(wspace = 0.7, bottom = 0.2)
        
        self.ax.plot(self.t, self.store1)
        self.ax.plot(self.t, self.store2)

        plt.ylim(0, 0.08)
        plt.ylabel("probability")
        plt.xlabel("t")
        self.ax.grid(which = "major", axis = "x", color = "gray", alpha = 0.8, linestyle = "-", linewidth = 1)
        self.ax.grid(which = "major", axis = "y", color = "gray", alpha = 0.8, linestyle = "-", linewidth = 1)
        self.ax.spines['left'].set_position(('data', 0))
        self.ax.spines['right'].set_position(('data', 1.0))

    def draw_graph(self):
        plt.show()

    def foward(self, success):
        if success:
            # 完走の場合
            for i in self.t:
                self.pat_[str(round(i, 2))] = round(i, 2)
        else:
            # 失敗の場合
            for i in self.t:
                self.pat_[str(round(i, 2))] = round(1 - i, 2)
        
        # 更新
        for i in self.t:
            key = str(round(i, 2))
            self.pta_[key] = self.pat_[key] * self.pt_[key]

        # 正規化定数の計算
        eta = sum(self.pta_.values())

        # p(t|a)の積分が1になるように正規化
        for i in self.t:
            key = str(round(i, 2))
            self.pta_[key] = (self.pat_[key] * self.pt_[key]) / eta

        self.pt_ = self.pta_.copy()

if __name__ == "__main__":
    node = prob_graph()

    for i in range(5):
        node.foward(SUCCESS_b[i])
    node.plot()
    
    node.__init__(False)

    for i in range(5):
        node.foward(SUCCESS_a[i])
    node.plot()

    error = {}

    n = np.arange(0.60, 0.80, 0.01)

    for i in n:
        key = str(round(i, 2))
        error[key] = (abs(node.store1[key] - node.store2[key]))
    
    min_v = min(error.values())

    key = [k for k, v in error.items() if v == min_v]

    print(key)

    avg1 = sum(node.store1.values()) / len(node.t)
    print(avg1)

    avg2 = sum(node.store2.values()) / len(node.t)
    print(avg2)

    sigma1 = []

    for i in node.store1.values():
        sigma1.append((i-avg1)**2)

    print(sum(sigma1)/101)
    print(math.sqrt(sum(sigma1)/101))

    e = []
    for i in node.t:
        e.append(node.store1[str(round(i, 2))] * i)

    print("改良前の期待値：" + str(sum(e)))

    e = []
    for i in node.t:
        e.append(node.store2[str(round(i, 2))] * i)

    print("改良後の期待値：" + str(sum(e)))

    # print(error)

    # [error.remove(0) for i in error]
    
    # key = str(node.store1[error.index(min(error))])
    # print(node.pt_[key])
