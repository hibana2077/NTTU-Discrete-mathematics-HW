<!--
 * @Author: error: git config user.name && git config user.email & please set dead value or install git
 * @Date: 2022-11-27 23:22:54
 * @LastEditors: error: git config user.name && git config user.email & please set dead value or install git
 * @LastEditTime: 2022-11-27 23:46:29
 * @FilePath: \2上\dismath\README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# RSA 加解密作業 作業報告

## 作業環境

![windows11](https://img.shields.io/badge/windows-11-blue?style=flat&logo=windows)
![python](https://img.shields.io/badge/python-3.10.8-blue?style=flat&logo=python)
![vscode](https://img.shields.io/badge/VScode-1.73.1-007ACC?style=flat&logo=Visual-studio-code)


## 執行結果

- 基礎版

![img](https://media.discordapp.net/attachments/1044190059596873819/1046449228932714516/image.png)

- 進階版(我有把結果存成json檔)

![img](https://media.discordapp.net/attachments/1044190059596873819/1046449430116716554/image.png?width=1193&height=246)

## 作業心得

這次的作業我用`python`來編寫，並且使用了物件導向的技術，在寫加密解密的
過程中，我發現了一個問題，就是如果使用基本的指數運算，在解密的時候會跑非常久，後來去搜尋相關資料發現可以使用 `python` 內建的 `pow()` 來達成目的 ， 這個函式可以快速的計算指數，而且可以使用 `mod` 來達到快速計算的效果，這個函式的使用方式如下:

```python
pow(x, y, z)
# x: 底數
# y: 指數 -> 這裡設為 -1 就可以達到取模運算的逆。
# z: 取餘數
```

## 參考資料

- [RSA加密算法](http://www.isg.rhul.ac.uk/static/msc/teaching/ic2/demo/42.htm)
- [Modular multiplicative inverse function in Python](https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python)
