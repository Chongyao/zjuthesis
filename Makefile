.DEFAULT_GOALS := build

# 输出文件名配置
OUTPUT_DIR := out
PDF_NAME := zjuthesis.pdf
COMPRESSED_NAME := zjuthesis_compressed.pdf

.PHONY: build clean cleanall watch count view safe rebuild

# 主编译目标 (增量编译，最快)，编译后自动压缩 PDF
build:
	latexmk
	@if [ -f $(OUTPUT_DIR)/$(PDF_NAME) ]; then \
		echo "Compressing PDF..."; \
		gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dNOPAUSE -dBATCH \
			-dQUIET \
			-sOutputFile=$(OUTPUT_DIR)/$(COMPRESSED_NAME) $(OUTPUT_DIR)/$(PDF_NAME); \
		echo "Compressed PDF saved to $(OUTPUT_DIR)/$(COMPRESSED_NAME)"; \
		ls -lh $(OUTPUT_DIR)/$(PDF_NAME) $(OUTPUT_DIR)/$(COMPRESSED_NAME) | awk '{print $$9, "→", $$5}'; \
	fi

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
