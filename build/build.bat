@echo off
:: nuitka --standalone --lto=yes --clang --remove-output --output-dir=payload ../payload/main.py
nuitka --standalone --onefile --lto=yes --clang --remove-output --output-filename=payload ../payload/main.py