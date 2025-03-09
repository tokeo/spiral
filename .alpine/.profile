# spiral profile

# repeat the prompt for login shell
export PS1="\[\e[0;33m\]\(> spiral <\) \[\e[1;35m\]\W\[\e[0m\] \[\e[0m\]# "

# define dome aliases
alias launch='screen'
alias ll='ls -la'

# always start the rabbitmq-server
/usr/sbin/rabbitmq-server -detached

# cleanup
clear

# show prompt
spiral --version
echo ""
echo ""
echo "Enter 'launch' to start the Spiral multi-window example."
echo ""
