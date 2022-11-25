# YouTubeChannelAnalysis
Data Science look at the statistics of a particular YouTube Channel
I used the YouTube Channel MKBHD to analyze his particular stats as a Tech Youtuber. I used the YouTube Api to grab data using the channel ID for MKBHD's particular channel. Being a Tech YouTuber, I find myself watching lots of his videos so I wanted to visualize what his YouTube numbers are using Python.
<img width="1434" alt="Screenshot 2022-11-24 at 9 34 03 PM" src="https://user-images.githubusercontent.com/107436055/203888869-7f8a496a-0ea4-4b7a-be49-758f3ff4a19f.png">
I used a Pandas Dataframe to put his general channel numbers onto a table, then created a function that allowed me to pull the different videos he has uploaded. This aids me in putting his data into infographics throughout his career rather than just looking at just what his channel displays. 
<img width="588" alt="Screenshot 2022-11-24 at 9 37 17 PM" src="https://user-images.githubusercontent.com/107436055/203889212-9ca41f2e-70a0-48a8-b19c-9e64e22cae1c.png">
After converting some columns of the data to be better used in seaborn graphs, I produced the bar chart above showing his best videos of all time by graphing the view count and title variables. 
<img width="558" alt="Screenshot 2022-11-24 at 9 39 30 PM" src="https://user-images.githubusercontent.com/107436055/203889455-0458b94b-1109-472a-920b-2ad72e5445dc.png">
I wanted to analyze the other side of the spectrum and check what were the worst performing videos, this most likely contains videos from his early YouTube era.
<img width="561" alt="Screenshot 2022-11-24 at 9 41 25 PM" src="https://user-images.githubusercontent.com/107436055/203889651-603d8bf9-6d30-469b-9ca3-e518cacd08d4.png">
Using the seaborn module again for data visualization, I wanted to compare if the number of comments/likes corresponds to the number of views that a video receives. Interestingly enough, in MKBHD's case, the like count tends to correspond to higher view counts. However, there are videos where a video receives tons of attention through views but with very little comments. 
