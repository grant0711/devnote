# Get our full filepath
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Read in our input vars from user input
read -p "Enter devnote url POST endpoint:" DEVNOTE_URL
read -p "Enter devnote token for authentication:" DEVNOTE_TOKEN
read -p "Enter devnote local filepath to store local files [default=$SCRIPT_DIR/local]": DEVNOTE_LOCAL
# If local filepath empty string set to default
DEVNOTE_LOCAL=${DEVNOTE_LOCAL:-"$SCRIPT_DIR/local"}

# Delete our commands exporting our env vars from .bashrc if they have already been set
DEVNOTE_URL_LN=$(grep -Fn 'export DEVNOTE_URL=' "$HOME/.bashrc" | cut -d: -f1)
if ! [[ -z $DEVNOTE_URL_LN ]]
then
    sed -i "${DEVNOTE_URL_LN}d" $HOME/.bashrc
fi

DEVNOTE_TOKEN_LN=$(grep -Fn 'export DEVNOTE_TOKEN=' "$HOME/.bashrc" | cut -d: -f1)
if ! [[ -z $DEVNOTE_TOKEN_LN ]]
then
    sed -i "${DEVNOTE_TOKEN_LN}d" $HOME/.bashrc
fi

DEVNOTE_LOCAL_LN=$(grep -Fn 'export DEVNOTE_LOCAL=' "$HOME/.bashrc" | cut -d: -f1)
if ! [[ -z $DEVNOTE_LOCAL_LN ]]
then
    sed -i "${DEVNOTE_LOCAL_LN}d" $HOME/.bashrc
fi

# Append our export commands to .bashrc
echo "export DEVNOTE_URL=$DEVNOTE_URL" >> $HOME/.bashrc
echo "export DEVNOTE_TOKEN=$DEVNOTE_TOKEN" >> $HOME/.bashrc
echo "export DEVNOTE_LOCAL=$DEVNOTE_LOCAL" >> $HOME/.bashrc

# Make devnote executable and move to /bin
chmod +x "$SCRIPT_DIR/app/devnote.py"
sudo cp "$SCRIPT_DIR/app/devnote.py" /bin/devnote

# Looks good!
echo "All done! Restart a new terminal and add a new devnote via command 'devnote'"
