# Git Cheatsheet

You can find most of this on the internet but for the sake of complecity of this session below are the commands that I personally find very useful

## To check the status
`git status`

## To add untracked file or files
```
# To add 1 file
git add 'file-name'

# To add all untracked files
git add .

# To add all files inside a directory

git add 'directory-name'

```

## To remove a tracked file

`git rm --cached file3.txt`

## Commit, Revert, Reset

```
# to commit

git commit -m "message"

# to uncommit & and get your changes in unstagged area

git reset <commit-id or ref> ( commit id or ref of the changes after which your new commit changes came)

# to trash your commmit changes

git revert <commit-id or ref> ( commit id of the changes you want to trash)
```

## To see changes of a specific commit
`git show <commit-id>`
