<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="3.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:xhtml="http://www.w3.org/1999/xhtml"
                xmlns:sitemap="http://www.sitemaps.org/schemas/sitemap/0.9">
  <xsl:output method="html" version="5" encoding="UTF-8" indent="yes" />
  <xsl:template match="/">
    <html lang="en">
      <head>
        <meta charset="utf-8" />
        <title>Sitemap - xythobuz.de</title>
        <meta name="description" content="Electronics &amp; Software Projects" />
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
                <a href="/">xythobuz.de - Sitemap</a>
              </li>
            </ul>
          </div>
        </div>
        <div id="content">
          <h1>Sitemap</h1>
          <p>
            This is the Sitemap for my blog.
            You can use it to find every subpage on this website.
          </p>
          <ul>
          <xsl:for-each select="/sitemap:urlset/sitemap:url">
            <li>
              <a>
                <xsl:attribute name="href">
                  <xsl:value-of select="sitemap:loc" />
                </xsl:attribute>
                <xsl:value-of select="xhtml:title" />
              </a>
              <br />
              <span class="listdesc">
                Updated: <xsl:value-of select="sitemap:lastmod" />
              </span>
              <br />
              <span class="listdesc">
                Change Frequency: <xsl:value-of select="sitemap:changefreq" />
              </span>
              <br />
              <span class="listdesc">
                Priority: <xsl:value-of select="sitemap:priority" />
              </span>
              <xsl:choose>
                <xsl:when test="xhtml:link">
                  <br />
                  <span class="listdesc">
                    Alternative language: <a>
                      <xsl:attribute name="href">
                        <xsl:value-of select="xhtml:link/@href" />
                      </xsl:attribute>
                      <xsl:value-of select="xhtml:link/@hreflang" />
                    </a>
                  </span>
                </xsl:when>
                <xsl:otherwise>
                  <br />
                  <span class="listdesc">
                    No other languages for this page.
                  </span>
                </xsl:otherwise>
              </xsl:choose>
            </li>
          </xsl:for-each>
          </ul>
          <p>
            Styled Sitemap inspired by <a href="rss.xml">Styled RSS Feed</a>.
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
            <a href="https://codeberg.org/xythobuz/website/src/branch/master/static/css/sitemap.xsl?display=source">
              View Source 'css/sitemap.xsl'</a> (<a href="/css/sitemap.xsl">locally</a>)
          </span>
          <br />
          <a href="https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fwww.xythobuz.de%2Fcss%2Fstyle.min.css">
            <img src="data/valid-css.svg" alt="Valid CSS" />
          </a>
        </div>
        <script type="text/javascript" src="js/jquery-3.7.1.min.js"></script>
        <script type="text/javascript" src="js/tracking.min.js"></script>
        <script type="text/javascript" src="js/scroller.min.js"></script>
        <script type="text/javascript" src="js/resize.min.js"></script>
        <script type="text/javascript" src="js/oneko.min.js"></script>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
