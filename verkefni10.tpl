<!DOCTYPE html>
<html>
<head>
	<title>verkefni5</title>
	<link rel="stylesheet" href="verkefni6.css">
</head>
<body>	
	<header>
	</header>
	<section>
	<form action="/a_adgang">
		<input type="submit" value="Áttu aðgang?">
	</form>
		<form action="/gogn" method="POST" accept-charset="ISO-8859-1">
			<h1>Nýskráning</h1>
			Netfang:<br>
			<input type="email" name="name" required><br>
			Lykilorð:<br>
			<input type="password" name="psw" pattern="(?=.*[a-z]).{8,}" title="Átta eða fleyri stafir, Þarf að hafa að minsta kosti eina tölu, einn lágstaf og einn hástaf" required><br>
<br>
			<input type="submit" value="Nýskrá">
		</form>
	</section>
</body>
</html>
