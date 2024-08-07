# Github events

## GitHub API
- Documentation: [GitHub activity events](https://docs.github.com/en/rest/activity/events?apiVersion=2022-11-28#list-public-events)
- Some repositories have a limit and therefore in some cases it is not possible to download the last 500 events (even if they happened less than 7 days ago)
---

## Event statistics
- Repo names are hardcoded at the beginning of the script
- For selected repo a list of last events (rolling window of either 7 days or 500 events) is fetched and average time between consecutive events is displayed in the chart
- Keeping previously downloaded events to minimize requests to the GitHub API.

## TODO & Missing parts
- Making an application
  - I've made it just as a jupyter notebook instead of an application.
- Dealing with timezones is not robust. I don't want to deal with it now.
- Retain data through application restarts
  - is done using pandas and reading and writing CSV file. It's not an ideal solution. I would consider a different approach here