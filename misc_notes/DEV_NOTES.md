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

**Date:** May 2, 2025  
**Reason:** Reconciling repo after changing name of root folder.

## 🛠 Resolving Git Push Rejection with `git pull --rebase`

**Context:**  
While trying to push changes to my GitHub repo (`main` branch), I got this error:

```

! \[rejected]        main -> main (fetch first)
error: failed to push some refs to ...
hint: Updates were rejected because the remote contains work that you do not
hint: have locally.

````

**Cause:**  
The remote repository had commits I didn’t have locally — likely added from another machine or via the GitHub UI. Git prevents me from pushing to avoid overwriting them.

**Fix:**  
Used `git pull --rebase` to safely bring down remote changes and replay my local commits on top:

```bash
git pull --rebase origin main
git push origin main
````

**Why `--rebase`?**

* Keeps history clean (avoids unnecessary merge commits)
* Ensures local changes are added *after* remote changes

```

**Date:** May 5, 2025  
**Reason:** Removed a .vscode folder that should have been added to .gitignore


---

### ✅ Removing `.vscode` from Git repo (while keeping it locally)

**Background**: The `.vscode` folder is created by Visual Studio Code to store editor-specific settings. It shouldn't usually be tracked in version control, especially in collaborative projects, because it's often machine- or user-specific.

**Steps Taken**:

1. **Ignored future tracking**:
   Added `.vscode/` to `.gitignore` so Git won’t track it in the future.

   ```bash
   echo ".vscode/" >> .gitignore
   ```

2. **Removed it from Git history (but not from my local machine)**:
   Used the `--cached` flag to stop tracking `.vscode` without deleting the local folder:

   ```bash
   git rm -r --cached .vscode
   ```

3. **Committed and pushed the change**:

   ```bash
   git commit -m "Remove .vscode from repo and ignore in future"
   git push
   ```

**Result**:
`.vscode` is now ignored by Git and no longer exists in the GitHub repo, but it still exists locally for personal use in VS Code.

