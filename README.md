
# Ansible Role: gitlab_hierarchy

Easily create your GitLab hierarchy as group and project tree from a simple YAML.

**Example:**

```
.
├── engineering
│   ├── api
│   ├── frontend
│   └── devops
│       └── ci-cd
└── marketing
    └── website
```

```yaml
gitlab_structure:
  - name: "engineering"
    projects:
      - name: "api"
      - name: "frontend"
    subgroups:
      - name: "devops"
        projects:
          - name: "ci-cd"
  - name: "marketing"
    projects:
      - name: "website"
```

## Description

This role allows you to:
- Create and manage GitLab groups, subgroups, and projects from a single declarative YAML structure.
- Automatically resolve and build the full parent/child hierarchy, supporting unlimited nesting (within GitLab's limits).
- Apply and override configuration options (visibility, features, etc.) globally, per group, or per project, using a clear inheritance model.

# Quick Start

1. Install dependencies :
  ```sh
  poetry install
  ```
2. Modify main.yaml and run your playbook :
  ```sh
  poetry run ansible-playbook main.yaml
  ```
> **Note**: If you do not use Poetry, you have a requirements.txt

## Configurable Variables

You can override the following variables globally (in `default_project_config` or `default_group_config`) or per group/project in your `gitlab_structure`:

**For projects:**
- `name`: Project name (required)
- `description`: Project description
- `visibility`: `private`, `internal`, or `public`
- `initialize_with_readme`: true/false
- `issues_enabled`: true/false
- `merge_requests_enabled`: true/false
- `wiki_enabled`: true/false
- `snippets_enabled`: true/false
- `auto_devops_enabled`: true/false
- `packages_enabled`: true/false
- `container_registry_enabled`: true/false
- `state`: `present` or `absent`

**For groups/subgroups:**
- `name`: Group name (required)
- `description`: Group description
- `visibility`: `private`, `internal`, or `public`
- `state`: `present` or `absent`

You can set these options at any level. Any value not set in a group/project will inherit from the global defaults.

## License

MIT
