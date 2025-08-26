# Set the directory we want to store zinit and plugins
ZINIT_HOME="${XDG_DATA_HOME:-${HOME}/.local/share}/zinit/zinit.git"

# Download Zinit, if it's not there yet
if [ ! -d "$ZINIT_HOME" ]; then
   mkdir -p "$(dirname $ZINIT_HOME)"
   git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME"
fi

# Source/Load zinit
source "${ZINIT_HOME}/zinit.zsh"

zinit ice as"command" from"gh-r" \
          atclone"./starship init zsh > init.zsh; ./starship completions zsh > _starship" \
          atpull"%atclone" src"init.zsh"
zinit light starship/starship

# Add zsh plugins
zinit light zsh-users/zsh-syntax-highlighting
zinit light zsh-users/zsh-completions
zinit light zsh-users/zsh-autosuggestions
zinit light Aloxaf/fzf-tab

#zinit ice depth=1
#zinit light jeffreytse/zsh-vi-mode

# Add snippets
#zinit snippet OMZP::sudo
zinit snippet OMZP::colorize
zinit snippet OMZP::colored-man-pages

# Source additional files if they exist
[[ ! -f ~/.config/zsh/zsh-aliases ]] || source ~/.config/zsh/zsh-aliases
[[ ! -f ~/.config/zsh/zsh-exports ]] || source ~/.config/zsh/zsh-exports
[[ ! -f ~/.config/zsh/zsh-keybinds ]] || source ~/.config/zsh/zsh-keybinds

# Source other specific configs if the corresponding app is available
which fabric >/dev/null && source ~/.config/zsh/fabric
which yazi >/dev/null && source ~/.config/zsh/yazi

# Load completions
autoload -Uz compinit && compinit

zinit cdreplay -q

# History (see man zshoptions)
HISTSIZE=10000
HISTFILE=~/.zsh_history
SAVEHIST=$HISTSIZE
HISTDUP=erase
setopt appendhistory
setopt sharehistory
setopt hist_ignore_space
setopt hist_ignore_all_dups
setopt hist_save_no_dups
setopt hist_ignore_dups
setopt hist_find_no_dups

# Completion styling (see man zslzle)
#zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"
zstyle ':completion:*' menu no
zstyle ':fzf-tab:complete:cd:*' fzf-preview 'ls --color $realpath'
zstyle ':fzf-tab:complete:__zoxide_z:*' fzf-preview 'ls --color $realpath'

#bindkey -v

# Shell integrations
# Unalias zi first to make zoxide work with default setting
unalias zi
which fzf >/dev/null && eval "$(fzf --zsh)"
which thefuck >/dev/null && eval "$(thefuck --alias)"
which zoxide >/dev/null && eval "$(zoxide init zsh)"

which fastfetch >/dev/null && fastfetch
