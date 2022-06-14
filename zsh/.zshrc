export ZDOTDIR=$HOME/.config/zsh

if [ -f "$ZDOTDIR/zsh-functions" ]; then
	source $ZDOTDIR/zsh-functions
	zsh_add_file spaceship
fi


if [ -f "$ZDOTDIR/antigen.zsh" ]; then
	source $ZDOTDIR/antigen.zsh

	antigen use oh-my-zsh

	antigen bundles <<EOBUNDLES
		colorize
		fzf
		zoxide
		zsh-users/zsh-syntax-highlighting
		zsh-users/zsh-autosuggestions
		zsh-users/zsh-completions
EOBUNDLES


#	antigen theme trapd00r
	antigen theme spaceship-prompt/spaceship-prompt

	antigen apply
fi

if [ -f "$ZDOTDIR/zsh-functions" ]; then
	zsh_add_file zsh-aliases
	zsh_add_file zsh-exports
	zsh_add_file zsh-keybindings
fi

fpath+=${ZDOTDIR:-~}/completions

eval $(thefuck --alias)

neofetch
