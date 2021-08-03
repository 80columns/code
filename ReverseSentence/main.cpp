#include <iostream>
using namespace std;

string ReverseSentence(string Sentence) {
    size_t EndIndex = Sentence.length() - 1;
    size_t StartIndex = EndIndex;

    // reverse each word in the string
    while (StartIndex >= 0) {
        if (Sentence[StartIndex] == ' ' && StartIndex < EndIndex) {
            // reverse the word starting at StardIndex and ending at EndIndex
            size_t WordHalfLength = (EndIndex - StartIndex) / 2;

            for (size_t j = 0; j < WordHalfLength; j++) {
                char Temp = Sentence[StartIndex + 1 + j];
                Sentence[StartIndex + 1 + j] = Sentence[EndIndex - j];
                Sentence[EndIndex - j] = Temp;
            }

            StartIndex--;
            EndIndex = StartIndex;
        } else if (StartIndex == 0 && StartIndex < EndIndex) {
            // reverse the word starting at StardIndex and ending at EndIndex
            size_t WordHalfLength = ((EndIndex - StartIndex) + 1) / 2;

            for (size_t j = 0; j < WordHalfLength; j++) {
                char Temp = Sentence[StartIndex + j];
                Sentence[StartIndex + j] = Sentence[EndIndex - j];
                Sentence[EndIndex - j] = Temp;
            }

            // break out of the while loop once we've reached the beginning of
            // the string, because StartIndex can never be less than 0 since
            // it's a size_t, which is an unsigned type
            break;
        } else {
            StartIndex--;
        }
    }

    EndIndex = Sentence.length() - 1;
    StartIndex = 0;
    size_t SentenceHalfLength = (EndIndex + 1) / 2;
    
    // reverse the string
    for (size_t j = 0; j < SentenceHalfLength; j++) {
        char Temp = Sentence[StartIndex + j];
        Sentence[StartIndex + j] = Sentence[EndIndex - j];
        Sentence[EndIndex - j] = Temp;
    }

    return Sentence;
}

int main() {
    cout << ReverseSentence("hello world") << "\n";
    cout << ReverseSentence("well hello there this is a really long sentence"
                            " and i'm really glad you read it all the way"
                            " through") << "\n";
    cout << ReverseSentence("do or do not there is no try") << "\n";
}