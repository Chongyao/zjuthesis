#!/bin/bash
# 替换1_background.tex中的手动引用为\cite
sed -i 's/ \[1\]/ {\\cite{hughes2012finite}}/g' body/graduate/intro/1_background.tex
sed -i 's/ \[2\]/ {\\cite{bathe2006finite}}/g' body/graduate/intro/1_background.tex
sed -i 's/ \[3\]/ {\\cite{nealen2006physically}}/g' body/graduate/intro/1_background.tex
sed -i 's/ \[4\]/ {\\cite{todorov2012mujoco}}/g' body/graduate/intro/1_background.tex
sed -i 's/ \[5\]/ {\\cite{huang2025stiffgipc}}/g' body/graduate/intro/1_background.tex
sed -i 's/ \[6\]/ {\\cite{saad2003iterative}}/g' body/graduate/intro/1_background.tex
sed -i 's/ \[7\]/ {\\cite{bridson2002robust}}/g' body/graduate/intro/1_background.tex
sed -i 's/ \[8\]/ {\\cite{Shewchuk2002whatIsAGoodLinearFiniteElement}}/g' body/graduate/intro/1_background.tex

# 检查修改结果
grep -n "\\cite{" body/graduate/intro/1_background.tex
