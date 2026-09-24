# Ocean Test Matrix

| Resource | How to generate/test it |
|---|---|
| Repository | Upload this project to GitHub |
| Branch | Create `feature/test-ocean` |
| File | Already present |
| Folder | Already present under `src`, `tests`, `docs` |
| Pull Request | Open a PR from `feature/test-ocean` to `main` |
| Issue | Create 2 issues using the templates |
| User | Add a second collaborator |
| Team | Create a GitHub team and grant repo access |
| Workflow | Included under `.github/workflows` |
| Workflow Run | Push a commit or manually run a workflow |
| Environment | Create `dev` and `prod` in repository Settings |
| Deployment | Run `Deploy Demo` against an environment |
| Deployment Status | Produced by the deployment workflow |
| Release | Create a GitHub Release |
| Tag | Create `v1.0.0` |
| Package | Publish/configure a GitHub package as needed |
| Dependabot Alert | Enable Dependabot and dependency graph/security features |
| Code Scanning Alert | Enable CodeQL workflow and inspect Security tab |
| Secret Scanning Alert | Enable secret scanning; use GitHub's documented safe test procedure |
| Collaborator | Add another GitHub user |
| Team | Create a team in the GitHub organization |

## Suggested test sequence

1. Upload repo.
2. Create branch.
3. Make a change.
4. Open PR.
5. Create issues.
6. Merge PR.
7. Run CI.
8. Run CodeQL.
9. Create environments.
10. Run deploy.
11. Create tag and release.
12. Configure security features.
13. Add collaborator/team.
14. Run Ocean sync and inspect Port entities.
