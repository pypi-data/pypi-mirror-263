# SCIV

> SCIV: Viewing the integrated landscape of variant mapping at single-cell resolution

> SCIV: 在单细胞分辨率下查看突变映射的整合景观

## 1. 介绍

## 2. 安装

## 3. 上传

> upload

> test

```shell
py -m build
twine check dist/*
twine upload --repository testpypi dist/*
```

> production

```shell
py -m build
twine check dist/*
twine upload dist/*
```

## 4. 使用

```shell
vim ~/.bashrc
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
source ~/.bashrc

```

> test

```shell
pip3 install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
pip3 install scLift -i https://test.pypi.org/simple/
```

> production

```shell
pip3 install scLift
```
