# ProbRobotics_task
確率ロボティクス 課題

## 作成したプログラム
- [prob_before.py](https://github.com/masakifujiwara1/ProbRobotics_task/blob/dev/scripts/prob_before.py)
 （改良前の試行による成否で更新するごとのグラフを描画）
  - 出力(上段左：事前分布, 上段中央から順に1回から5回までの試行を反映した分布) <br>
![Figure_b](https://user-images.githubusercontent.com/72371743/211248125-49ccd2f6-42f7-4676-8ffb-805b6f5abcf1.png)
- [prob_after.py](https://github.com/masakifujiwara1/ProbRobotics_task/blob/dev/scripts/prob_after.py)
 （改良後の試行による成否で更新するごとのグラフを描画）
   - 出力(上段左：事前分布, 上段中央から順に1回から5回までの試行を反映した分布) <br>
 ![Figure_a](https://user-images.githubusercontent.com/72371743/211248381-a829ec29-b64a-4870-b4bb-1cf4b8ebc293.png)
- [prob_compare.py](https://github.com/masakifujiwara1/ProbRobotics_task/blob/dev/scripts/prob_compare.py)
 （改良前後の5回の試行を反映したグラフを重ねて描画）
  - 出力(左：改良前, 中央：改良後, 右：改良前後のグラフを重ねて描画) <br>
![Figure_c](https://user-images.githubusercontent.com/72371743/211248828-24b998b2-869e-452b-ab6e-b1b8cab4a225.png)

## プログラムの説明（prob_compare.py）
共通部分が多いため, prob_compare.pyのみ説明します.
***
![Screenshot from 2023-01-09 17-00-33](https://user-images.githubusercontent.com/72371743/211262858-7e3e0bd6-0854-44e0-8bbb-a9d180c0b5bf.png)
1,2行目では, 必要なモジュールを読み込みます. 
<br>5,6行目では, 改良前後の試行結果をbool型でリストに格納します.
***
![Screenshot from 2023-01-09 17-04-19](https://user-images.githubusercontent.com/72371743/211263386-74793f94-50a5-46e6-81c5-ceebdc25f1f1.png)
prob_graphというクラスを作成します. 
<br> 12行目では, 完走率であるtを101個の数字に離散化しています. 

<br> 14,15,16行目では, 空のp(t), p(a|t), p(t|a)を作成しています. 辞書型なのは, 離散化した各値をキーにすることで完走率tの密度をピンポイントで抜き出せるようにするためです.

<br> 19行目では, 事前分布(一様分布)の値を求めています.
<br> 22,23行目では, 事前分布p(t)を作成しています.
***
![Screenshot from 2023-01-09 17-25-34](https://user-images.githubusercontent.com/72371743/211266250-bb7aae12-1613-4116-b4c0-675dfb9bc88c.png)
43行目では, 離散化したtの各値ごとに密度をプロットしています.
<br> 45〜51行目では, グラフを描画する際の設定をしています.
***
![Screenshot from 2023-01-09 17-59-26](https://user-images.githubusercontent.com/72371743/211271733-2fc8a95f-a0ed-415f-82c8-c323707f11a5.png)
73~80行目では, 式(1)で表されるp(a|t)を求めています. 
```math
p(a|t) = 
\left\{
 \begin{align*}
 t  （a:完走）\\
 1-t  （a:失敗）
 \end{align*}
\right.
\label{a}\tag{1}
```
