set relativenumber
set number
call plug#begin('~/.vim/plugged')

"enter plugins yay.

Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'tpope/vim-commentary'
Plug 'vim-airline/vim-airline'

call plug#end()
set clipboard+=unnamedplus
