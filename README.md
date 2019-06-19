# git process
Create a repo directory and type command 'https://github.com/jasontian-toosle/lupo.git'. Then you will find there is a folder called lupo and enter it.

Try following git commands:
git status (show the current branch and files with changes)

git pull origin master (pull the latest code from original master branch)

git fetch (fetch all remote branch information)

git checkout -b sample (create local branch named 'sample')

git commit -m "commit message" (commit staged changes)

git stash (stash all changes)

git stash pop (unstash the changes from previous stashing)

git push origin sample (push all staged files to remote)


# Steps
open termial

'mkdir training'
'cd training'

install homebrew which help to install package on mac easily
</usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)">
install gradle to initialize project(https://gradle.org/install/)
'java -version' will show your system java version, make sure you have at least 1.8
'brew install gradle'
read article to see how gradle start to build project https://guides.gradle.org/building-spring-boot-2-projects-with-gradle/

'git clone https://github.com/jasontian-toosle/lupo.git'
'ls' will show there is folder called lupo
'cd lupo'
'git status' will show master branch name
'git pull origin master' will pull the lastest code from master branch
'git log' show a list of git commit history
'git checkout -b first_commit' will create new branch first_commit
'git branch' will show that you are in branch first_commit
'git status' will show branch first_commit and nothing to commit yet
using intelliJ to import gradle project
make some changes: ie. add some comment in java code
'git status' will show which files have been modified
'git add <filepath>' will add changed file to stage
'git commit' will commit the changes and allow user to add comments
'git log' will show that there is some commit
'git push origin <branch>' will push the commits to remote origin

now login to github and check the repo. you will find your branch, except master which is default. create a pull request and add code reviewer. after some one approved your change, you can merge the request and delete your branch on repo.
back to terminal
'git checkout master' will go to master branch
'git pull' will pull latest changes
'git branch -D <branch>' will delete your branch locally


