## Exercise: Web Scraping, Part 2

### What You’ll Build

Blogs and other regularly updating websites usually have a front
page with the most recent post as well as a Previous button on the 
page that takes you to the previous post. Then that post will also 
have a Previous button, creating a trail from the most recent page 
to the first post on the site. If you wanted a copy of the site’s 
content to read when you’re not online, you could manually navigate 
over every page and save each one. But this is pretty boring work, 
so let’s write a program to do it instead.

[XKCD](https://xkcd.com/) is a popular geek webcomic with a website 
that fits this structure. The front page has a Prev button that 
guides the user back through prior comics. Downloading each comic by
hand would take forever, but you can write a script to do this in a couple 
of minutes.

Before you start, you’ll need to learn how to use two external 
packages: Requests and Beautiful Soup.

