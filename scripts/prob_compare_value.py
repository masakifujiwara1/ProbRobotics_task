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
        self.ax.spines['left'].set_position(('data', 0))
        self.ax.spines['right'].set_position(('data', 1.0))

    def plots(self):
        self.ax = self.fig.add_subplot(1, 3, self.draw_count)
        
        plt.subplots_adjust(wspace = 0.7, bottom = 0.2)

        y = []

        for i in self.store1.values():
            y.append(i)
        
        self.ax.plot(self.t, y)


        y = []

        for i in self.store2.values():
            y.append(i)

        self.ax.plot(self.t, y)

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

    origin = 5

    sample = 5
    N = int(sample/5)

    print("サンプル数：" + str(sample))

    for j in range(N):
        for i in range(origin):
            node.foward(SUCCESS_b[i])

    node.plot()
    
    node.__init__(False)

    for j in range(N):
        for i in range(origin):
            node.foward(SUCCESS_a[i])

    node.plot()

    error = {}

    n = np.arange(0.60, 0.80, 0.01)

    for i in n:
        key = str(round(i, 2))
        error[key] = (abs(node.store1[key] - node.store2[key]))
    
    min_v = min(error.values())

    key = [k for k, v in error.items() if v == min_v]

    print("交差するtの値: 約" + str(key[0]))

    e1 = []
    sigma1 = []

    for i in node.t:
        key1 = str(round(i, 2))
        e1.append(node.store1[key1] * i)

    for i in node.t:
        key1 = str(round(i, 2))    
        sigma1.append(node.store1[key1] * (i - sum(e1))**2)
    
    max_v1 = max(node.store1.values())
    key1 = [k for k, v in node.store1.items() if v == max_v1]

    print("-" * 50)
    print("改良前のtの最頻値：" + str(key1[0]))
    print("改良前のtの期待値：" + str(round(sum(e1), 2)))
    print("改良前のtの分散：" + str(round(sum(sigma1), 2)))
    print("改良前のtの偏差：" + str(round(math.sqrt(sum(sigma1)), 2)))
    print("1シグマ範囲：" + str(round(sum(e1) - 1 * math.sqrt(sum(sigma1)), 2)) + " <= t <= " + str(round(sum(e1) + 1 * math.sqrt(sum(sigma1)), 2)))
    print("2シグマ範囲：" + str(round(sum(e1) - 2 * math.sqrt(sum(sigma1)), 2)) + " <= t <= " + str(round(sum(e1) + 2 * math.sqrt(sum(sigma1)), 2)))
    print("-" * 50)

    e2 = []
    sigma2 = []

    for i in node.t:
        key2 = str(round(i, 2))
        e2.append(node.store2[key2] * i)

    for i in node.t:
        key2 = str(round(i, 2))    
        sigma2.append(node.store2[key2] * (i - sum(e2))**2)

    max_v2 = max(node.store2.values())
    key2 = [k for k, v in node.store2.items() if v == max_v2]

    # print("-" * 50)
    print("改良後のtの最頻値：" + str(key2[0]))
    print("改良後のtの期待値：" + str(round(sum(e2), 2)))
    print("改良後のtの分散：" + str(round(sum(sigma2), 2)))
    print("改良後のtの偏差：" + str(round(math.sqrt(sum(sigma2)), 2)))
    print("1シグマ範囲：" + str(round(sum(e2) - 1 * math.sqrt(sum(sigma2)), 2)) + " <= t <= " + str(round(sum(e2) + 1 * math.sqrt(sum(sigma2)), 2)))
    print("2シグマ範囲：" + str(round(sum(e2) - 2 * math.sqrt(sum(sigma2)), 2)) + " <= t <= " + str(round(sum(e2) + 2 * math.sqrt(sum(sigma2)), 2)))

    print("-" * 50)

    # t検定
    # s_2 = ((sample - 1) * sum(sigma1) + (sample - 1) * sum(sigma2)) / (sample * 2 - 2)
    # t = abs((sum(e1) - sum(e2)) / math.sqrt(s_2 * (1 / sample + 1/sample)))

    t = (sum(e1) - sum(e2)) / math.sqrt(sum(sigma1) / 101 + sum(sigma2) / 101)
    d = (sum(sigma1) / 101 + sum(sigma2) / 101)**2 / ((sum(sigma1)**2 / (101**2 * (101 - 1))) + (sum(sigma2)**2 / (101**2 * (101 - 1))))

    print("t値：" + str(t))
    print("自由度：" + str(d))
    print(str(sum(sigma2) / sum(sigma1)))

    node.plots()
    node.draw_graph()