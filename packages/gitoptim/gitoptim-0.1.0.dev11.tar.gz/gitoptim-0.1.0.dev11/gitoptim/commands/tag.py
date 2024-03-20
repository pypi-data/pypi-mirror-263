def command():
    """
    Mark the current location in job logs.

    This command can be used before `gitoptim analyse logs --after-last-command` command.
    This combination instructs the SDK to analyse only the logs that appear after this command.

    Example:
    $ npm install
    $ gitoptim tag
    $ npm run test
    $ gitoptim analyse logs --after-last-command

    Above example will only analyse from `npm run test` but not from `npm install`.
    """
