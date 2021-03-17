# Django_web

[![Build Status](https://travis-ci.org/ChiangChienWei/pwb.svg?branch=demo)](https://travis-ci.org/ChiangChienWei/pwb)
[![codecov](https://codecov.io/gh/ChiangChienWei/pwb/branch/demo/graph/badge.svg?token=5T5UF00CWA)](https://codecov.io/gh/ChiangChienWei/pwb)

首先請先下載 [Anaconda](https://www.anaconda.com/products/individual#macos)

1. Clone Django_web repository
  ```bash
  $ git clone git@github.com:ChiangChienWei/pwb.git

  (若此步驟有問題，請確認您的 GitHub 帳戶中有新增 SSH Key)
  ```

2. 建置 conda 的虛擬環境
  ```bash
  $ conda create -n Django-web python=3.7.9

  # 啟用虛擬環境
  $ source activate Django-web
  ```

3. 啟用伺服器
  ```bash
  $ python manage.py runserver
  ```


## Setup [pre-commit](http://pre-commit.com/) (非必要)
```bash
$ pip install pre-commit==1.18.3
$ pre-commit install
```
