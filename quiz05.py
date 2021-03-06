#######################################
# datetimeモジュールの使い方
#######################################

from datetime import date

# date型の値dが与えられたときに、その日の曜日を整数（月曜：0〜日曜：7）で返す関数f1を実装せよ
# 例：f1(date(2017,2,23)) => 4

# 以下を書きかえる
def f1(d):
    return
# ここまでを書きかえる

# date型の値dが与えられたときに、2000年1月1日からその日までの日数を整数で返す関数f2を実装せよ
# 例：
#   f2(date(2000,1,3)) =>2
#   f2(date(2017,6,23)) => 6383

# 以下を書きかえる
def f2(d):
    return
# ここまでを書きかえる

assert f1(date(2000,1,1)) == 5
assert f1(date(1900,1,1)) == 0

assert f2(date(2000,1,5)) == 4
assert f2(date(2100,1,1)) == 36525
