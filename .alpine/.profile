# image profile

# check if app has an overruled .docker dir
if [ -d "/app/.docker" ]
then
  # copy into $HOME
  cp -r /app/.docker/.* $HOME >/dev/null 2>&1
  cp -r /app/.docker/* $HOME >/dev/null 2>&1
fi

if [ -f "$HOME/.launchrc" ]
then
  source $HOME/.launchrc
fi
