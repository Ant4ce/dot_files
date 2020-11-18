set relativenumber
set number
call plug#begin('~/.vim/plugged')

"enter plugins yay.

Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'tpope/vim-commentary'
Plug 'vim-airline/vim-airline'
Plug 'sevko/vim-nand2tetris-syntax'

call plug#end()
set clipboard+=unnamedplus
syntax on 
