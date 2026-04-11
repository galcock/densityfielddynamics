#!/bin/bash
# Compile Patent 14 LaTeX documents
# Usage: ./compile.sh [main|engineering|all]

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

compile_doc() {
    local base="$1"
    echo "=== Compiling ${base}.tex ==="
    pdflatex -interaction=nonstopmode "${base}.tex" && \
    pdflatex -interaction=nonstopmode "${base}.tex" && \
    echo "=== ${base}.pdf generated successfully ===" || \
    echo "=== WARNING: ${base}.tex had compilation issues ==="
}

case "${1:-all}" in
    main)
        compile_doc main
        ;;
    engineering)
        compile_doc engineering_design
        ;;
    all)
        compile_doc main
        compile_doc engineering_design
        ;;
    *)
        echo "Usage: $0 [main|engineering|all]"
        exit 1
        ;;
esac

echo ""
echo "Output files:"
ls -la "$DIR"/*.pdf 2>/dev/null || echo "No PDF files generated."
