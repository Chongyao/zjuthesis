## Figure generation caveats — 2026-06-07

- `pdffonts` emitted `Syntax Warning: Mismatch between font type and embedded font file` for the generated PDFs, but still reported `SourceHanSansCN-Regular` as embedded/subset with Unicode mapping. PNG fallbacks were also generated beside each required PDF.

#AA|## 4_results.tex 验证记录
#BB|- 这次迁移只修改了 `body/graduate/paper3/4_results.tex` 和 notepad 备注。编译前已修正过一次 `\includegraphics` 路径笔误，最终版本已恢复为 `\linewidth`。
