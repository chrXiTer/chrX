<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - chrX's Website'</title>
    <link rel="stylesheet" href="../c3.css" />

    <style type="text/css">
        header {
            width:100%;
            background-color:#4d4545;
            height:36px;
            text-align:left
        }
        header nav{
            line-height:36px;
        }

        nav a{
            display:inline-block;
            padding-left:10px;
            padding-right:10px;
            height:100%;
        }
        nav a:link, nav a:visited{
            text-decoration: none;
            color : #ffffff;
            font-size:18px;
        }
        nav a:hover, nav a:active{
            background-color:#6d6565;
        }

        .currentHeaderNavA{
            background-color:#8d8585;
        }

        @media (max-width: 450px) {
            header{
                position:fixed;
                top:0px;
            }
        }

    </style>
</head>

<body>
    <header>
	<nav>
		<a href="/html/html_intro.htm">html5</a>
		<a href="/css/css_intro.htm">css3</a>
		<a href="/js/js_intro.htm">javascript</a>
		<a href="/other/index.htm">other</a>
	</nav>
    </header>
	{{!base}}
	<br/>
	<footer style="clear:both">
		<p>&copy; 2015 - chrX</p>
	</footer>

</body>
</html>
