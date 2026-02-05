Web crawler:
A web crawler is a program that automatically visits web pages, downloads their HTML content, and follows links found on those pages to discover other web pages. Web crawlers are commonly used by search engines to index websites and collect data from the internet.
Seed URL:
A seed URL is the starting web address from which the crawler begins its operation. The crawler first downloads the seed URL and then finds new links from that page to continue crawling.
Visited Set Need:
A visited set is used to keep track of all URLs that have already been crawled. It is needed to:
Avoid visiting the same page multiple times
Prevent infinite loops
Reduce unnecessary network requests
Improve crawling efficiency
Without a visited set, the crawler may keep crawling the same pages again and again.
Output:
The crawler fetched 5 web pages
Each page was saved as an .html file inside the pages/ folder
Files were saved as page_1.html, page_2.html, page_3.html, page_4.html, page_5.html
The console displayed logs showing:
Which URL was being fetched
Which file was saved
How many links were extracted from each page