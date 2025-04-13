# Topic 5: Assignment 4 - GitHub API 
# Author: Sharon Curley

from github import Github
import requests
from config import config as cfg

apikey = cfg["githubkey"]

#print(type(cfg))  # <class 'dict'>

g = Github(apikey)

#for repo in g.get_user().get_repos():      
#    print(repo.name)                       # test prints all my repositories

repo = g.get_repo("SBCURLEY/wsaa-assignments")  
#print(repo.clone_url)                      # test prints the repository name

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)

#newContents = contentOfFile + " another Andrew \n"     # adding in another Andrew to the file

newContents = contentOfFile.replace("Andrew","Sharon")  # replacing Andrew with Sharon
print (newContents)

gitHubResponse=repo.update_file(fileInfo.path,"Updated by prog",newContents,fileInfo.sha)
print("File updated successfully:", gitHubResponse)