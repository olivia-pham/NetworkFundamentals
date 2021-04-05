# NetworkFundamentals
## To clone project:
1. Navigate to the main branch, click on 'Code' button
..* You will see a link for the repo, e.g. https://github.com/olivia-pham/NetworkFundamentals.git which you can copy
3. Open cmd line/Git Bash
4. Type in **cd "file path where you want to store the project"**
5. Type in **git clone 'repo link'** e.g. **git clone https://github.com/olivia-pham/NetworkFundamentals.git**
6. Open up project on cmd line, **cd NetworkFundamentals**
7. To switch branches, **git checkout branchname**
8. After the project has been cloned you should see it stored in your local chosen folder.
9. Open up project in Pycharm: File -> Open Project

## To run:
1. Open cmd and enter **ipconfig** to get IP address
2. Open project in Pycharm and run server.py
3. From another device on the same IP address/network, e.g. phone enter this URL in browser **http://192.168.0.20:6789/simpleWeb.html**
..* Replace 192.168.0.20 with your IP address and 6789 with the port no. of the server, i.e. 80
4. The browser page should show the simpleWeb.html file and the message, 'Hello World!'
5. Try changing the file name in the url, e.g. to hello.html
6. The browser page should show an error message, '404 Not Found'

## To commit changes to project on Github:
https://www.srcmake.com/home/bitbucket-pr 
1. Open the project on cmd line, **cd ".....\NetWorkFundamentals**
2. Make sure you're on the branch where you made changes locally/switch to the branch using git checkout
3. **git status** to see changes made locally
4. **git add 'file name'**, e.g. **git add README.md** to add changes to file (I would add changes to files individually instead of doing **git add .** just in case of any issues.)
5. **git commit -m "commit message"** to add commit message
6. If you want to push to a new branch, **git checkout -b newbranchname**
..* Or just push to existing branch, e.g. **git push --set-upstream origin main**
8. Push changes to Github repo **git push --set-upstream origin newbranchname**
