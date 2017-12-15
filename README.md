# Github Visualisation Web-app #
A Django webserver visualising github data.
### Visualizing number of open issues and number of stars for all of the public repositories by google ###
  ![screenCapture](screenshots/google_repos_6pm.png)

### Number of Commits per Contributor on a Repository. ###
  ![screenCapture](screenshots/repo_contributor_google_ubps.png)

  Data is gathered from the github api and stored in a SQLite database. This is done to cache data to reduce the number of      queries needed to the Github Api. This data is then fetched using a json api to the pages that display the data. The data is visualized using the D3.js library.

### JSON API Example. ###
  ![screenCapture](screenshots/google_repos_api_6pm.png)
  
### JSON API Example: Individual Repository ###
  ![screenCapture](screenshots/google_contributors_api_6pm.png)



