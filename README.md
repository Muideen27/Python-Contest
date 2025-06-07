# Python-Contest documentation

# Python-Contest

# Getting Started with Git and GitHub 
## Author: Muideen Ilori

This guide walk through the steps to:

1. Create a `README.md` file locally  
2. Create a GitHub repository  
3. Generate a Personal Access Token (PAT)  
4. Clone the repo into VS Code  
5. Stage, commit, and push your `README.md`  

_Code checking begins at 5:30 PM (America/Chicago). You should finish by 5:40 PM._

---

## 1. Create a Local `README.md` File

1. **Open VS Code** (or any terminal/IDE).
2. Created a project directory in my case I created using `mkdir py_contest`
2. change directory to my folder py_contest using `cd py_contest`
3. In the Directory, I created the READE.md file using `code README.md`

---

## 2. Create a GitHub repository  

1. Creating a github repo was so easy to do
2. I logged into my account, clicked on my profile and seletect ` Your repositories` button
3. Inside the page was a green Icon `New`
4. Inside the Create a new repository page was the Repository name field in my case is `Python-Contest`
5. Lasted create repository button.
6. Easy pizzy `):`

--- 

## 3. Generate a Personal Access Token (PAT) 

1. In GitHub, click your profile icon (top-right) → Settings.
2. In the left sidebar, scroll down → Developer settings.
3. Click Personal access tokens → Tokens (classic) → Generate new token.
4. Under `Note` I entered the name `contest`
5. I selected the 90 days expiration and generate
6. Easy pizzy `):`

---

## 4. Clone the repo into VS Code  

1. I ented the code `git clone https://PAT@github.com/Username/repo-name` inside my directory

---

## 5. Stage, commit, and push your `README.md` 

1. using the code as follows
`git add README.md` 
`git commit -m "my first commit"`
`git push`

## 6. Creating a branch

1. we use the command `git branch` to chech the avaliable branches 
2. To create a branch we use `git checkout -b <name of branch>`