# 要件定義
random()：CMリストの並び替えを行う関数。
CMをいくつかの群に分けた時、同じ群の数字が連続で流れることがないようにする。
EX)A群[1,2,3,]B群[4,5,6]C群[7,8,9,10]の時、
1,2,5,8....だと1.2は連続してはいけないのでNG(この場合、連群と呼ぶ)
また、規則性をなくすために、A群、B群,C群,A群,B群,C群....のような選び方はしない。

# アルゴリズム内容
アルゴリズムの内容として、大きく二つに分類できます。
1. 重みつけ配列取得
2. 連群を防ぐために、前に取得した数字の群を記録する

EX)
A群、B群,C群がある時、重みつけ配列取得によって各群の長さを3,3,4とするとC群から数字が選ばれる確率を高く設定する。
ans_listという配列に答えとなる数字の並び(CMの並び)が記録されるが、ans_listの最後の要素が含まれる群をpre_picked_listとして記録しておき、ans_listに数字を入れる時、pre_picked_listに含まれないかチェックする。
