# 0x19. Postmortem

![](https://www.meme-arsenal.com/memes/e06b646269fbb79a05379b58976cb932.jpg)

## Issue Summary
An expasnsion which lead to an updgrad to the codebase was initiated and launched a day before some tickets where opened on problems caused by the update. The ticket was openned for review and the attending officer investigated and confirm the issue which the engineering team were notified to trace the bug, after some wrong hunch the bug were discorved to be caused by a misspell in the data base model. This was corrected and new update was pushed. Damage was limited to under 3hrs from the time of detection. 

## Events Timeline
- 04-12-2022 7:23 AM GMT+1 - Some users opened a ticket that they couldn't sign in to their dashboard.
- 04-12-2022 8:12 AM GMT+1 - Murphy, a customer representative reviewed the ticket and tested it out to find the same issue.
- 04-12-2022 8:25 AM GMT+1 - Murphy alerted the engineers and We investigated the controllers and the views for inconsistencies.
- 04-12-2022 9:10 AM GMT+1 - We assumed the db schema/model being used was either at fault or used incorrectly after a recent update because the error message on console indicated that the model  was raising an error preventing proper communication with the database.
- 04-12-2022 9:35 AM GMT+1 - We checked that the views might not be validating the form fields the right way to satisfy the model requiremets, but eventually wasn't the cause.
- 04-12-2022 9:52 AM GMT+1 - The engineering team eventually found a mispell in the last built that was shipped out and made the corrections.
- 04-12-2022 10:05 AM GMT+1 - Everything eventually returned back to normal.

## Root Cause And Resolution
The redeveloped model for the database migration had an error from a day earlier possibly from a code review, which eventually caused the error that prevented the users from gaining access into their dashboards. Eventually the engineering team was able to trace the bug to the database model set up and the misspell was corrected and the issue was resolved.

## Corrective And Preventative Measures
- Setup a continuous integration pipeline to run a build on each pull request branch. This would ensure that builds are passing in the pull request branch before it is merged with the deployment branch.
- Setup a monitoring system for the database and application servers to keep track of any issue that may occur.
- Develop tests that need to be passed for each new feature and those tests should be passing before they are merged with the deployment branch.