# Dev Notes

**Date:** April 11, 2025  
**Reason:** Expanded the repo beyond MIT 6.100L to include extra exercises and challenges.

## Steps Taken:

1. **Renamed the local folder** using the terminal:
    ```bash
    mv mit-6100l-fall-2022-undergraduate-introduction-to-cs-and-programming-using-python mit-6100l-extended-learning
    cd mit-6100l-extended-learning
    ```

2. **Renamed the GitHub repository**:
    - Went to GitHub → Repo → Settings → Changed name to `mit-6100l-extended-learning`

3. **Updated the local Git remote** to match the new GitHub URL:
    ```bash
    git remote set-url origin https://github.com/k10sj02/mit-6100l-extended-learning.git
    ```

4. **Confirmed the new remote**:
    ```bash
    git remote -v
    ```

5. **Committed and pushed updates** as normal:
    ```bash
    git add .
    git commit -m "Renamed project folder and updated repo URL"
    git push origin main
    ```

---

## 🔁 Git Pull & Merge Process

### ❓ Situation
I updated the repo on GitHub and also made local changes. When trying to push, I got an error because the remote was ahead of the local branch.

### ✅ What I Did

1. Tried to push changes:
   git push origin main
   Got an error because the remote branch had new commits.

2. Pulled remote changes:
   git pull origin main
   This triggered a merge because both local and remote had changes.

3. Git opened a merge message. I saved and exited the editor.

4. Added resolved files (in this case `README.md`):
   git add README.md

5. Committed the merge:
   git commit -m "Merge remote-tracking branch 'origin/main'"

6. Pushed everything to GitHub:
   git push origin main

---

## 🧾 Git Pull Safety Workflow

### 🔍 1. Check local changes
   git status

### 🔒 2. Fetch remote updates (optional but smart)
   git fetch origin main

### 👀 3. View differences
   git diff HEAD origin/main

### 🔄 4. Pull remote changes
   git pull origin main

### ⚔️ 5. Resolve merge conflicts (if any)
- Edit conflicted files
- Then:
   git add <filename>
   git commit
   git push origin main

### 💡 Optional Tips
- Skip editor prompt:
   git pull --no-edit origin main

- Use rebase for cleaner history:
   git pull --rebase origin main
