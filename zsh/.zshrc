export ZDOTDIR=$HOME/.config/zsh

if [ -f "$ZDOTDIR/zsh-functions" ]; then
	source $ZDOTDIR/zsh-functions
	#zsh_add_file spaceship
fi


if [ -f "$ZDOTDIR/antigen.zsh" ]; then
	source $ZDOTDIR/antigen.zsh

# antigen use oh-my-zsh

	antigen bundles <<EOBUNDLES
		colorize
		fzf
		zoxide
		zsh-users/zsh-syntax-highlighting
		zsh-users/zsh-autosuggestions
		zsh-users/zsh-completions
EOBUNDLES


#	antigen theme trapd00r
#	antigen theme spaceship-prompt/spaceship-prompt

	antigen apply
fi

if [ -f "$ZDOTDIR/zsh-functions" ]; then
	zsh_add_file zsh-aliases
	zsh_add_file zsh-exports
	zsh_add_file zsh-keybindings
fi

fpath+=${ZDOTDIR:-~}/completions

eval $(thefuck --alias)

# Install oh-my-posh:
# curl -s https://ohmyposh.dev/install.sh | bash -s
eval "$(oh-my-posh init zsh --config $HOME/.cache/oh-my-posh/themes/ys.omp.json)"


fastfetch
#if [ -f "/home/timo/.config/fabric/fabric-bootstrap.inc" ]; then . "/home/timo/.config/fabric/fabric-bootstrap.inc"; fi
autoload bashcompinit
bashcompinit
#source "/home/timo/.config/zsh/.bash_completion"
