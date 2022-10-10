using System.Security.Cryptography;

string characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" +
                    "abcdefghijklmnopqrstuvwxyz" +
                    "!@#$%^&*()_., <>?/" +
                    "1234567890";

Console.WriteLine($"Your password is: {GeneratePassword(26, characters)}");

string GeneratePassword(int length, IEnumerable<char> characterSet)
{
    var bytes = new byte[length! * 8];
    var characterArray = characterSet!.Distinct().ToArray();

    using (var rng = RandomNumberGenerator.Create())
    {
        rng.GetBytes(bytes);

        var result = new char[length];

        for (int i = 0; i < length; i++)
        {
            ulong value = BitConverter.ToUInt64(bytes, i * 8);
            result[i] = characterArray[value % (uint)characterArray.Length];
        }

        return new string(result);
    }
}
