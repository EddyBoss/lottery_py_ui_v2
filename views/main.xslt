<?xml version="1.0" encoding="UTF-8"?>

<?xml-stylesheet href="../styles/style.css" type="text/css"?>
<xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
    <html>
    <body>
        <h1>Lottery</h1>
        <xsl:apply-templates select="lottery"/>
        <h1>Lottery UI</h1>
        <table class="grid_template">
            <tr>
                <th>Number</th>
                <th>Number</th>
                <th>Number</th>
            </tr>   
            <tr>
                <th>Number</th>
                <th>Number</th>
                <th>Number</th>
            </tr>   
            <tr>
                <th>Number</th>
                <th>Number</th>
                <th>Number</th>
            </tr>   
        </table>
    </body>
    </html>

</xsl:template>

</xsl:stylesheet>
