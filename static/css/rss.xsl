<?xml version="1.0" encoding="utf-8"?>
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
        <div id="wrap">
          <div id="nav">
            <ul id="navbar">
              <li id="home">
                <a>
                  <xsl:attribute name="href">
                    <xsl:value-of select="/rss/channel/link" />
                  </xsl:attribute>
                  <xsl:value-of select="/rss/channel/title" />
                </a>
              </li>
              <li>
                <img src="img/rss.png" alt="RSS feed icon" />
              </li>
            </ul>
          </div>
        </div>
        <div id="content">
          <h1>
            RSS Feed
          </h1>
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
          <h2>Recent Blog Posts</h2>
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
                Published: <xsl:value-of select="substring(pubDate, 1, string-length(pubDate) - 6)" />
              </span>
              <br />
              <span class="listdesc">
                Updated: <xsl:value-of select="substring(atom:updated, 1, string-length(atom:updated) - 6)" />
              </span>
              <div class="collapse">
                Expand article contents.
              </div>
              <div class="collapsecontent">
                <iframe style="width: 100%; border-width: 0px;">
                  <xsl:attribute name="srcdoc">
                    <xsl:value-of select="description" />
                  </xsl:attribute>
                </iframe>
              </div>
            </li>
          </xsl:for-each>
          </ul>
          <p>
            Styled RSS feed inspired by <a href="https://darekkay.com/blog/rss-styling/">Darek Kay</a> and <a href="https://github.com/genmon/aboutfeeds/blob/main/tools/pretty-feed-v3.xsl">pretty-feed-v3</a>.
          </p>
          <hr id="footbar" />
        </div>
        <div id="scroll_up"></div>
        <div id="footer">
          <a rel="jslicense" href="licensing.html" data-jslicense="1">Licensing</a>
          ·
          <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-BY-NC-SA</a>
          ·
          <a rel="license" href="https://www.gnu.org/licenses/gpl-3.0.html">GPLv3</a>
          <br />
          <a href="https://hg.sr.ht/~obensonne/poole">Poole</a>
          ·
          <a href="https://jquery.com">jQuery</a>
          ·
          <a href="http://shjs.sourceforge.net">SHJS</a>
          ·
          <a href="https://github.com/sachinchoolur/lightGallery">lightGallery</a>
          ·
          <a href="https://github.com/adryd325/oneko.js">oneko.js</a>
          <br />
          <a href="https://github.com/sponsors/xythobuz">GitHub Sponsors</a>
          ·
          <a href="http://www.amazon.de/?_encoding=UTF8&amp;camp=1638&amp;creative=19454&amp;linkCode=ur2&amp;site-redirect=de&amp;tag=xythobuzorg-21">Amazon.de Affiliate</a>
          ·
          <a href="https://www.paypal.com/us/cgi-bin/webscr?cmd=_send-money&amp;nav=1&amp;email=xythobuz@me.com">PayPal</a>
          <br />
          <span style="font-size: x-small">
              <a href="https://codeberg.org/xythobuz/website/src/branch/master/static/css/rss.xsl?display=source">
                View Source 'css/rss.xsl'</a> (<a href="/css/rss.xsl">locally</a>)
          </span>
          <br />
          <span style="font-size: xx-small">
              RSS feed generated at <xsl:value-of select="substring(/rss/channel/lastBuildDate, 1, string-length(/rss/channel/lastBuildDate) - 6)" />
          </span>
        </div>
        <script type="text/javascript" src="js/jquery-3.7.1.min.js"></script>
        <script type="text/javascript" src="js/tracking.min.js"></script>
        <script type="text/javascript" src="js/scroller.min.js"></script>
        <script type="text/javascript" src="js/resize.min.js"></script>
        <script type="text/javascript" src="js/oneko.min.js"></script>
        <script type="text/javascript" src="js/auto_toc.min.js"></script>
        <script type="text/javascript" src="js/collapse.min.js"></script>
        <script type="text/javascript" src="js/iframe.min.js"></script>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
