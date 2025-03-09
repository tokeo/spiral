# image profile

# check if app has an overruled .docker dir
if [ -d "/app/.docker" ]
then
  # copy into $HOME
  cp -a /app/.docker/.[a-zA-U0-9]* $HOME/ >/dev/null 2>&1
  cp -a /app/.docker/* $HOME/ >/dev/null 2>&1
fi

if [ -f "$HOME/.launchrc" ]
then
  source $HOME/.launchrc
fi
