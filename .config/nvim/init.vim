set relativenumber
set number
call plug#begin('~/.vim/plugged')

"enter plugins yay.

Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'tpope/vim-commentary'
Plug 'vim-airline/vim-airline'
Plug 'sevko/vim-nand2tetris-syntax'
Plug 'tomasiser/vim-code-dark'

call plug#end()
set clipboard+=unnamedplus
syntax on 
set autoread
set termguicolors
let g:airline_theme = 'codedark'
set expandtab
set tabstop=4
set shiftwidth=4
set autoindent
