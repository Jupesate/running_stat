## Summary
Analysing runs with Power BI, just for fun.

## Current situation

Files are very messy and i have been going with the flow without that much cleaning done.
But now 14.6 I achieved the first "big" milestone which is getting the relevant data to excel and the ability to filter it.
Next up would be the cleaning of the files or thinking of a better logic how to save to excel.
Currently it writes to excel and removes what there were previously. Would be wise to make multiple sheets e.g "may, june, july, august"
Theres not really point of making one bigsheet where i would append the months since i can just fetch all if the need be.
Also It would be nice to write them to excel such as they would be in nice table.

*8.7.2025 UPDATE*
Now the overall usage of the program is much easier. You dont need to worry about the unix time and the excel
writing logic is finalised. Next step would be to make some tests and clean up the files and improve over all
look and documentation of the program. This will be done eventually, but for the next step I will move onto
Power BI. If i get something interesting I will add a screenshot here.

*9.7.2025 UPDATE**
Made my first PowerBi report, this was just a quick one and this could be done in excel likewiese. Didnt have the time
to really get into it and also noticed few problems which need to be addressed in what data I bring to the excel files.

*11.7.2025 UPDATE**
Past few days I have been trying to get hang of Power BI, especially through making new measures which leverage the data that I am using. Some small problem we're the changing of average speed to min/km in python, reversed so I only take m/s and calculate the pace through that in Power BI through measures. Same goes for moving length of session, it was not a good idea to change it to more readable form from total seconds to hh:mm:ss. So reversed that also and calculated that through formatting and measures in Power BI. Overall valuable lessons learned on why the API gives values as they are and the end responsibility is on the user to change it to readable form after leveraging it. Below is quick update now when I can count the averages for everything.

<img width="2004" height="1103" alt="image" src="https://github.com/user-attachments/assets/b0a141a4-cc06-4abb-a953-32110846df2c" />

Now I can move onto more challenging visuals since I have all the data in the form that I need and also have it in readable form.


*Summary*

--> Make files and structure pretty (tests?)
--> Improve excel writing logic and process --> DONE
--> Import to power BI


## Plan
1. From strava get latest runs with API call to their service.
   -Simple
3. Add the data to to excel as a row
     - What data is relevant? how to optimise this
4. Use power Bi to create statistic and graphs
   - Use for fun, try to learn alot


## Final
Learned about power BI and strava API. Learned some data analysis and something new about me as a runner.
Maybe with these insights I can finally run maraton under 3:30 h
