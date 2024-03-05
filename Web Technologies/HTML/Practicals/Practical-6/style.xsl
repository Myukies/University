<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <head>
        <link rel="stylesheet" type="text/css" href="style.css"/>
      </head>
      <body>
        <h1>Books Catalog</h1>
        <xsl:apply-templates select="catalog"/>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="catalog">
    <div>
      <xsl:apply-templates select="book"/>
    </div>
  </xsl:template>

  <xsl:template match="book">
    <div>
      <h2><xsl:value-of select="title"/></h2>
      <p><xsl:value-of select="author"/></p>
      <p><xsl:value-of select="year"/></p>
    </div>
  </xsl:template>
</xsl:stylesheet>
