<a href="http://ec2-54-214-112-22.us-west-2.compute.amazonaws.com/">http://ec2-54-214-112-22.us-west-2.compute.amazonaws.com/</a>

<h1>about this website</h1>

<p>When this project is finished it will show a line graph of the vegas betting line over time alongside a line graph of the betting consensus over the same time for every NFL game each week.  This is intended to more easily show what is called 'reverse line movement.'  When the betting public is wagering heavily on a particular side of a line, the betting houses will sometimes move the line in that direction to encourage wagering on the other side.  However, when the line moves in the opposite direction, it is called 'reverse line movement' and is supposedly an indicator of 'smart money,' or very large wagers placed by a small number of individuals who possibly know more than the betting public.  Therefore, when I see this happening, I can use this to inform my fantasy football lineup.</p>

<h1>how it works</h1>

<p>Currently I have an AWS EC2 instance hosting the website and an AWS RDS hosting the database.  When the project is completed the EC2 instance will run a web scraper written in Python using BeautifulSoup to scrape the game info and vegas lines and upload to the RDS at certain times of the day.  Currently the tables being displayed are sample data located at: <a href="http://ec2-54-214-112-22.us-west-2.compute.amazonaws.com/testdata.php">http://ec2-54-214-112-22.us-west-2.compute.amazonaws.com/testdata.php</a>.  The website itself uses HTML, CSS, and AngularJS.</p>
