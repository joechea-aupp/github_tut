## To Get Start

Download [GitHub Desktop app](https://desktop.github.com/)

Install the application, sign-in with you github account (the one that you are using with github classroom)

then chose the repository that you just fork

![picture1](resources/image_2023-07-27_22-06-51.png)

Once done, choose folder that you want to store the project on your local computer

![picture2](resources/image_2023-07-27_22-06-54.png)

click on clone to start download the project.

After made change on the project, go back to the github desktop app and observe the change

![picture3](resources/image_2023-07-27_22-21-52.png)

To save change or commit the history, locate the bottom left screen, give title to the change history and click on `commit to main` button.

![picture4](resources/image_2023-07-27_22-29-22.png)

once commited, your change file will disappear from the left menu.

Click `Push origin` button to send the change to github (cloud).

![picture5](resources/image_2023-07-27_22-30-59.png)

## 2. Git In VS Code

Green vertical line after line number indicate the incoming update to the repository.

![picture5](resources/image_2023-07-27_22-35-04.png)

Blue vertical line after line number indicate the outgoing update to the repository. if you click on the blue line, you will see the change that you made.

![picture6](resources/image_2023-07-27_23-09-10.png)

## 3. Github Desktop

- Green color indicate the additional data is added to the repository.
- Red color indicate the data is deleted from the repository.
- Orange color indicate the data is modified in the repository.

![picture7](resources/image_2023-07-27_23-18-22.png)

### 3.1. History

On Github Desktop, you can see the history tab on the right of `Changes` tab. Click on it to see the history of the repository.

![picture8](resources/image_2023-07-27_23-25-48.png)

each commit that we save will be shown on the history tab. Click on the commit to see the change that we made.

### 3.2. Git Revert

If you want to revert the change that you made, right click on any history that you want to reverted and click on `Revert changes in commit`.

![picture9](resources/image_2023-07-27_23-32-01.png)

### 3.2 Dealing with Conflict

If your change is impact or about to overwrite the current content that exist on your project, a prompt to resolve conflict will appear.

![picture11](resources/image_2023-07-28_08-26-24.png)

Switch to VS Code to resolve the conflict. file that marked as conflicted will have `>>>>>>` and `<<<<<<` on the file and colored in red or orange.

![picture10](resources/image_2023-07-28_08-26-31.png)

click on the conflicted file and click on `Resolve in Merge Editor` button on the bottom left of the screen. the incoming change will be on the left side and the outgoing change will be on the right side.

![picture12](resources/image_2023-07-28_08-29-11.png)

click `Accept Incoming Change` to accept the incoming change or click `Accept Current Change` to accept the outgoing change.

![picture13](resources/image_2023-07-28_08-30-03.png)

click `Accept Both Changes` to accept both change.

click `Complete Merge` to complete the merge.

![picture14](resources/image_2023-07-28_08-33-51.png)

## Branching

Branching is a way to work on different version of a repository at one time. By default, your repository has one branch named `main` which is considered to be the definitive branch. We use branches to experiment and make edits before committing them to `main`.

When you create a branch off the `main` branch, you’re making a copy, or snapshot, of `main` as it was at that point in time. If someone else made changes to the `main` branch while you were working on your branch, you could pull in those updates.

### 1. Create Branch

To create a new branch, click on the `Current Branch` button on the top left of the screen and click on `New Branch`.

![picture14](resources/image_2023-07-28_08-47-02.png)

Give the branch a name and click `Create Branch` button.

![picture15](resources/image_2023-07-28_08-48-14.png)

Any change you made on the new branch will not affect the `main` branch.
