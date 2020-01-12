Help Manual

Here in this task I have created three apis. Description are mentioned below:

1.	Created rest api to upload a csv file at server, then created a global pandas dataframe object. This dataframe object can be used with other apis. The benefit of having global dataframe object is that we need not read file again and again when other apis are consumed.

Api Url: 127.0.0.1:5002/uploader

 

2.	Created a api to get info of csv file uploaded on server.

Api url: 127.0.0.1:5002/getfileinfo
 

3.	In this api we pass two column name. In which one is categorical column and one is numerical column. Api return the name of category that holds the maximum groupby sum on that numerical column.

Api Url: 127.0.0.1:5002/check?cat=Ship Mode&num=Sales

For more info refer the Readme.pdf 
