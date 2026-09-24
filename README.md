# Port Ocean GitHub Demo — Full Lab

Repositorio de laboratorio para probar la integración **GitHub Ocean de Port**.

## Recursos que este repositorio ayuda a generar

- Repository
- Branches
- Files
- Folders
- Pull Requests
- Issues
- Users / Collaborators
- Teams (se crean en GitHub, no en el repo)
- GitHub Actions Workflows
- Workflow Runs
- Environments
- Deployments
- Deployment Status
- Releases
- Tags
- Packages (requiere publicar el paquete)
- Dependabot Alerts
- Code Scanning Alerts
- Secret Scanning Alerts (requiere configurar/usar un caso de prueba seguro en GitHub)

## Estructura

```text
.github/
├── CODEOWNERS
├── dependabot.yml
├── pull_request_template.md
├── ISSUE_TEMPLATE/
│   ├── bug_report.md
│   └── feature_request.md
└── workflows/
    ├── ci.yml
    ├── codeql.yml
    ├── deploy.yml
    └── package.yml

docs/
├── architecture.md
└── ocean-test-matrix.md

src/
├── app.py
└── utils.py

tests/
└── test_app.py

Dockerfile
package.json
pyproject.toml
```

## Cómo usarlo para la POC

1. Crea un repositorio público o privado en GitHub llamado `port-ocean-github-demo`.
2. Sube este contenido.
3. Crea una rama `feature/test-ocean`.
4. Abre un Pull Request.
5. Crea al menos 2 Issues.
6. Ejecuta los workflows de GitHub Actions.
7. Configura environments `dev` y `prod`.
8. Ejecuta el workflow de deploy.
9. Crea un tag y un Release.
10. Publica el paquete de prueba si necesitas probar Packages.
11. Habilita Dependabot y Code Scanning.
12. Agrega un segundo colaborador/equipo si quieres probar esas entidades.

### Importante

Un ZIP no puede crear por sí mismo objetos que viven en GitHub, como Pull Requests,
Issues, Releases, Environments, Deployments, Teams o colaboradores. Esos se crean
después de subir el repositorio a GitHub.

No agregues secretos reales al repositorio.
