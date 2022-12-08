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

- 進階版(我有把結果存成json檔)(要透過選項去進行)

![img](https://media.discordapp.net/attachments/868759966431973416/1048203865570426951/image.png?width=1193&height=424)

## 作業心得

在這次作業中，使用python函式編程的技術，讓我更清楚地了解到了函式的威力。使用函式可以讓程式的結構更加清晰，並且可以重複使用，大大提升了程式的可讀性和可維護性。在寫加密解密的過程中，我發現到使用基本的指數運算在解密的時候會跑非常久，這時候我就去搜尋相關資料，找到了python內建的pow()函式，這個函式可以快速的計算指數，並且可以使用mod來達到快速計算的效果。使用這個函式，我解決了原本的問題，並且大大提升了程式的效率。這次的作業讓我更加深刻地體會到了函式編程的重要性，也讓我學到了許多新知識。

## 參考資料

- [RSA加密算法](http://www.isg.rhul.ac.uk/static/msc/teaching/ic2/demo/42.htm)
- [Modular multiplicative inverse function in Python](https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python)
