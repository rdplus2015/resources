
# Git Cheat 

## Configuration and Initialization
```bash
sudo apt update
```
```bash
sudo apt install git
```
```bash
git --version
```

## Configuration and Initialization

- Set username:
  ```bash
  git config --global user.name "user_name"
  ```

- Set email:
  ```bash
  git config --global user.email "my@email.com"
  ```

- Show all configurations:
  ```bash
  git config --global --list
  ```

- Get help:
  ```bash
  git --help
  ```

- Set default branch name for new repositories:
  ```bash
  git config --global init.defaultBranch <branch_name>
  ```

- Rename default branch to `main`:
  ```bash
  git branch -m main
  ```

## SSH Key Configuration

- Generate an SSH key:
  ```bash
  ssh-keygen
  ```

- Display the SSH public key:
  ```bash
  cat ~/.ssh/id_rsa.pub
  ```

## Basic Commands

- Initialize a Git repository:
  ```bash
  git init
  ```

- Check the status of the repository:
  ```bash
  git status
  ```

- ### Staging Area

- Add a file to the staging area:
  ```bash
  git add <file_name>
  ```

- Add all modified files to the staging area:
  ```bash
  git add .
  ```

- Remove files from the staging area:
  ```bash
  git reset
  ```

- Create a commit with a message:
  ```bash
  git commit -m "enter your message here"
  ```

- See differences between the working directory and the index:
  ```bash
  git diff <file_name>
  ```

- See differences after staging:
  ```bash
  git diff --cached
  ```

## History and Inspection

- Show commit history:
  ```bash
  git log
  ```

- Show a specific number of commits:
  ```bash
  git log -n <number>
  ```

- Show details of a specific commit:
  ```bash
  git show <commit_SHA>
  ```

- Checkout an old commit:
  ```bash
  git checkout <commit_SHA>
  ```

- Checkout the latest commit on the default branch:
  ```bash
  git checkout main
  ```

- Tag a commit:
  ```bash
  git tag <tag_name>
  ```

- Delete a tag:
  ```bash
  git tag --delete <tag_name>
  ```

- List all tags:
  ```bash
  git tag
  ```

## Working with Remote Repositories

- Clone a repository:
  ```bash
  git clone <repository_url>
  ```

- Show remote URLs:
  ```bash
  git remote -v
  ```

- Add a remote:
  ```bash
  git remote add origin <repository_url>
  ```

- Update the remote URL:
  ```bash
  git remote set-url origin <new_url>
  ```

- Push to a remote repository:
  ```bash
  git push -u origin main
  ```

- Push tags to a remote repository:
  ```bash
  git push origin --tags
  ```

- Fetch changes from a remote repository:
  ```bash
  git fetch
  ```

- Pull changes from a remote repository:
  ```bash
  git pull
  ```

- Get information about a file (useful for collaboration):
  ```bash
  git blame <file.extension>
  ```

## Branching

- List all branches:
  ```bash
  git branch
  ```

- List all branches including remote branches:
  ```bash
  git branch -a
  ```

- Create a new branch:
  ```bash
  git branch <branch_name>
  ```

- Switch to a branch:
  ```bash
  git checkout <branch_name>
  ```

- Create and switch to a new branch:
  ```bash
  git checkout -b <branch_name>
  ```

- Delete a local branch:
  ```bash
  git branch -d <branch_name>
  ```

- Delete a remote branch:
  ```bash
  git push origin --delete <branch_name>
  ```

- Cherry-pick a commit:
  ```bash
  git cherry-pick <commit_SHA>
  ```
  

## Stashing

- Save changes temporarily:
  ```bash
  git stash
  ```

- List stashed changes:
  ```bash
  git stash list
  ```

- Apply stashed changes:
  ```bash
  git stash apply
  ```

- Apply and remove stashed changes:
  ```bash
  git stash pop
  ```

- Drop a specific stash:
  ```bash
  git stash drop <stash@{n}>
  ```

- Clear all stashes:
  ```bash
  git stash clear
  ```
  
  ### Advanced Usage
- Stash with a descriptive message:
  ```bash
  git stash save "Sauvegarde des modifications avant de revenir à un ancien commit"
  ```
- Stash only tracked files:

  ```bash
  git stash -k
  ```
- Stash including untracked files:

  ```bash
  git stash -u
  ```

## Merging and Rebasing

- Merge branches:
  ```bash
  git merge <branch_name>
  ```

- Rebase branches:
  ```bash
  git rebase <branch_name>
  ```

- Pull with rebase:
  ```bash
  git pull --rebase
  ```

## Understanding Differences: Merge vs Rebase

### `git merge`
- **How it works**: Combines changes from two branches into a new commit.
- **History**: Retains the full history of both branches.
- **Use case**: Useful in collaborative environments where you want to preserve the context of merges.

### `git rebase`
- **How it works**: Moves or combines a sequence of commits to a new base commit.
- **History**: Creates a linear history by rewriting commits.
- **Use case**: Ideal for cleaning up local commits before merging into a shared branch.

### When to use `merge`:
- When you need to preserve the history of how changes were combined.
- When working in a team to show the integration of feature branches.

### When to use `rebase`:
- When you want a cleaner, linear history.
- When preparing commits for a pull request to make the history easier to understand.

## Summary
- Use `merge` to combine branches with full context.
- Use `rebase` to create a linear, cleaner history.


## Revert to a Previous Commit

Reverting to a previous commit can be done if you want to discard recent changes and start from a specific commit.

### Steps to Revert to a Previous Commit

1. **Find the Commit Hash**

   First, identify the hash of the commit you want to revert to. You can use the following command to list your commits:

   ```bash
   git log --oneline
   ```
2. **Checkout to the Specific Commit** 

   Once you have identified the commit hash, you can check out to that specific commit using:
   ```bash
   git checkout <commit-hash>
   ```
3. **Create a New Branch from the Previous Commit**

   It is a good practice to create a new branch from this commit so that you can continue working from this point:

   ```bash
   git checkout -b <new-branch-name>
   ```

## Remove a Commit That Has Not Been Pushed 

If you've committed changes locally that you don't want to keep, you can remove them before pushing.

### Steps to Remove the Last Commit

1. **Reset to the Previous Commit**

   You can use the `git reset` command to remove the last commit:

   ```bash
   git reset --soft HEAD~1
   ```

   -  use `--soft` keeps your changes staged.
   -  Use `--mixed` to unstage the changes.
   -  Use `--hard` to discard the changes completely.

   Warning: Using `--hard` will permanently delete your changes.

2. **Push the Changes to GitHub**

   If you have already pushed the commit to GitHub and want to remove it, you'll need to force push the changes:

   ```bash
   git push origin <branch-name> --force
   ```

### Safety Tips

- Use `git reflog` to recover from accidental resets.
- Always backup important changes before performing destructive operations.
- Communicate with your team when rewriting commit history in shared repositories.
- Use `BFG Repo-Cleaner` or `git filter-branch` to rewrite Git history.

This cheat sheet covers the essential Git commands and concepts you need to know as a developer. For more detailed information, refer to the Git documentation or use `git help <command>`.
