<?xml version="1.0" encoding="utf-8"?>
<!--

# Pretty Feed

Styles an RSS/Atom feed, making it friendly for humans viewers, and adds a link
to aboutfeeds.com for new user onboarding. See it in action:

   https://interconnected.org/home/feed


## How to use

1. Download this XML stylesheet from the following URL and host it on your own
   domain (this is a limitation of XSL in browsers):

   https://github.com/genmon/aboutfeeds/blob/main/tools/pretty-feed-v3.xsl

2. Include the XSL at the top of the RSS/Atom feed, like:

```
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet href="/PATH-TO-YOUR-STYLES/pretty-feed-v3.xsl" type="text/xsl"?>
```

3. Serve the feed with the following HTTP headers:

```
Content-Type: application/xml; charset=utf-8  # not application/rss+xml
x-content-type-options: nosniff
```

(These headers are required to style feeds for users with Safari on iOS/Mac.)



## Limitations

- Styling the feed *prevents* the browser from automatically opening a
  newsreader application. This is a trade off, but it's a benefit to new users
  who won't have a newsreader installed, and they are saved from seeing or
  downloaded obscure XML content. For existing newsreader users, they will know
  to copy-and-paste the feed URL, and they get the benefit of an in-browser feed
  preview.
- Feed styling, for all browsers, is only available to site owners who control
  their own platform. The need to add both XML and HTTP headers makes this a
  limited solution.


## Credits

pretty-feed is based on work by lepture.com:

   https://lepture.com/en/2019/rss-style-with-xsl

This current version is maintained by aboutfeeds.com:

   https://github.com/genmon/aboutfeeds


## Feedback

This file is in BETA. Please test and contribute to the discussion:

     https://github.com/genmon/aboutfeeds/issues/8

-->
<xsl:stylesheet version="3.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/"
                xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
  <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes" />
  <xsl:template match="/">
    <html lang="en">
      <head>
        <meta charset="utf-8" />
        <title>RSS Feed - xythobuz.de</title>
        <meta name="description">
          <xsl:attribute name="content">
            <xsl:value-of select="/rss/channel/description" />
          </xsl:attribute>
        </meta>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="author" href="xythobuz@xythobuz.de" />
        <link rel="shortcut icon" href="img/favicon.ico" />
        <link type="text/css" rel="stylesheet" href="css/style.css" />
      </head>
      <body>
        <div id="wrap"><div id="nav">
          <a>
            <xsl:attribute name="href">
              <xsl:value-of select="/rss/channel/link" />
            </xsl:attribute>
            <h1>
              <xsl:value-of select="/rss/channel/title" />
              - RSS Feed
              <img src="img/rss.png" />
            </h1>
          </a>
        </div></div>
        <div id="content">
          <p>
            This is the RSS feed for my blog.
            You can use it to get notified about new posts automatically.
          </p>
          <p>
            If you're already used to this and wondering why this looks strange, this is a styled RSS feed.
            Just copy the URL into your newsreader.
          </p>
          <p>
            If you don't know what RSS is check out <a href="https://aboutfeeds.com">About Feeds</a> to get started.
          </p>
          <h1>Recent Blog Posts</h1>
          <ul>
          <xsl:for-each select="/rss/channel/item">
            <li>
              <a>
                <xsl:attribute name="href">
                  <xsl:value-of select="link" />
                </xsl:attribute>
                <xsl:value-of select="title" />
              </a>
              <br />
              <span class="listdesc">
                Published: <xsl:value-of select="substring(pubDate, 1, string-length(pubDate) - 15)" />
              </span>
              <br />
              <span class="listdesc">
                Updated: <xsl:value-of select="substring(atom:updated, 1, string-length(atom:updated) - 15)" />
              </span>
            </li>
          </xsl:for-each>
          </ul>
          <p>
            Last rebuild at: <xsl:value-of select="substring(/rss/channel/lastBuildDate, 1, string-length(/rss/channel/lastBuildDate) - 6)" />
          </p>
          <p>
            Styled RSS feed inspired by <a href="https://darekkay.com/blog/rss-styling/">Darek Kay</a> and <a href="https://github.com/genmon/aboutfeeds/blob/main/tools/pretty-feed-v3.xsl">pretty-feed-v3</a>.
          </p>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
