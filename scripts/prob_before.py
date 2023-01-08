import numpy as np
from matplotlib import pyplot as plt

# 改良前の成否
SUCCESS = [True, False, False, True, True]

class prob_graph:
    def __init__(self):
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
        self.fig = plt.figure(figsize=(6, 4))
        self.draw_count = 1

        # 事前分布p(t)を描画
        self.plot()

    def plot(self):
        self.ax = self.fig.add_subplot(2, 3, self.draw_count)
        plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
        self.draw_count += 1

        y = []

        for i in self.pt_.values():
            y.append(i)

        plt.plot(self.t, y)
        plt.ylim(0, 0.08)

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

            # print(self.pta_)

        self.pt_ = self.pta_.copy()
        self.plot()

if __name__ == "__main__":
    node = prob_graph()

    for i in range(5):
        node.foward(SUCCESS[i])

    node.draw_graph()
