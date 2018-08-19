alias ll="ls -alF"

if which pyenv > /dev/null; then
  eval "$(pyenv init -)";
fi
export PYENV_ROOT=/usr/local/var/pyenv

if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
export PATH="~/.pyenv/bin:$PATH"

export PATH=$PATH:/Users/YourUserGoesHere/Library/Python/3.7/bin
