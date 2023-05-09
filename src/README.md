# Git and GitHub

Git - local version control system
GitHub - cloud repository website, website that is integrated with git system,
            shareable repository/location, that produces shareable link

git
 - local vs cloud
 - create project -> enable git (enable VCS) -> add the cloud link (add origin)
  -> create repository on the GitHub -> use the link as origin
  -> configure global git configuration (name, email)
  -> add and commit, push, pull

1 - Git commands you will use for local project:
        cd projectDirectory
        git init
        git add folder1/scenario1.py
        git commit -m 'message for your commit'
        git status
        git log
        git push
        git pull

2- Branching:
    create new branch, switch to new branch, create Pull Requests (highlights the changes)
    a - Create new local branch:
            1 - Pycharm:
                    select new branch option for current branch (bottom right)
                    push each branch separately, creates origin:feature1-scen1 automatically
            2 - git bash, git CLI (Command Line Interface):
                    git checkout -b 'new-branch-name'
                    git add folder1/ scenario1.py
                    git commit -m 'message for your commit'
                    git push
                    git push -- set upstream origin features1-scen2

    b - Collaboration in GitHub:
        1 - Creating the Pull Requests, get reviews and approval from Senior Engineer
        2 - Merge your code in your branch to a master (main) branches

3- Get/download gitHub project to your local location and start new project:
        go to your terminal:
            cd /c/dev/
            mkdir temp
            pwd
            /c/dev/temp/
            git cole https://github.com/MassoumAbdel/PythonBasics.git
            (previous link comes from the link of your project you want to download get it from code(https))
            cd pythonBasics
            git log # shows latest commit in the log
            # then you can open in PyCharm and start working on it as regular project

- Ignore files
   - create .gitignore (list of files to be ignored bi git)
   - you can copy the standard .gitignore file for python projects (like we did in the class)

----
# MarkDown (.md) files for Project Documentation
       README files are previewed in gitHub projects by default, 
       so usually README files are created in Markdown language
       so text format looks more readable and neat, link, images can be also included in the documents.
       (Most of functionalities you could in MS Word or other text Editors).
        Markdown language is mostly used to write technical text.
 ## two hashtags are heading 2
 ### two hashtags are heading 3
 #### two hashtags are heading 4

**marking the text as bold**

*italic text is covered with asterisk*

Below you can the bullet point:
- point 1 of many points
- point 2 of many points
- point 3 of many points
- point 4 of many points

## Highlight the code or command line
You can highlight the code with apostrophe (') or with indentation:

a - using apostrophe:
```python
print('python code inside the code block in MD file')
# this is how comment line of the python code block
```

```shell
pwd
cd /c/dev/
mkdir "pythonBasics"
# comment line of shell
cd pythonBasics
```

b - indent the line to put in code box

    print('hello world')

## Displaying links in MD file

please [click here](https://www.jetbrains.com/help/pycharm/markdown.html) to see more details about md features

## Displaying the pictures in MD file

you can see the pictures below

[funny classroom](funny-classroom.png)

picture will be between the text

another picture 

[picture2](2.jpeg)

## References:
1. level up github account [link](https://github.com/levelupcgi?tab=repositories).
2. [Markdown support](https://www.jetbrains.com/help/pycharm/markdown.html)


