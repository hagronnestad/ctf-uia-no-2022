var c = new HttpClient();

while (true)
{
	var s = await c.GetStringAsync("http://ctf.uiactf.no:3008/index.php?hent_side=true");
	if (!s.Contains("Nope!")) s.Dump();
}
