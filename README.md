# ProbRobotics_task
確率ロボティクス 課題

## 作成したプログラム
- [prob_before.py](https://github.com/masakifujiwara1/ProbRobotics_task/blob/dev/scripts/prob_before.py)
 （改良前）
  - 出力(上段左：事前分布, 上段中央から順に1回から5回までの試行を反映した分布) <br>
![Figure_b](https://user-images.githubusercontent.com/72371743/211248125-49ccd2f6-42f7-4676-8ffb-805b6f5abcf1.png)
- [prob_after.py](https://github.com/masakifujiwara1/ProbRobotics_task/blob/dev/scripts/prob_after.py)
 （改良後）
   - 出力(上段左：事前分布, 上段中央から順に1回から5回までの試行を反映した分布) <br>
 ![Figure_a](https://user-images.githubusercontent.com/72371743/211248381-a829ec29-b64a-4870-b4bb-1cf4b8ebc293.png)
- [prob_compare.py](https://github.com/masakifujiwara1/ProbRobotics_task/blob/dev/scripts/prob_compare.py)
 （改良前後を比較）
  - 出力(左：改良前, 中央：改良後, 右：改良前後のグラフを重ねて描画) <br>
![Figure_c](https://user-images.githubusercontent.com/72371743/211248828-24b998b2-869e-452b-ab6e-b1b8cab4a225.png)

## プログラムの説明（prob_compare.py）
共通部分が多いため, prob_compare.pyのみ説明します.
***
![Screenshot from 2023-01-09 17-00-33](https://user-images.githubusercontent.com/72371743/211262858-7e3e0bd6-0854-44e0-8bbb-a9d180c0b5bf.png)
<br>1,2行目では, 必要なモジュールを読み込みます. 
<br>5,6行目では, 改良前後の試行結果をbool型でリストに格納します.
***
![Screenshot from 2023-01-09 17-04-19](https://user-images.githubusercontent.com/72371743/211263386-74793f94-50a5-46e6-81c5-ceebdc25f1f1.png)
<br>prob_graphというクラスを作成します. 
<br> 12行目では, 完走率である $t$ を $t = 0.00,0.01,0.02,...,1.00$ と101個の数字に離散化しています. 

<br> 14,15,16行目では, 空の $p(t), p(a|t), p(t|a)$ を作成しています. 辞書型なのは, 離散化した各値をキーにすることで完走率tの密度をピンポイントで抜き出せるようにするためです.

<br> 19行目では, 事前分布(一様分布)の値を求めています.
<br> 22,23行目では, 事前分布 $p(t)$ を作成しています.
***
![Screenshot from 2023-01-09 17-25-34](https://user-images.githubusercontent.com/72371743/211266250-bb7aae12-1613-4116-b4c0-675dfb9bc88c.png)
<br>43行目では, 離散化したtの各値ごとに密度をプロットしています.
<br> 45~51行目では, グラフを描画する際の設定をしています.
***
![Screenshot from 2023-01-09 17-59-26](https://user-images.githubusercontent.com/72371743/211271733-2fc8a95f-a0ed-415f-82c8-c323707f11a5.png)
<br>このfoward関数では, 試行結果の反映を行います. 引数は初めに定義した試行結果です.
<br><br>

73~80行目では, 式(1)で表される $p(a|t)$ を求めています. 
```math
p(a|t) = 
\left\{
 \begin{align*}
 t  （a:完走）\\
 1-t  （a:失敗）
 \end{align*}
\right.
\tag{1}
```
<br><br>

83~85行目では, 式(2)で表される正規化前の $p(t|a)$ である $p(t|a)^*$ を求めています.
```math
p(t|a)^* = p(a|t)p(t)
\tag{2}
```
<br><br>

88行目では, 定数とみなすことのできる $p(a)$ を求めます.
```math
p(t|a) = \frac{p(a|t)p(t)}{p(a)}
\tag{3}
```
$p(a)$を求めるには, 式(3)から $p(t|a)$ を積分をすると
```math
p(t|a) = \frac{1}{p(a)} \int p(a|t)p(t)dt \approx \frac{1}{p(a)}\sum_{t=0.00}^{1.00}p(a|t)p(t)
\tag{4}
```
となり, $p(t|a)$ の積分が1だと仮定すると
```math
p(a) = \sum_{t=0.00}^{1.00}p(a|t)p(t)
\tag{5}
```
と式変形できます. 式(2)と式(5)から, 
```math
p(a) = \sum_{t=0.00}^{1.00}p(t|a)^*
\tag{6}
```
となります. 
<br> よって, 88行目では, 式(6)から $p(a)$を求めています.
<br><br>

91~93行目では, 求めた $p(a)$ を用いて式(3)から $p(t|a)$ を求めています.
<br><br>

95行目では, 式(7)のように, 2回目以降の試行結果を繰り返し代入して計算できるように代入しています.
```math
p(t|a_{1:i+1}) = \eta p(a_{i+1}|t)p(t|a_{1:i})
\tag{7}
```
***
![Screenshot from 2023-01-09 20-10-03](https://user-images.githubusercontent.com/72371743/211297024-24a0fb88-0e25-487d-8fb3-560e30e939f0.png)
<br>100~101行目では, 改良前の試行結果を1回ごとに反映しています.
<br>106\~107行目では, 改良後の試行結果を1回ごとに反映しています.
<br>112行目では, グラフの描画を行っています.

## 計算から帰結されること
### 5回試行した場合
![Figure_c](https://user-images.githubusercontent.com/72371743/211248828-24b998b2-869e-452b-ab6e-b1b8cab4a225.png)
求めた改良前後のtの確率分布より, tの期待値, 分散, 偏差が分かる.
|    |  最頻値  |  期待値  |  分散  |  偏差  |
| ---- | :----: | :----: | ---- | ---- |
|  改良前  |  0.60  |  0.57  |  0.03  |  0.17  |
|  改良後  |  1.00  |  0.86  |  0.02  |  0.12  |
<br>

また, 期待値と偏差より, $\sigma$ 範囲が分かる.
|    |  1 $\sigma$ 範囲  |  2 $\sigma$ 範囲  |
| ---- | ---- | ---- |
|  改良前  | 0.4 $\leq t \leq$ 0.75  |  0.22 $\leq t \leq$ 0.92  |
|  改良後  | 0.74 $\leq t \leq$ 0.99  |  0.61 $\leq t \leq$ 1.00  |
<br>

2 $\sigma$ 範囲より, 約95％の確率で改良前は 0.22 $\leq t \leq$ 0.92 に収まり, 改良後は 0.61 $\leq t \leq$ 1.00 に収まることが分かる.
期待値を比較すると, 改良前より改良後の方が約0.3ほど高い. そのため, 改良後の方が完走する可能性が高いといえる.
<br> しかし, 上のグラフのように重なる面積が非常に大きいため, 試行を重ねるとtの期待値が逆転する可能性がある. また, 求めた偏差は1回の試行により全体の値が大きく変化してしまうおそれがあることを示している.
<br> 
### 試行が5回より多い場合
5回の試行で観測された試行結果を単に複数回繰り返す操作を行い, グラフがどのように変化するか確認する.
10, 15, 20まで確認を行った.
#### 10回
![Figure_10](https://user-images.githubusercontent.com/72371743/211726327-239e6f31-bcc2-458c-be4f-48adfaf66061.png)
赤紫(magenta)色の垂直線：改良前の1 $\sigma$ 範囲の大きい方の境界線
<br> 濃紺(navy)色の垂直線：改良前の2 $\sigma$ 範囲の大きい方の境界線
<br> <br>
改良前の期待値が0.58 $\pm$ 0.14, 改良後の期待値が0.92 $\pm$ 0.08となり, 試行回数が5回の時と比較すると偏差は落ち着いて来たが, まだ1回の試行により全体の値に影響を及ぼすおそれがあることを示している. また, 未だに大部分で重なりが起きているため, 10回では試行回数が十分だとは言い難い.
#### 15回
![Figure_15](https://user-images.githubusercontent.com/72371743/211729306-25b270f6-7878-495c-90f8-5ddc693f80df.png)
赤紫(magenta)色の垂直線：改良前の1 $\sigma$ 範囲の大きい方の境界線
<br> 濃紺(navy)色の垂直線：改良前の2 $\sigma$ 範囲の大きい方の境界線
<br> <br>
改良前の期待値が0.59 $\pm$ 0.12, 改良後の期待値が0.95 $\pm$ 0.06となった. 改良前の1 $\sigma$ 範囲の大きい方の境界線を表す赤紫色の垂直線（t = 0.70）に注目すると, t = 0.70の時, 改良後の値は0.00070となり, 減衰しきっているといえる. このことから, 約16％（1 $\sigma$ 範囲：約68％であり, 片側のみ重なりが起きているため）の確率で, 改良前の群は改良後の群と重なるtの値を取りうるといえる. 15回の試行回数が適切かどうかは後述する.
#### 20回
![Figure20](https://user-images.githubusercontent.com/72371743/211733238-d5d2517b-01ef-4a1f-b2e2-1e3116d31bac.png)
赤紫(magenta)色の垂直線：改良前の1 $\sigma$ 範囲の大きい方の境界線
<br> 濃紺(navy)色の垂直線：改良前の2 $\sigma$ 範囲の大きい方の境界線
<br> <br>
改良前の期待値が0.59 $\pm$ 0.1, 改良後の期待値が0.96 $\pm$ 0.04となった. 改良前の2 $\sigma$ 範囲の大きい方の境界線を表す濃紺色の垂直線（t = 0.80）に注目すると, t = 0.80の時, 改良後の値は0.0022となり, ほぼ減衰しきっている見なせる. このことから, 約2.5％（2 $\sigma$ 範囲：約95％であり, 片側のみ重なりが起きているため）の確率で, 改良前の群は改良後の群と重なるtの値を取りうるといえる. この場合, 改良前と改良後のtの値が逆転する可能性が少ないと考えられる.
<br> <br>
15回と20回の間で, 改良前の群は改良後の群と重なるtの値を取りうる確率が, 約2.5％\~16％まで変化するため, 約5％になるような試行回数が最低試行回数に近いおそれがある.
そのため, 改良後の有効性を検証するために十分な試行回数は, 15回~20回の間に存在すると考えられる.

## 動作確認
- OS: Ubuntu 20.04 LTS
- Python: 3.8.10
- Numpy: 1.23.2
- Matplotlib: 3.1.2

## LICENSE
[MIT](https://github.com/masakifujiwara1/ProbRobotics_task/blob/dev/LICENSE)
