# Github events

## GitHub API
- Documentation: [GitHub activity events](https://docs.github.com/en/rest/activity/events?apiVersion=2022-11-28#list-public-events)
- Some repositories have a limit and therefore in some cases it is not possible to download the last 500 events (even if they happened less than 7 days ago)


## Event statistics
- Repo names are hardcoded at the beginning of the script
- For each repo a list of last events (rolling window of either 7 days or 500 events) is fetched and average time between consecutive events is displayed in the chart 

## TODO
- I'm giving up this assignment: "The application should minimize requests to the GitHub API and retain data through application restarts."
- dealing with timezones is not robust. I don't want to deal with it now