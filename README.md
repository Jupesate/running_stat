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

*24.7.2025 UPDATE*
At this point I have everything that I need from the data which I am interested in. Of course there is cadence and other metrics which can be interesting, but at this point because of work and summer studies I dont have anymore time so I am leaving the code where it is. 
I am really happy with the process and I use my power BI report daily to check my runs and progress, so I am happy to say that this project was a success and is in weekly use. Below I will share are the visuals that I follow in my training. Firstly is the previous 2 months activities.

<img width="1902" height="1109" alt="tiettykk" src="https://github.com/user-attachments/assets/dfd3d349-979e-4908-8eb4-785a0dd4439e" />

Secondly is the over all activities.

<img width="1874" height="1042" alt="kaikki" src="https://github.com/user-attachments/assets/6773e051-43a4-4f10-8b6e-bdf7c6cc7721" />

Then I have dashboard including many interesting visuals for me.

<img width="1914" height="1007" alt="useita_vis" src="https://github.com/user-attachments/assets/b9a45ee5-82b0-41bc-9f7c-7bd6b636b0b4" />

Then I have currenth months runs with average heartrape and speed, to follow aerobic endurance. This can be easily filtered to show only aerobic or speed work

<img width="1867" height="1052" alt="line_chart" src="https://github.com/user-attachments/assets/f01d529f-49d0-4fa6-8ed5-40ac390567c1" />


Lastly I have a dashboard where I can follow over all progress.

<img width="1872" height="1020" alt="dashboard" src="https://github.com/user-attachments/assets/8a976553-efa2-41b1-8303-441cfdfbbe92" />


Feel free to contact if you want to use this or want help in creating these dashboards or help with strava API.

*Summary*

--> Make files and structure pretty (tests?) --> Sort of, no tests yet
--> Improve excel writing logic and process --> DONE
--> Import to power BI --> Done


## Plan
1. From strava get latest runs with API call to their service.
   -Simple
3. Add the data to to excel as a row
     - What data is relevant? how to optimise this
4. Use power Bi to create statistic and graphs
   - Use for fun, try to learn alot


## Final
Learned about power BI and strava API. Learned some data analysis and something new about me as a runner.
Maybe with these insights I can finally run maraton under 3:30 h. Will update after 6.9.2025 Finlandia marathon
*UPDATE - Got the sub 3:30 marathon with a finishing time of 3:28:32. I am still using this project to follow runs althought not so frequently since running is on a hiatus till next summer :D
