# Set the directory we want to store zinit and plugins
ZINIT_HOME="${XDG_DATA_HOME:-${HOME}/.local/share}/zinit/zinit.git"

# Download Zinit, if it's not there yet
if [ ! -d "$ZINIT_HOME" ]; then
   mkdir -p "$(dirname $ZINIT_HOME)"
   git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME"
fi

# Source/Load zinit
source "${ZINIT_HOME}/zinit.zsh"

# Remove "zi" alias for default zoxide alias to work
#zinit ice atload'unalias zi'

zinit ice as"command" from"gh-r" \
          atclone"./starship init zsh > init.zsh; ./starship completions zsh > _starship" \
          atpull"%atclone" src"init.zsh"
zinit light starship/starship

# Add Spaceship
#zinit light spaceship-prompt/spaceship-prompt
#zinit light spaceship-prompt/spaceship-vi-mode

# Source Spaceship configuration if it exists
#[[ ! -f ~/.config/zsh/spaceship ]] || source ~/.config/zsh/spaceship

# Add zsh plugins
zinit light zsh-users/zsh-syntax-highlighting
zinit light zsh-users/zsh-completions
zinit light zsh-users/zsh-autosuggestions
zinit light Aloxaf/fzf-tab

# Add snippets
#zinit snippet OMZP::sudo
zinit snippet OMZP::colorize
zinit snippet OMZP::colored-man-pages
zinit snippet OMZP::vi-mode

# Load completions
autoload -U compinit && compinit

zinit cdreplay -q

#spaceship add --after line_sep vi_mode

# Source additional files if they exist
[[ ! -f ~/.config/zsh/zsh-history ]] || source ~/.config/zsh/zsh-history
[[ ! -f ~/.config/zsh/zsh-aliases ]] || source ~/.config/zsh/zsh-aliases
[[ ! -f ~/.config/zsh/zsh-exports ]] || source ~/.config/zsh/zsh-exports
[[ ! -f ~/.config/zsh/zsh-keybinds ]] || source ~/.config/zsh/zsh-keybinds

# Completion styling
#zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"
zstyle ':completion:*' menu no
zstyle ':fzf-tab:complete:cd:*' fzf-preview 'ls --color $realpath'
zstyle ':fzf-tab:complete:__zoxide_z:*' fzf-preview 'ls --color $realpath'


# Shell integrations
unalias zi
eval "$(fzf --zsh)"
eval "$(thefuck --alias)"
eval "$(zoxide init zsh)"
#eval spaceship_vi_mode_enable

fastfetch
