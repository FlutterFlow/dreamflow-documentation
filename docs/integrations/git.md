---
slug: /integrations/git
title: Git
description: Learn how to connect your Dreamflow project with Git providers and perform Git operations.
tags: [Git, Integration, Dreamflow]
sidebar_position: 3
toc_max_heading_level: 4
keywords: [git, Integration, Dreamflow, Version Control, Source Control]
---

# Git

Dreamflow supports Git integration, allowing you to connect your projects directly to GitHub, GitLab, or other Git providers.
:::warning

Currently, it does not support multi-user collaboration within the same repository. If multiple Dreamflow projects attempt to use the same repo, the system will detect and restrict it.

For team collaboration, please contact the **Enterprise team**.

:::

## Connect Repository

You can connect a repository in two main ways:

- **Clone Codebase**: Use this option when you want to start a new project in Dreamflow using an existing Git repository.

- **Connect Project to Git**: Use this option when you already have a project built inside Dreamflow and want to link it to a Git repository.

### Clone Codebase

To clone a codebase:

1. Go to the [**Dreamflow Dashboard**](https://app.dreamflow.com/dashboard) and select **Clone Codebase**.
2. In the dialog box, enter the following details:
    - **Project Name** – Choose a name for your Dreamflow project.
    - **Repository URL** – Paste the HTTPS URL of your Git repository (e.g., `https://github.com/username/repo.git`).
    - **Access Token** – Enter your personal access token. Refer to the [**Get Access Token**](#get-access-token) for more information on how to generate one.
3. Once all fields are filled in, click **Clone Repository**. 

Dreamflow will then clone the repository, import your Flutter project files, and automatically open it in your workspace for editing.

Here’s an example of cloning a repository from GitHub:

<div style={{
    position: 'relative',
    paddingBottom: 'calc(52.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/kUa2NnyUeTHlPsjdfl3B?embed&show_copy_link=true"
        title=""
        style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            colorScheme: 'light'
        }}
        frameborder="0"
        loading="lazy"
        webkitAllowFullScreen
        mozAllowFullScreen
        allowFullScreen
        allow="clipboard-write">
    </iframe>
</div>
<p></p>

:::warning

Dreamflow currently supports **Flutter repositories only**. If your repository contains non-Flutter code or multiple projects (like a monorepo), the import may fail.

Support for monorepos is planned for a future update.

:::

### Connect Project to Git

To connect a Dreamflow project to Git repo:

1. Open your existing project in Dreamflow. Go to the **Source Control Panel** on the left sidebar and click **Connect Repository**. 
2. In the dialog, provide:
    1. **Repository URL** – Paste the HTTPS URL of your new blank repository. If you haven’t already created one, you can create a new repository on your Git provider (such as [GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)) before proceeding.
    2. **Access Token** – Enter your personal Git access token. Refer to the [**Get Access Token**](#get-access-token) for more information on how to generate one.
3. Click **Connect**.

Once connected, Dreamflow will automatically start tracking file changes, which you can view in the **Changes** list.

:::warning

The repository must be blank or contain only a README and/or LICENSE file.

:::

Here’s an example of connecting a project to a repository hosted on GitHub:

<div style={{
    position: 'relative',
    paddingBottom: 'calc(52.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/sVeZ20PpJwRrMpUwTJ6I?embed&show_copy_link=true"
        title=""
        style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            colorScheme: 'light'
        }}
        frameborder="0"
        loading="lazy"
        webkitAllowFullScreen
        mozAllowFullScreen
        allowFullScreen
        allow="clipboard-write">
    </iframe>
</div>
<p></p>

### Get Access Token

To connect with your Git provider, you’ll need to generate a **Personal Access Token (PAT)**. This token allows Dreamflow to authenticate and securely interact with your repository.

#### For GitHub

Follow these official GitHub guides to create a Personal Access Token:

- [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- [Creating a fine-grained personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token)
- [Creating a classic personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)

**Required Scopes for Dreamflow:**

- For **Fine-grained tokens:** Grant **Content: Read & Write** access to the specific repository you plan to use.
- For **Classic tokens:** Enable **repo** and **workflow** permissions.

#### For GitLab

You can generate a Personal Access Token directly from your GitLab account by following the official documentation:

- [GitLab: Create a personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)

**Required Scopes for Dreamflow:**

- `api`: Full API access.
- `read_repository` and `write_repository` to read and write code to your repository.

Once your token is created, copy it and paste it into the **Access Token** field when connecting your repository in Dreamflow.

## Git Operations

This section walks you through how to perform common Git operations like branching, committing, and syncing your code.

### Branching

You can easily manage branches directly within the platform, i.e., create new ones, switch between existing ones, and refresh your branch list when needed.

#### Create a New Branch

You can create a new branch to work on a specific feature or fix without affecting the `main` branch. 

To create a new branch:

1. Open the **branch dropdown** in the **Source Control panel** and choose the branch you want to create your new branch from (e.g., `main`).
2. Click the **+** button on the right side of the panel.
3. In the dialog, enter a name for your new branch (for example, `feature/user-profile`).
4. Click **Save**.

Once created, Dreamflow will automatically switch your workspace to the new branch.

<div style={{
    position: 'relative',
    paddingBottom: 'calc(52.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/EJWEpo1PSAo6xE5ow1e0?embed&show_copy_link=true"
        title=""
        style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            colorScheme: 'light'
        }}
        frameborder="0"
        loading="lazy"
        webkitAllowFullScreen
        mozAllowFullScreen
        allowFullScreen
        allow="clipboard-write">
    </iframe>
</div>
<p></p>

#### View and Switch Branches

You can view all available branches in the dropdown menu in the **Source Control panel**. To switch branches, simply open the dropdown and select the branch you want to work on.

![switch-branch.avif](imgs/switch-branch.avif)

#### Refresh Branch List

If you’ve created or deleted branches outside of Dreamflow, click the **Refresh Branches** icon beside the dropdown. This updates your local list so you always see the latest branches available in your remote repository.

![refresh-branch.avif](imgs/refresh-branch.avif)

### Push Changes

To push changes from your project to the remote repository:

1. Make edits to your app.
2. Check **Source Control > Changes**. The modified file will be tagged **M** and listed there.
3. (Optional) Click **View Diff** to compare your edit with the previous version.
4. Enter a short **commit message** (e.g., “Change welcome message”).
5. Click the **Push** icon to commit and push the update to your connected repository.

<div style={{
    position: 'relative',
    paddingBottom: 'calc(52.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/ip4kqyERAlghfxmFhV6c?embed&show_copy_link=true"
        title=""
        style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            colorScheme: 'light'
        }}
        frameborder="0"
        loading="lazy"
        webkitAllowFullScreen
        mozAllowFullScreen
        allowFullScreen
        allow="clipboard-write">
    </iframe>
</div>
<p></p>


### Revert Changes

If you want to undo changes before pushing them, you can revert individual files or all changes at once.

- To revert a specific file, **right-click** on it and select **Discard Changes**.
- To discard all pending changes, click the **discard icon** on the right side of the Source Control panel.

![revert-change.avif](imgs/revert-change.avif)

### Pull Changes

To update your project with the latest code from the remote repository, click the **pull icon** in the Source Control panel. Dreamflow will fetch and merge any new commits from your remote branch.

![pull-changes.avif](imgs/pull-changes.avif)

