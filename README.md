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
1,2行目では, 必要なモジュールを読み込みます. 
<br>5,6行目では, 改良前後の試行結果をbool型でリストに格納します.
***
![Screenshot from 2023-01-09 17-04-19](https://user-images.githubusercontent.com/72371743/211263386-74793f94-50a5-46e6-81c5-ceebdc25f1f1.png)
prob_graphというクラスを作成します. 
<br> 12行目では, 完走率である $t$ を $t = 0.00,0.01,0.02,...,1.00$ と101個の数字に離散化しています. 

<br> 14,15,16行目では, 空の $p(t), p(a|t), p(t|a)$ を作成しています. 辞書型なのは, 離散化した各値をキーにすることで完走率tの密度をピンポイントで抜き出せるようにするためです.

<br> 19行目では, 事前分布(一様分布)の値を求めています.
<br> 22,23行目では, 事前分布 $p(t)$ を作成しています.
***
![Screenshot from 2023-01-09 17-25-34](https://user-images.githubusercontent.com/72371743/211266250-bb7aae12-1613-4116-b4c0-675dfb9bc88c.png)
43行目では, 離散化したtの各値ごとに密度をプロットしています.
<br> 45~51行目では, グラフを描画する際の設定をしています.
***
![Screenshot from 2023-01-09 17-59-26](https://user-images.githubusercontent.com/72371743/211271733-2fc8a95f-a0ed-415f-82c8-c323707f11a5.png)
このfoward関数では, 試行結果の反映を行います. 引数は初めに定義した試行結果です.

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

83~85行目では, 式(2)で表される正規化前の $p(t|a)^*$ を求めています.
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

95行目では, 式(7)のように2回目以降の試行結果を繰り返し代入して計算できるように, 求めた $p(t|a)$ を $p(t)$ に代入しています.
```math
p(t|a_{1:i+1}) = \eta p(a_{i+1}|t)p(t|a_{1:i})
\tag{7}
```
***
