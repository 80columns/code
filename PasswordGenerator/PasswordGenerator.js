var PasswordChars = new Array("a", "b", "c", "d", "e", "f", "g", "h",
                              "i", "j", "k", "l", "m", "n", "o", "p",
                              "q", "r", "s", "t", "u", "v", "w", "x",
                              "y", "z", "A", "B", "C", "D", "E", "F",
                              "G", "H", "I", "J", "K", "L", "M", "N",
                              "O", "P", "Q", "R", "S", "T", "U", "V",
                              "W", "X", "Y", "Z", "1", "2", "3", "4",
                              "5", "6", "7", "8", "9", "`", "~", "!",
                              "@", "#", "$", "%", "^", "&", "*", "(",
                              ")", "-", "_", "+", "=", "[", "{", "]",
                              "}", "\\", "|", ":", ";", ",", "<",
                              ".", ">", "/", "?", "\"");
var RandomIndex;
var Password = "";
var i;

for(i = 0; i < 20; i++)
{
    RandomIndex = Math.floor(Math.random()*PasswordChars.length);
    Password = Password + PasswordChars[RandomIndex];
}

document.write(Password);
