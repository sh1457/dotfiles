set fish_greeting

if status is-interactive
    set -x STARSHIP_CONFIG ~/.config/starship/config.toml
    starship init fish | source
end
