byte known_input = 0x20; // space (' ')

var output = "1314111615101016131816121010161314111615101016131816121010161314111615101016131816121010161314111615101016131816121010161314111615101016131816121010161314111615103a";
var flag_output = "667d707561764b4244576946595d53406b5044506f5f585667425d5f6f5b525a484b3f";

var output_bytes = StringToByteArray(output);
//output_bytes.Dump();

var flag_output_bytes = StringToByteArray(flag_output);
//flag_output_bytes.Dump();

var key = output_bytes.Select(x => (byte)(x ^ known_input)).ToArray();
//key.Dump();

byte[] flag_bytes = new byte[flag_output_bytes.Length];

for (int i = 0; i < flag_output_bytes.Length; i++)
{
    flag_bytes[i] = (byte)(flag_output_bytes[i] ^ key[i]);
}

System.Text.Encoding.UTF8.GetString(flag_bytes).Dump();

static byte[] StringToByteArray(string hex)
{
    return Enumerable.Range(0, hex.Length)
                     .Where(x => x % 2 == 0)
                     .Select(x => Convert.ToByte(hex.Substring(x, 2), 16))
                     .ToArray();
}
