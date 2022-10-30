This file is to explain the bootstrap file and how to use it. 
It also covers how to install sudo permissions for the cyberghost vpn.

MAKE SURE that you run the yadm clone --bootstrap <URL> with SUDO PERMISSION otherwise you will have to manually run the commands in the bootstrap file each with SUDO. Yes, this would make it the 2nd time I made this mistake. SO use SUDO.

the bootstrap file is dedected when cloning a yadm (git) repo. Say 'yes' to 
using the bootstrap file if you want to make yadm install some packages and give 
sudo permissions to xkeysnails to setup the custom keyboard layout. This will also
download the minimalist plugin manager for neovim which upon first lauch will then
download all the packages specified under "HOME/.config/nvim/init.vim". 

For the cyberghost vpn sudo permission you need to look at "/etc/sudoers", there
you add the following line: 
wessel weernink ALL = (root) NOPASSWD: /usr/bin/cyberghostvpn

This will give sudo permissions to the cyberghostvpn executable.

For more notes on the function of the different files and their contents see the comments inside
the respective files.

In case running the bootstrap file causes the .basrc and .profile files not to be swapped with the new files. Make sure to run:
yadm checkout -- <filename>
On each of the files. Then pull. This will make the repo abandon the local versions of the file in favour of HEAD, which is the ones with all my customization.

