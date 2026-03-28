.DEFAULT_GOALS := build

.PHONY: build clean cleanall watch count view safe rebuild

# 主编译目标 (增量编译，最快)
build:
	latexmk

# 安全编译目标 (如果增量编译失败，自动清理后全量重编译)
safe:
	latexmk || (echo "Incremental build failed. Cleaning and rebuilding..." && $(MAKE) rebuild)

# 强制全量重编译 (不使用任何旧缓存)
rebuild: cleanall build

# 清理辅助文件 (保留 PDF)
clean:
	latexmk -c

# 清理所有生成文件（包括 PDF 和 out/）
cleanall:
	latexmk -C
	rm -rf out/

# 持续监控编译（文件变化自动重新编译）
watch:
	latexmk -pvc

# 字数统计（需要先编译一次）
count:
	@./script/utils/word_count.sh

# 打开 PDF 查看
view:
	@xdg-open out/zjuthesis.pdf 2>/dev/null || open out/zjuthesis.pdf 2>/dev/null || echo "PDF not found, run 'make build' first"

