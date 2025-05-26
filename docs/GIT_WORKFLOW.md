# Greyhawk Weather — Git Workflow Cheat Sheet

A simple, safe workflow for managing your stable code and experimental features using Git branches.

---

## Core Concepts

- **`main` branch:** Your stable, working version of the project.
- **Feature branches:** Isolated environments for developing new features or experiments.
- **Switching branches:** Allows moving between stable and experimental code without risk.

---

## Common Commands

| Action                      | Command                                  | Notes                              |
|-----------------------------|-----------------------------------------|----------------------------------|
| Create a new feature branch | `git checkout -b feature/branch-name`   | Starts a new branch from current code |
| Switch to main branch        | `git checkout main`                      | Returns to your stable code        |
| Stage all changes            | `git add .`                             | Prepare changes for commit        |
| Commit changes               | `git commit -m "Commit message"`        | Save changes locally              |
| Push branch to GitHub        | `git push origin feature/branch-name`   | Backup branch remotely            |
| Merge feature into main      | `git checkout main` <br> `git merge feature/branch-name` | Incorporate changes after testing |

---

## Suggested Workflow for Greyhawk Weather Project

1. **Keep `main` branch stable and tagged:**

   - Tag stable releases with version, e.g., `v1.2.2-stable`.
   - Use tags as rollback points if needed.

2. **Develop new features in branches named by feature:**

   - Examples:
     - `feature/daily-stages`
     - `feature/weather-persistence`
     - `feature/geographic-influence`

3. **Push feature branches regularly to GitHub for backup.**

4. **Test extensively in feature branch before merging.**

5. **Merge back into `main` only when stable and tested.**

6. **Keep your `TODO.md` updated with task status linked to branches.**

---

## Tips

- Write descriptive commit messages.
- Commit often, especially after completing logical steps.
- Use GitHub Desktop if you prefer GUI for commits and branch switching.
- Consider setting up GitHub Actions to run tests automatically on your feature branches.

---

## Next Steps in Greyhawk Weather (from TODO)

- Add detailed daily stages for weather (dawn, noon, dusk, midnight).
- Implement weather persistence between days.
- Develop geographic influence modeling between towns.
- Add export to `.txt` or `.md`.
- Highlight festival days and warnings.
- Add moonrise/set or visibility flags.
- Refactor seasonal profiles for data-driven design.

---

## Additional Resources

- [Git Branching Basics](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
- [GitHub Desktop Documentation](https://docs.github.com/en/desktop)
- [GitHub Actions for Python](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)

---

*Keep this sheet handy to streamline your development and protect your stable Greyhawk Weather codebase!*
