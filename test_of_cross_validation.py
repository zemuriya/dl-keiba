# -*- coding: utf-8 -*-
##上記がないと日本語のコメントがエラーになる http://linux.oboe-gaki.com/archives/000379.html
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import sklearn

from sklearn import svm
from sklearn import cross_validation

from sklearn.grid_search import GridSearchCV
## http://d.hatena.ne.jp/teramonagi/20130825/1377434479
# X座標を適当にサンプリングして指定、それに合わせてy = sin(x) + noiseを生成
np.random.seed(1)
x = np.sort(np.random.uniform(-np.pi, np.pi,100))
y = np.sin(x) + 0.1*np.random.normal(size=len(x))
# scikit-learnに突っ込むためにフォーマット変更
x = x.reshape((len(x),1))
# 全データの描画
plt.plot(x, y, 'o')
plt.show()

#データを6割をトレーニング、4割をテスト用とする
x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.4)
# 線でつないでplotする用にx_test・y_testをx_testの昇順に並び替える
index = x_test.argsort(0).reshape(len(x_test))
x_test = x_test[index]
y_test = y_test[index]
# サポートベクトル回帰を学習データ使って作成
reg = svm.SVR(kernel='rbf', C=1).fit(x_train, y_train)
# テストデータに対する予測結果のPLOT
plt.plot(x_test, y_test, 'bo-', x_test, reg.predict(x_test), 'ro-')
plt.show()
# 決定係数R^2
print reg.score(x_test, y_test)

# 5-foldクロスバリデーション。デフォルトはr^2がスコアとなって返ってくる。すなわち以下と等価
# cross_validation.cross_val_score(svm.SVR(), x, y, cv=5, scoring="r2")
scores = cross_validation.cross_val_score(svm.SVR(), x, y, cv=5)
# 5-foldクロスバリデーション毎のR^2の平均値とその±2σレンジ
print("R^2(not adjusted): %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
#平均二乗誤差(MSE)をスコアに変更
scores = cross_validation.cross_val_score(svm.SVR(), x, y, cv=5, scoring="mean_squared_error")
# 5-foldクロスバリデーション毎のMSEの平均値とその±2σレンジ
print("MSE: %0.2f (+/- %0.2f)" % (-scores.mean(), scores.std() * 2))

#RBFカーネルのパラメーターγと罰則Cを複数個作ってその中で(スコアの意味で）良い物を探索(カーネルもパラメーターとして使用可能)
tuned_parameters = [{'kernel': ['rbf'], 'gamma': [10**i for i in range(-4,0)], 'C': [10**i for i in range(1,4)]}]
gscv = GridSearchCV(svm.SVR(), tuned_parameters, cv=5, scoring="mean_squared_error")
gscv.fit(x_train, y_train)
#一番スコア悪い&良い奴を出す
params_min,_,_ = gscv.grid_scores_[np.argmin([x[1] for x in gscv.grid_scores_])]
reg_min = svm.SVR(kernel=params_min['kernel'], C=params_min['C'], gamma=params_min['gamma'])
reg_max = gscv.best_estimator_
#全トレーニングデータを使って再推計
reg_min.fit(x_train, y_train)
reg_min.fit(x_train, y_train)
#正答(青)＆良い(赤)＆悪い(緑)の結果をPLOT
plt.plot(x_test, y_test, 'bo-',x_test, reg_max.predict(x_test), 'ro-',x_test, reg_min.predict(x_test), 'go-')
plt.show()