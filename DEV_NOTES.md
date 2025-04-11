# Dev Notes – Folder & GitHub Repo Renaming

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