def get_posts_details(rss=None):
	if rss is not None:
		import feedparser
		blog_feed = blog_feed = feedparser.parse(rss)
		posts = blog_feed.entries
		posts_details = {"Blog Title" : blog_feed.feed.title,
						"Blog Link" : blog_feed.feed.link}
		post_list = []
    
		for post in posts:
			temp = dict()
			
			try:
        temp["Link"] = post.link
				temp["Title"] = post.title
        temp["Author(s)"] = [author.name for author in post.authors]
				temp["Time of publication"] = post.published
				temp["Summary"] = post.summary
        temp["Tags"] = [tag.term for tag in post.tags]
			except:
				pass
			
			post_list.append(temp)
		
		posts_details["posts"] = post_list
		
		return posts_details 
	else:
		return None

if __name__ == "__main__":
  import json
  feed_url = "https://xxxx.hashnode.dev/rss.xml" # Enter an RSS Feed link here.
  data = get_posts_details(rss = feed_url) 
  if data:
    print(json.dumps(data, indent=2))
  else:
    print("None")
