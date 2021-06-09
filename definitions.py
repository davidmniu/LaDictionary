import os, sys

PROJ_ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
EXE_ROOT_DIR = os.path.dirname(sys.executable)
TEX_DIR =  EXE_ROOT_DIR if getattr(sys, 'frozen', False) else os.path.join(PROJ_ROOT_DIR, "latex/")
TEX_PATH = os.path.join(TEX_DIR, "dictionary.tex")
PDF_PATH = os.path.join(TEX_DIR, "dictionary.pdf")
